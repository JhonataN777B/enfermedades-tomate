# Enfermedades en hojas de tomate

Proyecto para explorar, entrenar y evaluar modelos de visión por computador que identifiquen enfermedades en hojas de tomate.

## Estructura

- `data/`: datos pequeños, metadatos y documentación para obtener conjuntos de datos.
- `notebooks/`: exploración, preparación de datos y experimentos reproducibles.
- `src/`: código reutilizable para carga de datos, entrenamiento, evaluación e inferencia.
- `models/`: modelos exportados únicamente si su tamaño y licencia permiten versionarlos.
- `reports/`: fichas técnicas, figuras y presentaciones.

## Puesta en marcha

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Coloca los datos sin procesar en `data/raw/` (no se versionan) y registra su procedencia, licencia y particiones en `data/README.md`.

## Convenciones

- No incluir imágenes masivas, credenciales ni datos personales en el repositorio.
- Mantener las transformaciones y parámetros de experimentos documentados en los notebooks o en `reports/`.
- Registrar el uso de IA generativa en `AI_USE_LOG.md`.
