# Bitácora de uso de IA generativa

La evidencia exportada o depurada se guarda en `reports/ai/`. No incluir credenciales, información personal ni datos restringidos.

| Fecha | Herramienta/modelo | Finalidad | Archivos afectados | Evidencia o enlace | Revisión humana |
| --- | --- | --- | --- | --- | --- |
| 2026-09-11 | Gemini (interfaz mostrada: Flash-Lite) | Apoyo para configurar, depurar, explorar e interpretar la línea base de visión por computador. | Notebook inicial y sus decisiones metodológicas. | [PDF del diálogo](reports/ai/uso_ia_hojas_tomate.pdf) y [resumen](reports/ai/resumen_uso_ia.md) | **Completada:** se revisaron detalladamente los códigos, rutas, ejecución y resultados; el flujo funcionó correctamente. |
| 2026-10-16 | OpenAI Codex | Integrar el segundo avance en una libreta reproducible, transcribir los resultados entregados, señalar la diferencia entre validación y test y corregir el preprocesamiento de MobileNetV2. | `notebooks/02_comparacion_modelos_cnn.ipynb`, `reports/second_cut_results.md` y documentación. | Conversación de trabajo en Codex; resultados fuente en la presentación y libreta de `../2° avance/`. | **Revisión de contenido completada:** cifras cotejadas entre benchmark, reportes por clase y particiones del notebook fuente. **Pendiente de reproducibilidad:** ejecutar en esta rama para obtener la comparación corregida de los tres modelos en test. |
