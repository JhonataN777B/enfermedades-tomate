# Enfermedades en hojas de tomate

Proyecto para explorar, entrenar y evaluar modelos de visión por computador que identifiquen enfermedades en hojas de tomate.

El trabajo inicial está documentado en el notebook `notebooks/Proyecto_Profundizacion_3_Enfermedades_en_hojas_de_tomate.ipynb`. Incluye exploración de datos, análisis visual y una línea base con características HSV y regresión logística.

## Estructura

- `data/`: datos pequeños, metadatos y documentación para obtener conjuntos de datos.
- `notebooks/`: exploración, preparación de datos y experimentos reproducibles.
- `src/`: código reutilizable para descargar datos, extraer características e inferencia.
- `models/`: modelos exportados únicamente si su tamaño y licencia permiten versionarlos.
- `reports/`: fichas técnicas, figuras y presentaciones.

## Puesta en marcha

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

El dataset no se incluye en Git. Consulta [las instrucciones de descarga](data/README.md) y registra cualquier versión adicional que se use.

## Dataset y particiones

El dataset está disponible en [Google Drive](https://drive.google.com/file/d/1iR-_h-xHfI5F_m3J98sSu0jXPJtbExVx/view?usp=sharing). Al descomprimirlo, se espera esta estructura:

```text
Dataset/
  train/
  val/
  test/
```

Las clases observadas en el notebook son: `Tomato___Bacterial_spot`, `Tomato___Early_blight`, `Tomato___Late_blight`, `Tomato___Leaf_Mold`, `Tomato___Septoria_leaf_spot` y `Tomato___healthy`.

## Convenciones

- No incluir imágenes masivas, credenciales ni datos personales en el repositorio.
- Mantener las transformaciones y parámetros de experimentos documentados en los notebooks o en `reports/`.
- Guardar la evidencia de uso de IA generativa en `AI_USE_LOG.md` o como un documento enlazado desde allí.
