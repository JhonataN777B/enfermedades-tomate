# Notebooks

Los notebooks sirven para exploración, visualización y narrativa experimental. Toda función estable o reutilizable debe extraerse a `src/`.

| Archivo | Finalidad | Datos requeridos | Productos |
| --- | --- | --- | --- |
| `Proyecto_Profundizacion_3_Enfermedades_en_hojas_de_tomate.ipynb` | Conteos, EDA, HSV, LBP y línea base de regresión logística. | `Dataset/train`, `Dataset/val`, `Dataset/test`. | Gráficas, galerías, reporte de clasificación y matriz de confusión. |

## Ejecución

**Google Colab:** ejecutar las celdas en orden. El notebook descarga el ZIP con `gdown`; la importación `google.colab` no participa en esa descarga y puede omitirse.

**Local:** instalar dependencias, ejecutar `python -m src.data --download --destination data/raw`, abrir Jupyter desde la raíz y cambiar `base_dir` por `data/raw/Dataset`. Comentar la importación exclusiva de Colab.

La línea base ajusta con `train/` y evalúa de forma exploratoria en `val/`. Esas métricas no son resultado final: `test/` se reserva hasta fijar el modelo.

## Convenciones

- Nuevos notebooks: prefijo numérico, por ejemplo `02_modelo_cnn.ipynb`.
- Primera celda: objetivo, fecha, versión del dataset, semilla y dependencias no estándar.
- Exportar resultados finales a `reports/figures/`.
- No usar rutas absolutas, secretos ni descargas no documentadas.
