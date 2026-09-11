# Resumen de ayudas solicitadas a la IA

## Evidencia revisada

- Registro: [uso_ia_hojas_tomate.pdf](uso_ia_hojas_tomate.pdf).
- Formato: PDF de 33 páginas, exportado el 11 de septiembre de 2026.
- Herramienta visible en las capturas: Gemini, con la interfaz indicando `Flash-Lite`.
- Alcance: conversación de apoyo para construir el notebook inicial de clasificación de enfermedades en hojas de tomate.

El PDF está compuesto por capturas de pantalla, por lo que este resumen se elaboró mediante revisión visual de sus páginas. Resume los temas observados, sin presentar las respuestas de la IA como resultados experimentales verificados.

## Ayudas solicitadas

### 1. Preparación y acceso a los datos

- Configurar un entorno de Google Colab para el proyecto.
- Recorrer `train`, `validation`/`val` y `test` para comprobar la estructura y el balance por clase.
- Descargar y descomprimir el dataset desde Google Drive.
- Comparar el montaje de Drive con una descarga directa mediante `gdown` y el identificador del archivo.
- Inspeccionar subcarpetas intermedias para ajustar correctamente `base_dir` a `dataset_tomato/Dataset`.

### 2. Línea base de clasificación

- Definir una línea base clásica con histogramas tridimensionales HSV normalizados (8 x 8 x 8, 512 características).
- Cargar imágenes y etiquetas por carpeta de clase.
- Entrenar una regresión logística con límite de iteraciones y semilla fija.
- Considerar un árbol de decisión como alternativa interpretable, aunque el notebook consolidó la regresión logística.
- Generar reporte de clasificación y matriz de confusión para identificar errores entre clases similares.

### 3. Exploración visual e interpretación metodológica

- Proponer galerías de muestras para examinar lesiones, fondos, iluminación y variación dentro de cada clase.
- Comparar visualmente clases que el clasificador confunde.
- Interpretar las métricas y la matriz de confusión, en especial la separación más clara de hojas sanas y las confusiones entre tizón temprano y tardío.
- Señalar la limitación de generalizar desde imágenes de PlantVillage, con fondos relativamente controlados, a condiciones reales de campo.

### 4. Características y visualizaciones adicionales

- Introducir LBP como análisis exploratorio de textura.
- Explicar por qué no es útil construir un `pairplot` directo de las 512 dimensiones del histograma HSV.
- Diseñar un `pairplot` alternativo con cuatro estadísticas por imagen: media de H, media de S, media de V y desviación estándar de V como contraste.
- Aclarar que cada punto del gráfico representa una imagen y que las clases se codifican por color, no como ejes numéricos.
- Corregir la configuración de Seaborn para añadir título y tamaño al `pairplot`.
- Interpretar curvas de densidad, incluida una distribución bimodal observada para la clase sana y su relación con iluminación, sombras y geometría de la hoja.

## Aportes incorporados al notebook

El notebook conserva código para descarga con `gdown`, exploración de la estructura de datos, resumen de particiones, histograma HSV, regresión logística, matriz de confusión, galerías visuales, LBP y gráficos de características HSV. La implementación final debe revisarse frente al dataset local y las dependencias declaradas en `requirements.txt`.

## Revisión humana necesaria

Antes de usar el material en una entrega o informe, el equipo debe:

1. Ejecutar el notebook y confirmar que rutas, conteos y resultados corresponden al dataset empleado.
2. Distinguir explícitamente validación de prueba final; `test/` no debe intervenir en decisiones de desarrollo.
3. Comprobar las métricas mostradas y no repetir como hechos las interpretaciones de la IA sin evidencia del experimento.
4. Declarar como limitación que el dataset procede de PlantVillage y no representa por sí solo imágenes tomadas en campo.
5. Mantener la atribución y licencia del dataset en toda figura, informe o redistribución de imágenes.
