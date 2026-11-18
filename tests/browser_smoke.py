"""Playwright smoke: local assets only; no real contact submission."""
import os
from pathlib import Path
import base64
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
html = (ROOT / "index.html").read_text(encoding="utf-8")
css = (ROOT / "styles.css").read_text(encoding="utf-8")
js = (ROOT / "script.js").read_text(encoding="utf-8")
html = html.replace('<link rel="stylesheet" href="/styles.css">', "<style>" + css + "</style>")
html = html.replace('<script src="/script.js" defer></script>', "<script>" + js + "</script>")
snapshot = base64.b64encode((ROOT / "assets/hypenosys-ui-test.png").read_bytes()).decode("ascii")
html = html.replace('src="/assets/hypenosys-ui-test.png"',
                    'src="data:image/png;base64,' + snapshot + '"')
assert "<style>" in html and "<script>" in html, "Failed to inline local assets"
artifacts = ROOT / "browser-artifacts"
artifacts.mkdir(exist_ok=True)
errors = []
with sync_playwright() as playwright:
    chrome_executable = os.environ.get("CHROME_EXECUTABLE")
    browser = playwright.chromium.launch(
        headless=True, **({"executable_path": chrome_executable} if chrome_executable else {})
    )
    try:
        for width, height in [(320, 790), (390, 844), (768, 1024), (1024, 768), (1440, 900)]:
            ctx = browser.new_context(viewport={"width": width, "height": height}, device_scale_factor=1)
            page = ctx.new_page()
            page.on("pageerror", lambda error: errors.append(str(error)))
            page.set_content(html, wait_until="domcontentloaded")
            page.locator("h1").wait_for()
            page.screenshot(path=str(artifacts / f"hero-{width}.png"), timeout=15000)
            assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth"), f"overflow at {width}px"
            assert page.get_by_role("main").count() == 1
            assert page.get_by_role("heading", level=1).count() == 1
            assert page.locator('main#contenido[tabindex="-1"]').count() == 1
            assert page.locator('#contact-form[aria-describedby="contact-privacy-note"]').count() == 1
            assert page.locator(".writing-list a").count() == 6
            assert page.locator(".contact-form input[required]").count() == 3
            assert page.locator(".contact-form textarea[required]").count() == 1
            assert not page.locator("#contact-form").evaluate("f => f.checkValidity()")
            theme = page.locator("#theme-toggle")
            before = page.locator("html").get_attribute("data-theme")
            theme.click()
            assert page.locator("html").get_attribute("data-theme") != before
            theme.click()
            assert theme.get_attribute("aria-pressed") == str(before == "dark").lower()
            assert theme.get_attribute("aria-label") in ("Activar modo oscuro", "Activar modo claro")
            page.locator("#archivo summary").click()
            assert page.locator("#archivo").evaluate("d => d.open")
            assert page.locator(".archive-list > a").count() == 7
            evidence = page.locator("#hypenosys-interfaz")
            assert evidence.count() == 1
            evidence.locator("summary").click()
            assert evidence.evaluate("d => d.open")
            assert evidence.locator('img[loading="lazy"]').count() == 1
            evidence.locator("img").scroll_into_view_if_needed()
            page.wait_for_function("""() => {
                const img = document.querySelector('#hypenosys-interfaz img');
                return img && img.complete && img.naturalWidth === 1280 && img.naturalHeight === 720;
            }""")
            if width == 1440:
                evidence.screenshot(path=str(artifacts / "project-evidence-1440.png"), timeout=15000)
            evidence.locator("summary").click()
            assert not evidence.evaluate("d => d.open")
            page.locator("#clonar-repos summary").click()
            assert page.locator(".clone-copy").count() == 8
            page.evaluate('window.location.hash = "#EditMovie"')
            page.wait_for_timeout(80)
            assert page.locator("#archivo").evaluate("d => d.open")
            nav = page.locator("#mobile-nav")
            if width <= 740:
                assert nav.is_visible()
                nav.locator("summary").click()
                assert nav.evaluate("d => d.open")
                assert page.locator(".mobile-nav-panel a").count() == 5
                nav.locator("summary").press("Escape")
                assert not nav.evaluate("d => d.open")
                nav.locator("summary").click()
                page.locator('.mobile-nav-panel a[href="#sobre-mi"]').click()
                assert not nav.evaluate("d => d.open")
            else:
                assert not nav.is_visible()
            if width in (390, 1440):
                page.locator("#contacto").scroll_into_view_if_needed()
                page.screenshot(path=str(artifacts / f"contact-{width}.png"), timeout=15000)
            ctx.close()
            print(f"PASS: {width}px, layout + theme + links + form + navigation")
    finally:
        browser.close()
assert not errors, errors
print("Browser smoke PASS; no external submissions.")
