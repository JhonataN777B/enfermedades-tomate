# Datos

Esta carpeta establece el contrato de datos. El dataset completo se descarga localmente y está excluido de Git; solo `reference_images/` conserva seis muestras pequeñas para documentación.

## Fuente, atribución y licencia

- **Nombre:** *Processed Tomato Leaf Disease Image Dataset with Train-Validation-Test Split for Deep Learning Applications*.
- **Autores:** Shahriar Ahmed Shovo y Samiha Raisa Mostafa.
- **Fuente oficial:** [Mendeley Data](https://data.mendeley.com/datasets/3zwdw6y4pn/1) · [DOI 10.17632/3zwdw6y4pn.1](https://doi.org/10.17632/3zwdw6y4pn.1).
- **Origen:** versión procesada, depurada y organizada derivada de PlantVillage.
- **Licencia:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

La publicación declara eliminación de imágenes borrosas y duplicadas, selección de seis clases y partición 70/15/15. Al distribuir imágenes, resultados o subconjuntos, conserva autores, DOI y licencia.

## Descarga y ubicación local

Prioriza la fuente oficial. El [enlace de Google Drive](https://drive.google.com/file/d/1iR-_h-xHfI5F_m3J98sSu0jXPJtbExVx/view?usp=sharing) (ID `1iR-_h-xHfI5F_m3J98sSu0jXPJtbExVx`) es el acceso usado por el notebook; la atribución y licencia proceden de Mendeley.

Desde la raíz del proyecto:

```powershell
python -m src.data --download --destination data/raw
```

No ejecutes `git add data/raw`; es una ruta ignorada. La estructura esperada es:

```text
data/
├── raw/                         # descarga local, ignorada
│   └── Dataset/
│       ├── train/
│       ├── val/
│       └── test/
└── reference_images/            # muestras atribuidas y versionadas
```

## Clases y conteos verificados

| Etiqueta | Nombre legible | Train | Validación | Test | Total |
| --- | --- | ---: | ---: | ---: | ---: |
| `Tomato___Bacterial_spot` | Mancha bacteriana | 768 | 164 | 166 | 1.098 |
| `Tomato___Early_blight` | Tizón temprano | 762 | 163 | 164 | 1.089 |
| `Tomato___Late_blight` | Tizón tardío | 763 | 163 | 165 | 1.091 |
| `Tomato___Leaf_Mold` | Moho de la hoja | 760 | 163 | 164 | 1.087 |
| `Tomato___Septoria_leaf_spot` | Mancha foliar por Septoria | 768 | 164 | 166 | 1.098 |
| `Tomato___healthy` | Hoja sana | 765 | 164 | 165 | 1.094 |
| **Total** |  | **4.586** | **981** | **990** | **6.557** |

Los conteos se verificaron contra la copia local del proyecto. No mezcles las particiones sin documentar el cambio.

## Muestras de referencia y reglas

`reference_images/` contiene una imagen de `val/` por clase, sin uso en entrenamiento ni evaluación. La atribución de cada archivo está en [reference_images/README.md](reference_images/README.md).

- No subas el dataset completo, ZIP, datos privados ni derivados masivos.
- Conserva las particiones independientes.
- Documenta nuevas fuentes con URL/DOI, licencia, fecha, transformación y conteos.
- Guarda derivados regenerables en `data/interim/` o `data/processed/` (ignorados) y explica cómo crearlos.
