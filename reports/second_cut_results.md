# Resultados del segundo corte

## Protocolo documentado

La presentación del segundo corte y las salidas del notebook original reportan tres modelos: histograma HSV + regresión logística, CNN pequeña con augmentation y MobileNetV2 con transferencia de aprendizaje. La CNN y MobileNetV2 usan imágenes de 128 × 128 píxeles y se evalúan sobre 990 imágenes de `test`.

**Advertencia de comparabilidad:** el baseline HSV usa 981 imágenes de `val`, según el notebook original. Por tanto, la tabla del benchmark mezcla particiones y no permite concluir con rigor cuál de los tres modelos generaliza mejor en el mismo conjunto. CNN y MobileNetV2 sí comparten la partición `test`, y esa comparación es directa. El notebook `02_comparacion_modelos_cnn.ipynb` ajusta el protocolo para evaluar los tres modelos en `test` en una ejecución reproducible; esos resultados nuevos deben reemplazar la comparación histórica cuando se ejecute.

## Métricas reportadas

| Modelo | Partición | n | Accuracy | Precision macro | Recall macro | F1 macro |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| HSV + regresión logística | Validación | 981 | 0.906218 | 0.905382 | 0.906074 | 0.904660 |
| CNN pequeña + augmentation | Test | 990 | 0.943434 | 0.946009 | 0.943316 | 0.942456 |
| MobileNetV2 | Test | 990 | 0.884848 | 0.887306 | 0.884613 | 0.883918 |

Entre los dos modelos evaluados sobre el mismo `test`, la CNN supera a MobileNetV2 por **5.86 puntos porcentuales** en accuracy y **0.0585** en macro F1. En la CNN, el recall más bajo corresponde a Leaf Mold (0.80; 131 de 164 correctas), principalmente confundida con Septoria (19 casos). En MobileNetV2, Early blight tiene el recall más bajo (0.73; 119 de 164 correctas). Estos errores orientan la siguiente revisión del modelo.

## Resultados por clase

Los valores de la tabla siguiente provienen de los reportes de clasificación redondeados a dos decimales que se muestran en la presentación. El baseline es de validación; los otros dos reportes son de test.

| Clase | Baseline F1 (val) | CNN F1 (test) | MobileNetV2 F1 (test) |
| --- | ---: | ---: | ---: |
| Bacterial spot | 0.95 | 0.98 | 0.91 |
| Early blight | 0.86 | 0.94 | 0.79 |
| Late blight | 0.81 | 0.96 | 0.86 |
| Leaf Mold | 0.93 | 0.88 | 0.91 |
| Septoria leaf spot | 0.91 | 0.91 | 0.86 |
| Healthy | 0.96 | 0.98 | 0.97 |

## Interpretación y alcance

- La CNN pequeña es el mejor modelo **entre los dos evaluados en el mismo test** y queda como modelo provisional del segundo corte.
- El baseline de validación proporciona una referencia histórica, pero debe evaluarse de nuevo en test antes de compararlo con redes neuronales.
- La libreta de origen configura `rescale=1/255` también para MobileNetV2. MobileNetV2 con pesos ImageNet requiere su preprocesamiento (`preprocess_input`); el notebook actualizado lo corrige. Por esto, las métricas históricas de MobileNetV2 no se reproducen necesariamente al ejecutar la versión corregida.
- La libreta de origen no implementa parada temprana; la duración indicada fue hasta 35 épocas. Los resultados dependen del hardware, las versiones y la inicialización, y la presentación no registra semilla ni versiones completas.
- El dataset deriva de PlantVillage y contiene imágenes controladas. El resultado no demuestra desempeño en fotografías de campo ni reemplaza el diagnóstico agronómico.

## Fuente

Presentación del segundo corte y notebook original suministrados en `../2° avance/` (diapositivas 21, 23–27 y salidas de las celdas de benchmark). Los valores se transcribieron de sus tablas y reportes; no son una nueva ejecución de esta rama.
