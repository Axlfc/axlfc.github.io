# Axlfc Portfolio — V2 editorial redesign

This draft branch experiments with a **personal**, multilingual-ready, editorial portfolio focusing on public evidence of work in software, web, systems and creative technology.

## Structure
- `index.html`: semantic editorial content, projects, references, articles and contact form.
- `styles.css`: independent CSS design system, color themes, responsive layouts.
- `script.js`: progressive enhancement (theme, anchored archive links, copy controls, form redirect).
- `privacidad.html`: provisional privacy information for FormSubmit, pending legal verification.
- `assets/axlfc-mark.svg`: lightweight favicon.
- `tests/test_portfolio.py`: static regression tests; CI also checks Jekyll build.

## Local checks
```sh
python -m unittest discover -s tests -v
node --check script.js
bundle exec jekyll build
```

## Publication
This is a **Draft PR candidate**, not a production release. Do not merge before all release gates in `docs/portfolio-v2/RELEASE-CHECKLIST.md` are checked. The FormSubmit action is the existing public recipient from `master`; do not send real test messages without approval.

The old site stays available on `master`.
