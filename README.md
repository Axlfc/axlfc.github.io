# Axlfc — Portafolio personal

Código fuente de [axlfc.github.io](https://axlfc.github.io), el portafolio de Axel Fernández Curros.

El objetivo editorial es mostrar **trabajos verificables** en desarrollo web, software, automatización, infraestructura y tecnología creativa, con una navegación limpia y accesible. Los proyectos de investigación se diferencian de los productos ejecutables.

> **Estado:** el rediseño se encuentra en [Draft PR #2](https://github.com/Axlfc/axlfc.github.io/pull/2), rama `feat/portfolio-v2-editorial`. La rama `master` continúa publicada sin modificaciones hasta autorizar el merge.

## Estructura de la V2

| Archivo | Función |
| --- | --- |
| `index.html` | Contenido y estructura semántica del portafolio |
| `styles.css` | Layout editorial, responsive, colores y foco visible |
| `script.js` | Preferencia de tema, navegación, enlaces históricos y botones de copia |
| `privacidad.html` | Información preliminar sobre datos del formulario |
| `404.html` | Página de error |
| `assets/axlfc-mark.svg` | Favicon |
| `tests/` | Regresiones estáticas y de navegador |
| `.github/workflows/portfolio-ci.yml` | Pruebas de integración en GitHub Actions |
| `docs/portfolio-v2/` | Criterios de liberación y decisiones del rediseño |

No se necesita React, un backend para mostrar la web ni dependencias JavaScript en producción. GitHub Pages construye el repositorio con Jekyll; los estilos y scripts del portafolio son propios.

## Desarrollo y validación

```sh
python -m unittest discover -s tests -v
node --check script.js
bundle exec jekyll build --trace
```

Para ejecutar las pruebas de navegador:

```sh
python -m pip install playwright==1.57.0
python -m playwright install chromium
python tests/browser_smoke.py
```

Los checks del PR prueban contenido original, enlaces de sección y proyectos históricos, sintaxis JavaScript, build Jekyll y comportamiento responsive. El script de navegador **no envía datos al servicio de contacto**.

## Formulario

Se mantiene el proveedor FormSubmit y el destino ya configurado en la web anterior. Incluye campos obligatorios, honeypot y un retorno corregido. La recepción efectiva, el riesgo de spam y la documentación jurídica **requieren validación antes del merge**; no se hacen envíos automáticos como parte de los tests.

## Publicación y decisiones pendientes

La publicación en `master` depende de cerrar [la checklist de liberación](docs/portfolio-v2/RELEASE-CHECKLIST.md). No se realizarán merges automáticos.

Los recursos visuales de proyectos etiquetados como conceptuales **no son capturas de producto**. No publicar contenido privado de terceros ni atribuir a una persona contribuciones sin verificación.

**Licencias:** no presupongas una licencia de reutilización para la totalidad de este repositorio: comprueba las condiciones de cada recurso y la existencia de una licencia explícita antes de redistribuirlo.

## Documentación anterior

El [README histórico](docs/portfolio-v2/README-LEGACY.md) se conserva por trazabilidad; menciona Bootstrap y una rama `main` que no corresponden a la arquitectura actual.
