# Axlfc — Portafolio personal

Código fuente de [axlfc.github.io](https://axlfc.github.io), el portafolio de Axel Fernández Curros.

El objetivo editorial es mostrar **trabajos verificables** en desarrollo web, software, automatización, infraestructura y tecnología creativa, con una navegación limpia y accesible. Los proyectos de investigación se diferencian de los productos ejecutables.

> **Origen del rediseño:** [PR #2](https://github.com/Axlfc/axlfc.github.io/pull/2). Publicación sujeta a CI y verificaciones de producción.

## Estructura de la V2

| Archivo | Función |
| --- | --- |
| `index.html` | Contenido y estructura semántica del portafolio |
| `styles.css` | Layout editorial, responsive, colores y foco visible |
| `script.js` | Preferencia de tema, navegación, enlaces históricos y botones de copia |
| `privacidad.html` | Información de privacidad y proveedor externo de contacto |
| `404.html` | Página de error |
| `assets/axlfc-mark.svg` | Favicon |
| `assets/axlfc-social.png` | Imagen social PNG 1200×630, generada a partir de la identidad editorial |
| `scripts/generate_social_card.py` | Generador reproducible de esa tarjeta social (requiere Pillow) |
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

Para recrear la imagen social tras modificar la identidad gráfica:
```sh
python -m pip install pillow==11.3.0
python scripts/generate_social_card.py
```

## Formulario

Se mantiene el proveedor FormSubmit y el destino ya configurado en la web anterior. Incluye campos obligatorios, honeypot y un retorno corregido. Las pruebas no envían mensajes reales. La recepción en la bandeja de correo y el tratamiento operativo del servicio externo deben verificarse por el titular.

## Publicación y decisiones pendientes

La [checklist de mantenimiento y publicación](docs/portfolio-v2/RELEASE-CHECKLIST.md) documenta qué se verificó automáticamente y qué requiere revisión humana. Para futuras versiones, revisa CI antes de fusionar.

Los recursos visuales de proyectos etiquetados como conceptuales **no son capturas de producto**. No publicar contenido privado de terceros ni atribuir a una persona contribuciones sin verificación.

**Licencias:** no presupongas una licencia de reutilización para la totalidad de este repositorio: comprueba las condiciones de cada recurso y la existencia de una licencia explícita antes de redistribuirlo.

## Documentación anterior

El [README histórico](docs/portfolio-v2/README-LEGACY.md) se conserva por trazabilidad; menciona Bootstrap y una rama `main` que no corresponden a la arquitectura actual.

## Conservación íntegra del portafolio anterior

La versión original de `master`, tal como existía antes de la PR #2, se ha conservado **sin modificaciones** en [docs/portfolio-v2/LEGACY-INDEX.html](docs/portfolio-v2/LEGACY-INDEX.html). También se ofrece una [versión navegable del archivo en inglés](https://axlfc.github.io/legacy-english.html), identificada como histórica y excluida de indexación. El README previo permanece en `docs/portfolio-v2/README-LEGACY.md` y se conserva todo el historial Git.

Las menciones del archivo a métricas, títulos o productos son declaraciones **históricas del portafolio anterior**, no validaciones nuevas.
