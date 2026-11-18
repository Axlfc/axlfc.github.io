"""Auditoría automatizada axe-core WCAG 2.0/2.1 A/AA.

Ejecuta Chromium sobre HTML/CSS/JS locales, sin solicitudes de red ni envíos.
No certifica cumplimiento WCAG ni sustituye pruebas manuales.
"""
import base64
import json
import os
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
AXE = Path(os.environ.get("AXE_CORE_PATH", "/tmp/axlfc-a11y/node_modules/axe-core/axe.min.js"))
if not AXE.is_file():
    raise SystemExit(f"axe-core no encontrado: {AXE}")

css = (ROOT / "styles.css").read_text(encoding="utf-8")
js = (ROOT / "script.js").read_text(encoding="utf-8")
image = base64.b64encode((ROOT / "assets/hypenosys-ui-test.png").read_bytes()).decode("ascii")
pages = {
    "home": (ROOT / "index.html").read_text(encoding="utf-8")
        .replace('<link rel="stylesheet" href="/styles.css">', f"<style>{css}</style>")
        .replace('<script src="/script.js" defer></script>', f"<script>{js}</script>")
        .replace('src="/assets/hypenosys-ui-test.png"', f'src="data:image/png;base64,{image}"'),
    "privacy": (ROOT / "privacidad.html").read_text(encoding="utf-8")
        .replace('<link rel="stylesheet" href="/styles.css">', f"<style>{css}</style>"),
    "not-found": (ROOT / "404.html").read_text(encoding="utf-8")
        .replace('<link rel="stylesheet" href="/styles.css">', f"<style>{css}</style>"),
}
all_violations = []
with sync_playwright() as pw:
    chrome_executable = os.environ.get("CHROME_EXECUTABLE")
    browser = pw.chromium.launch(
        headless=True, **({"executable_path": chrome_executable} if chrome_executable else {})
    )
    try:
        for name, html in pages.items():
            for theme in ("light", "dark"):
                page = browser.new_page(viewport={"width": 390 if name == "home" else 1024, "height": 844}, reduced_motion="reduce")
                page.set_content(html, wait_until="domcontentloaded")
                page.evaluate("(theme) => { document.documentElement.dataset.theme = theme; }", theme)
                page.add_script_tag(path=str(AXE))
                results = page.evaluate("""async () => await axe.run(document, {
                    runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'] }
                })""")
                for violation in results["violations"]:
                    entry = {
                        "page": name, "theme": theme, "id": violation["id"],
                        "impact": violation["impact"],
                        "description": violation["description"],
                        "nodes": [{"target": n["target"], "summary": n["failureSummary"]}
                                  for n in violation["nodes"][:6]],
                    }
                    all_violations.append(entry)
                    print(f"{name}/{theme}: {violation['impact']} {violation['id']} "
                          f"({len(violation['nodes'])} affected nodes)")
                print(f"{name}/{theme}: {len(results['passes'])} axe checks passed")
                page.close()
    finally:
        browser.close()
report = ROOT / "browser-artifacts" / "axe-report.json"
report.parent.mkdir(exist_ok=True)
report.write_text(json.dumps(all_violations, ensure_ascii=False, indent=2), encoding="utf-8")
blocking = [x for x in all_violations if x["impact"] in ("critical", "serious")]
if blocking:
    print(json.dumps(blocking, ensure_ascii=False, indent=2)[:15000])
    raise SystemExit(f"{len(blocking)} serious/critical axe-core violations; see {report}")
print(f"axe-core audit complete: {len(all_violations)} findings, 0 serious/critical. "
      "Manual accessibility review remains required.")
