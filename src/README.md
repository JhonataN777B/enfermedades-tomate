# Código reutilizable

Los módulos de esta carpeta deben importarse desde la raíz del repositorio y no depender de un notebook.

| Módulo | Responsabilidad | Uso |
| --- | --- | --- |
| `data.py` | Descarga el ZIP público y localiza una estructura válida. | `python -m src.data --download --destination data/raw` |
| `features.py` | Extrae histogramas HSV y carga una partición como matrices. | Línea base y experimentos. |

`find_dataset_root(path)` exige `train/`, `val/` y `test/`. `extract_hsv_features(path)` devuelve 512 características normalizadas (8×8×8) o `None` para una imagen ilegible. `load_split_features(root, split)` devuelve `(X, y, classes)` con clases ordenadas.

Agregar pruebas a cualquier comportamiento nuevo y mantener separados descarga, entrenamiento y visualización.
