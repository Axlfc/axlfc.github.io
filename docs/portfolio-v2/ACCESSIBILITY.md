# Accesibilidad — alcance y método

La interfaz es HTML semántico con controles nativos (`details`, `summary`, `button`, `form`), enlace de salto al contenido, foco visible, soporte de movimiento reducido, temas claro/oscuro y colores forzados.

## Auditoría reproducible

El workflow ejecuta Playwright Chromium con axe-core 4.10.3 en tres páginas (inicio, privacidad, 404) y dos temas. Se comprueban las reglas etiquetadas WCAG 2.0/2.1 A/AA. Los hallazgos se conservan en `browser-artifacts/axe-report.json` y en el artefacto de Actions. Los impactos `serious` o `critical` bloquean CI.

```sh
python -m pip install playwright==1.57.0
python -m playwright install chromium
npm install --prefix /tmp/axlfc-a11y --no-save --no-package-lock axe-core@4.10.3
python tests/a11y_axe.py
```

## No demostrado

Una ejecución automatizada **no certifica conformidad WCAG**. Siguen pendientes navegación completa por teclado, lector de pantalla, zoom al 200/400%, contraste de todas las ilustraciones y estados interactivos, dispositivos físicos y revisión de lenguaje y contenido. La ausencia de incidencias de axe no debe presentarse como certificación.
