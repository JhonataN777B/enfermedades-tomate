# Modelos

`Tomate_DeepMLP_HSV.keras` es el artefacto de la red final entrenada con histogramas HSV de 512 dimensiones. La API de `app.py` lo carga desde esta carpeta y el archivo está incluido como artefacto versionable del proyecto.

El archivo contiene los pesos entrenados y se distribuye junto con su documentación técnica. El dataset no se incluye; su fuente y licencia están registradas en `data/README.md`.

Esta carpeta almacena artefactos reproducibles y documentados del proyecto.

Junto a cada modelo, incluir metadatos de dataset/versión, partición, semilla, preprocesamiento, clases, métricas, fecha y licencia. Para pesos grandes, guardar un enlace externo y checksum; no subir checkpoints, cachés ni modelos sin procedencia.

La línea base actual se explica en [reports/baseline_hsv.md](../reports/baseline_hsv.md).
