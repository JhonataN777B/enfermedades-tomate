# Línea base clásica: HSV + regresión logística

## Propósito

La línea base comprueba carga de imágenes, etiquetas y métricas antes de usar redes neuronales y permite comparar modelos posteriores.

## Método implementado

1. Leer imágenes `.jpg`, `.jpeg` o `.png` por clase.
2. Convertir BGR a HSV con OpenCV.
3. Calcular un histograma HSV normalizado de 8 × 8 × 8 bins.
4. Entrenar `LogisticRegression(max_iter=1000, random_state=42, n_jobs=-1)` con `train/`.
5. Generar reporte de clasificación y matriz de confusión en `val/` para exploración.

`src/features.py` contiene las funciones de carga y extracción HSV. El notebook también incorpora galerías, análisis de fondos/iluminación y LBP como descriptor exploratorio de textura.

| Etapa | Partición permitida |
| --- | --- |
| Ajuste | `train/` |
| Selección de enfoque/hiperparámetros | `val/` |
| Informe final único | `test/` |

El notebook entrega métricas de validación. Para el informe final, fijar el modelo antes de cargar `test/` y guardar métricas, matriz de confusión, fecha, dependencias y versión de datos.
