"""Regresiones editoriales y de interfaz del portafolio; no hacen peticiones externas."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
CSS = (ROOT / "styles.css").read_text(encoding="utf-8")
JS = (ROOT / "script.js").read_text(encoding="utf-8")


class PortfolioSmokeTests(unittest.TestCase):
    def test_core_files(self):
        for relative in ("index.html", "styles.css", "script.js", "404.html", "privacidad.html", "assets/axlfc-mark.svg"):
            with self.subTest(relative=relative):
                self.assertTrue((ROOT / relative).is_file())

    def test_document(self):
        self.assertIn('<html lang="es"', HTML)
        self.assertEqual(len(re.findall(r"<h1\b", HTML)), 1)
        self.assertIn('href="/styles.css"', HTML)
        self.assertIn('src="/script.js"', HTML)

    def test_original_anchors(self):
        for anchor in ("home", "about", "projects", "skills", "ethics", "articles", "contact"):
            with self.subTest(anchor=anchor):
                self.assertIn(f'id="{anchor}"', HTML)

    def test_contact_form(self):
        self.assertRegex(HTML, r'action="https://formsubmit\.co/[a-zA-Z0-9]+"')
        for name in ("name", "email", "subject", "message", "_next", "_honey"):
            with self.subTest(name=name):
                self.assertIn(f'name="{name}"', HTML)
        self.assertIn('https://axlfc.github.io/?success=true#contacto', HTML)
        self.assertNotIn("previsualización local", JS.lower())
        self.assertNotIn('action="#contacto"', HTML)

    def test_legacy_projects(self):
        paths=("RuneScript","find-a-job","UE5-python","file_converters","edit-movie","ScriptsStudio","ReplikaAI","get-winget")
        for repo in paths:
            with self.subTest(repo=repo):
                self.assertIn(repo, HTML)

    def test_communication_channels(self):
        for channel in ("github.com/Axlfc","linkedin.com/in/axelcurros","dev.to/axlfc","mastodon.social/@axlfc"):
            self.assertIn(channel, HTML)

    def test_articles_and_principles(self):
        self.assertGreaterEqual(HTML.count("medium.com/@axelfernandezcurros"), 6)
        self.assertIn("FLOSS", HTML)

    def test_accessibility_and_responsive(self):
        self.assertIn("prefers-reduced-motion", CSS)
        self.assertIn(":focus-visible", CSS)
        self.assertIn('class="skip-link"', HTML)
        self.assertIn("viewport", HTML)
        self.assertIn("mobile-nav", HTML)

    def test_publication_guardrails(self):
        self.assertNotIn("Esta es una previsualización local", HTML)
        self.assertNotRegex(HTML, r"(?i)diputaci[oó]n de tarragona|gabinet[e]? de presidencia")
        self.assertIn("privacidad.html", HTML)
        self.assertNotIn("assets/axlfc-social.png", HTML)


if __name__ == "__main__":
    unittest.main()
