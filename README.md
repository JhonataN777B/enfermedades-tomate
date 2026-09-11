# Proyecto 7 — Diagnóstico visual de enfermedades en hojas de tomate

**Visión por computador · clasificación multiclase · agricultura**

Repositorio reproducible para reconocer seis condiciones foliares del tomate a partir de imágenes. Contiene exploración visual, una línea base clásica basada en HSV y regresión logística, funciones reutilizables y documentación para usar el proyecto sin incorporar el dataset completo a Git.

> Alcance académico/investigativo: no sustituye el diagnóstico agronómico ni debe ser la única base para decidir tratamientos.

## Estructura y responsabilidad

```text
enfermedades-tomate/
├── data/          # procedencia, descarga, contrato de datos y muestras atribuidas
├── notebooks/     # exploración y experimento inicial en Colab
├── src/           # funciones de descarga y extracción de características HSV
├── models/        # registro de artefactos; pesos grandes no se versionan
├── reports/       # fichas, figuras, métricas y evidencia de IA
├── requirements.txt
└── AI_USE_LOG.md
```

Cada carpeta tiene un `README.md` que define qué archivos pertenecen allí y cómo utilizarlos.

## Dataset: procedencia y licencia

Se emplea **Processed Tomato Leaf Disease Image Dataset with Train-Validation-Test Split for Deep Learning Applications**, de Shahriar Ahmed Shovo y Samiha Raisa Mostafa, publicado en [Mendeley Data, DOI: 10.17632/3zwdw6y4pn.1](https://doi.org/10.17632/3zwdw6y4pn.1). Es un dataset depurado derivado de PlantVillage: contiene seis clases, remueve imágenes borrosas/duplicadas y usa divisiones `train`/`val`/`test` 70/15/15. Su licencia es [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

El repositorio no incluye el dataset completo: solo incorpora seis imágenes de referencia, acreditadas, una por clase. Consulta [data/README.md](data/README.md) para la descarga, conteos y atribución.

## Inicio rápido

Requisitos: Python 3.10+, Git y acceso al dataset.

```powershell
git clone https://github.com/JhonataN777B/enfermedades-tomate.git
cd enfermedades-tomate
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m src.data --download --destination data/raw
jupyter notebook notebooks/Proyecto_Profundizacion_3_Enfermedades_en_hojas_de_tomate.ipynb
```

El notebook original fue creado en Google Colab. Para ejecutarlo localmente, configura `base_dir` como `data/raw/Dataset` y omite `from google.colab import drive`. Más detalles en [notebooks/README.md](notebooks/README.md).

## Flujo de trabajo

1. Descargar el dataset y comprobar `train/`, `val/` y `test/`.
2. Ejecutar la exploración y línea base del notebook.
3. Mover lógica reutilizable a `src/`, no duplicarla entre notebooks.
4. Ajustar con `train/`, seleccionar con `val/` y mantener `test/` para la evaluación final.
5. Exportar métricas y figuras reproducibles a `reports/`.
6. Versionar modelos en `models/` solo si su tamaño y licencia lo permiten.

## Dependencias

| Paquete | Uso |
| --- | --- |
| `gdown` | Descarga del ZIP de Google Drive. |
| `opencv-python`, `numpy` | Imágenes, HSV e histogramas. |
| `pandas`, `scikit-learn` | Resúmenes, regresión logística y métricas. |
| `matplotlib`, `seaborn` | EDA y visualizaciones. |
| `scikit-image` | Descriptores LBP del notebook. |
| `jupyter`, `Pillow` | Notebooks y manejo de imágenes. |

Las dependencias se declaran en `requirements.txt`; toda dependencia adicional debe registrarse allí.

## Reproducibilidad, licencia y uso responsable

- No uses `test/` para ajustar o seleccionar modelos.
- Datos locales, ZIP, resultados temporales y pesos pesados están ignorados por Git.
- Registra fuente, versión de datos, semilla, transformaciones y métricas en el notebook o reporte correspondiente.
- Documenta IA generativa en [AI_USE_LOG.md](AI_USE_LOG.md) y adjunta el chat/evidencia en `reports/ai/` si no contiene información sensible.
- CC BY 4.0 aplica al dataset citado, no presupone una licencia para el código. Antes de redistribuir el código, define su licencia explícitamente.
