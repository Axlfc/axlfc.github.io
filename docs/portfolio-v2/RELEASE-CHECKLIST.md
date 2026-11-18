# Portfolio V2 — Draft release gates

Source: V2.4 editorial prototype, migrated to explicit production assets.

## Preserved and checked
- [x] Original public name and `axlfc.` visual identity
- [x] Eight historical project links, including RuneScript, and new selected work
- [x] Six Medium articles, public contact profiles and original FormSubmit recipient
- [x] Contact fields, honeypot, corrected success query and privacy disclosure
- [x] Original anchors (`#home`, `#about`, `#projects`, `#skills`, `#ethics`, `#articles`, `#contact`)
- [x] Mobile navigation, theme preference and reduced-motion support
- [x] Legacy item aliases (`#EditMovie`, `#GetWinget`) inside expandable content
- [x] Static smoke tests and CI configuration

## Controles finales y verificaciones humanas
- [x] GitHub Actions: static tests, Jekyll build and real browser Playwright smoke PASS (2026-11-18)
- [ ] Comprobar de forma controlada la recepción en el buzón del titular (no se envían mensajes de prueba desde CI)
- [ ] Revisar periódicamente los términos del proveedor FormSubmit, las condiciones de tratamiento de datos y la política editorial de privacidad
- [x] La página principal describe áreas de formación sin atribuir títulos oficiales no verificados
- [ ] Complete keyboard/screen reader accessibility audit and independent Lighthouse metrics (basic interaction/contrast checks automated)
- [x] Ilustraciones principales etiquetadas explícitamente como conceptuales; captura auténtica adicional con procedencia y autoría colectiva indicadas
- [x] PNG social 1200x630 añadido al repositorio y metadatos OG/Twitter activados; test valida cabecera y dimensiones
- [x] Capturas de revisión automática con Playwright a cinco anchuras; revisión humana visual adicional opcional
- [x] Sitio antiguo íntegro conservado en docs y disponible como archivo navegable en inglés, con noindex

No employment affiliation with the previously excluded institution may be published.

## Automated checks introduced during PR review
- [x] Five Chromium responsive viewports: 320, 390, 768, 1024, 1440 px, without overflow.
- [x] Native HTML form validation without sending any third-party requests.
- [x] Theme toggle, disclosure interactions and historical deep-link handling.
- [x] Browser screenshots uploaded as short-lived CI artifacts for human visual review.
- [x] Contrast token checks for both themes and safe external-link checks.
- [x] Correct README and archived superseded documentation for traceability.

## Deliberate limitations
- [ ] The selected project visuals remain explicitly labeled *conceptual*. Real screenshots must only come from real deployed/working code.
- [ ] Live FormSubmit delivery and anti-spam behavior cannot be established from mock submissions; provider recommends reCAPTCHA but the existing site intentionally has it disabled, so review the privacy/spam tradeoff before enabling it.
- [ ] A clear licensing decision is required before claiming the portfolio code itself is under an open-source license.

## Refinamientos de accesibilidad y metadatos (18/11/2026)
- [x] Metadatos Twitter Card sin duplicación; Open Graph y JSON-LD conservados.
- [x] Destino de enlace «Saltar al contenido» enfocable por teclado sin añadirlo al orden de tabulación.
- [x] Formulario vinculado mediante `aria-describedby` a su aviso de privacidad.
- [x] Tamaño táctil mínimo de 44 px en controles de navegación y copia.
- [x] Tema de color coherente con controles nativos y soporte de colores forzados.
- [x] Tests estáticos y de navegador para las regresiones anteriores.
- [ ] Auditoría manual con lector de pantalla y dispositivos físicos: los tests no sustituyen WCAG completo.

## Cierre de preservación de identidad
- [x] El contenido exacto del `index.html` anterior a la PR #2 se conserva en `docs/portfolio-v2/LEGACY-INDEX.html`.
- [x] Enlaces externos públicos del original (salvo fuentes Google y favicon sustituido) se conservan.
- [x] Referencias explícitas a FLOSS First, software libre, sostenibilidad, inclusión, privacidad e IA local en el sitio nuevo.
- [x] El archivo original en inglés se ofrece también como `legacy-english.html`, etiquetado como histórico.
