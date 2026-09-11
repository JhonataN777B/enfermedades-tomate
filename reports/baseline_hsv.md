# Línea base: HSV + regresión logística

El notebook inicial implementa una referencia clásica para clasificación multiclase:

1. Convierte cada imagen a HSV.
2. Calcula un histograma tridimensional normalizado de 8 × 8 × 8 bins.
3. Entrena una regresión logística sobre `train/`.
4. Reporta métricas y una matriz de confusión durante la exploración.

Para resultados comparables, conserva `test/` para la evaluación final. La sección exploratoria actual del notebook carga `val/` como conjunto de evaluación; no debe presentarse como resultado final de prueba.

Las figuras generadas deben exportarse a esta carpeta con un nombre descriptivo y anotarse con fecha, versión del notebook y versión del dataset.
