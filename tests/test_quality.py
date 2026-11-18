"""Independent WCAG-like contrast and navigation integrity regression checks.

This is a deterministic token-level check, not a full WCAG conformance audit.
"""
import re
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
CSS = (ROOT / 'styles.css').read_text(encoding='utf-8')
HTML = (ROOT / 'index.html').read_text(encoding='utf-8')


def tokens(text):
    result = dict(re.findall(r'(--[\w-]+):\s*(#[0-9a-fA-F]{3,6})', text))
    return {key: ('#' + ''.join(c * 2 for c in val[1:]) if len(val) == 4 else val) for key, val in result.items()}


def luminance(color):
    v = [int(color[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in v]
    return sum(x * w for x, w in zip(c, (0.2126, 0.7152, 0.0722)))


def contrast(a, b):
    large, small = sorted((luminance(a), luminance(b)), reverse=True)
    return (large + 0.05) / (small + 0.05)


class Tags(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []

    def handle_starttag(self, name, attrs):
        self.tags.append((name, dict(attrs)))


class PortfolioQualityTests(unittest.TestCase):
    def test_main_text_contrast_in_both_themes(self):
        light = tokens(CSS.partition('[data-theme=dark]')[0])
        dark = tokens(CSS.partition('[data-theme=dark]')[2].partition('}')[0])
        for theme, palette in [('light', light), ('dark', dark)]:
            for fg in ('--ink', '--muted', '--subtle', '--accent'):
                for bg in ('--paper', '--surface'):
                    with self.subTest(theme=theme, foreground=fg, background=bg):
                        self.assertGreaterEqual(
                            contrast(palette[fg], palette[bg]), 4.5,
                            f'{theme}: {fg} on {bg} has insufficient contrast',
                        )
        self.assertGreaterEqual(contrast('#ffffff', light['--accent']), 4.5)
        self.assertGreaterEqual(contrast('#172125', dark['--accent']), 4.5)

    def test_all_local_fragment_links_resolve_to_unique_ids(self):
        parser = Tags()
        parser.feed(HTML)
        identifiers = [attrs['id'] for _, attrs in parser.tags if attrs.get('id')]
        self.assertEqual(len(identifiers), len(set(identifiers)), 'duplicate HTML IDs')
        for tag, attrs in parser.tags:
            if tag != 'a':
                continue
            href = attrs.get('href', '')
            if href.startswith('#') and len(href) > 1:
                with self.subTest(href=href):
                    self.assertIn(href[1:], identifiers)

    def test_external_links_opened_in_new_tabs_are_isolated(self):
        parser = Tags()
        parser.feed(HTML)
        for tag, attrs in parser.tags:
            if tag != 'a' or attrs.get('target') != '_blank':
                continue
            with self.subTest(url=attrs.get('href')):
                rel = attrs.get('rel', '').split()
                self.assertIn('noopener', rel)
                self.assertIn('noreferrer', rel)
                self.assertEqual(urlsplit(attrs.get('href','')).scheme, 'https')

    def test_form_does_not_submit_during_ci(self):
        parser = Tags()
        parser.feed(HTML)
        forms = [attrs for name, attrs in parser.tags if name == 'form']
        self.assertEqual(len(forms), 1)
        self.assertTrue(forms[0]['action'].startswith('https://formsubmit.co/'))
        for field in ('name', 'email', 'subject', 'message'):
            self.assertTrue(
                any(attrs.get('name') == field and 'required' in attrs
                    for _, attrs in parser.tags),
                f'missing required contact field: {field}',
            )


if __name__ == '__main__':
    unittest.main()
