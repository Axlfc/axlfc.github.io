# Evidencia editorial — proyectos de Axlfc

*Revisión del 18 de noviembre de 2026. Es una matriz de alcance, no una certificación de funcionalidad ni una medida de competencia personal.*

## Qué puede afirmarse públicamente

| Trabajo | Evidencia pública | Alcance verificable | Qué no debemos afirmar |
| --- | --- | --- | --- |
| [Afaces Web](https://github.com/Axlfc/afaces_web) | Código HTML/CSS/JS, metadatos, tests Node/Python y documentación | Web musical, catálogo, cronología y radio compartida en su implementación | Que todos los navegadores, despliegues y enlaces de reproducción estén auditados o funcionando ahora mismo |
| [connect-core](https://github.com/Axlfc/connect-core) | README de Docker/Podman, perfiles de hardware, n8n y modelos locales | Arquitectura modular y recursos para orquestación/automatización en desarrollo | Software listo para producción: su propio README exige auditoría de seguridad |
| [BrokenLinkCrawler](https://github.com/hypenosys/BrokenLinkCrawler) | CLI, pruebas, manejo de `robots.txt` y documentación de límites | Rastreo acotado de enlaces internos, páginas referidoras e informes | Rastreo exhaustivo de sitios con JavaScript o auditoría sin falsos negativos |
| [RuneScript](https://github.com/Axlfc/RuneScript) | Código y documentación pública, hoja de ruta | Trabajo con Python, scripts e integración experimental de herramientas | Todas las características descritas en la visión/roadmap como terminadas |
| [The Deputation](https://github.com/hypenosys/Deputation) | Inventario de mecánicas, contratos de comportamiento y simulaciones limitadas | Investigación y diseño de un juego retro sujeto a restricciones técnicas | Juego terminado, jugable o validado sobre C64 real |
| [Hypenosys Web](https://github.com/hypenosys/hypenosys.github.io) | Código público Jekyll/JS, documentación y pruebas | Colaboración en interfaces, paneles y herramientas de desarrollo web | Autoría exclusiva de un trabajo colectivo o despliegue sin incidencias |
| [THE MACHINE](https://github.com/hypenosys/the_machine) | Documentación y auditoría del diseño conceptual | Investigación arquitectónica y límites de evidencia | Plataforma Rust implementada o producto en producción |

## Principios de atribución

1. **No convertir actividad en GitHub en una prueba automática de resultados en producción.** Commits y archivos comprueban la existencia de trabajo, no su fiabilidad.
2. **Distinguir autoría propia de colaboración.** Las contribuciones a repositorios de `hypenosys` se atribuyen al equipo cuando corresponda.
3. **Separar prototipo, investigación, software operativo y producto validado.** No se asignan porcentajes de habilidad.
4. **No mostrar imágenes como capturas si son ilustraciones.** Las gráficas actuales de Afaces y connect-core se etiquetan claramente como conceptuales.
5. **No publicar datos de proyectos privados sin autorización expresa.**
6. **No inventar acreditaciones.** Los títulos académicos se describen en términos generales hasta comprobar denominaciones exactas.

## Recursos visuales pendientes de publicación

- Capturas reales de Afaces Web y de una implementación web adicional, con procedencia y derechos de uso revisados.
- Una demostración funcional breve de alguna herramienta Python.
- Imagen social del portafolio (puede generarse localmente mediante `scripts/generate_social_card.py`).

Una imagen conceptual puede ser válida para la composición, pero nunca debe suplir una prueba visual de software real.

## Prueba visual de desarrollo web

- Una captura real de prueba de interfaz se conserva en `assets/hypenosys-ui-test.png`, tomada **sin modificar** de [Hypenosys Web / `runners_ui_test.png`](https://github.com/hypenosys/hypenosys.github.io/blob/master/runners_ui_test.png). Tamaño original: 1280×720.
- La captura muestra un estado de desarrollo de la plataforma colaborativa; **no demuestra un despliegue actual ni autoría individual exclusiva**.
- Se presenta en un desplegable voluntario para mantener aire visual y dar contexto documental a quien desee profundizar.
