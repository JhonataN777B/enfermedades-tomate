# Notebooks

Los notebooks sirven para exploración, visualización y narrativa experimental. Toda función estable o reutilizable debe extraerse a `src/`.

| Archivo | Finalidad | Datos requeridos | Productos |
| --- | --- | --- | --- |
| `Proyecto_Profundizacion_3_Enfermedades_en_hojas_de_tomate.ipynb` | Primera entrega: conteos, EDA, HSV, LBP y regresión logística exploratoria. | `Dataset/train`, `Dataset/val`, `Dataset/test`. | Galerías, gráficas y baseline inicial. |
| `02_comparacion_modelos_cnn.ipynb` | Segunda entrega: baseline HSV, CNN propia con augmentation y MobileNetV2 congelada; comparación final en test. | `Dataset/train`, `Dataset/val`, `Dataset/test`. | Tabla de métricas, reportes históricos del segundo corte, reportes por clase y matrices de confusión. |

## Ejecución

Desde la raíz del repositorio:

```powershell
python -m pip install -r requirements.txt
python -m src.data --download --destination data/raw
jupyter notebook notebooks/02_comparacion_modelos_cnn.ipynb
```

El segundo notebook localiza `data/raw/Dataset` o `dataset_tomato/Dataset` (la ruta histórica de Colab). También puede ejecutarse en Colab si se descarga el dataset a esa última ruta. TensorFlow descarga los pesos ImageNet de MobileNetV2 al inicializar el modelo.

## Protocolo experimental

- Ajustar pesos con `train`; usar `val` para parada temprana y selección.
- Mantener `test` sin augmentation y reservarlo para una evaluación final después del entrenamiento.
- MobileNetV2 requiere su función `preprocess_input`; la CNN pequeña usa escala `[0, 1]`.
- Registrar fecha, semilla, versiones, hardware, resultados y limitaciones en `reports/`.
- Las métricas históricas de la primera entrega son exploratorias; no son directamente comparables con el test del segundo notebook.
- Los resultados compartidos para el segundo corte y la advertencia de que baseline usa `val` mientras las redes usan `test` están documentados en [reports/second_cut_results.md](../reports/second_cut_results.md).

## Convenciones

- Nuevos notebooks: prefijo numérico, por ejemplo `02_modelo_cnn.ipynb`.
- Primera celda: objetivo, procedencia de datos, protocolo y dependencias.
- Exportar resultados finales a `reports/figures/`.
- No usar rutas absolutas, secretos ni descargas no documentadas.
