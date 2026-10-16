# Proyecto 7 — Diagnóstico visual de enfermedades en hojas de tomate

**Visión por computador · clasificación multiclase · agricultura**

Repositorio reproducible para reconocer seis condiciones foliares del tomate a partir de imágenes. Conserva la exploración y línea base HSV + regresión logística de la primera entrega, e incorpora una segunda entrega con augmentation, una CNN propia y transferencia de aprendizaje con MobileNetV2. Incluye funciones reutilizables y documentación para trabajar sin incorporar el dataset completo a Git.

> Alcance académico/investigativo: no sustituye el diagnóstico agronómico ni debe ser la única base para decidir tratamientos.

## Estructura y responsabilidad

```text
enfermedades-tomate/
├── data/          # procedencia, descarga, contrato de datos y muestras atribuidas
├── notebooks/     # primera entrega (EDA/baseline) y segunda (CNN/MobileNetV2)
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
jupyter notebook notebooks/02_comparacion_modelos_cnn.ipynb
```

El notebook original de la primera entrega fue creado en Google Colab. La segunda entrega detecta `data/raw/Dataset` o la ruta histórica `dataset_tomato/Dataset` automáticamente. MobileNetV2 descarga sus pesos ImageNet al ejecutar el modelo. Consulta [notebooks/README.md](notebooks/README.md) para el protocolo y las diferencias entre entregas.

**Windows:** TensorFlow debe ejecutarse en WSL2 o Google Colab; la instalación nativa de Windows no está disponible en las versiones requeridas por esta entrega. En Linux/WSL2 o Colab, instala las dependencias desde `requirements.txt`.

## Flujo de trabajo

1. Descargar el dataset y comprobar `train/`, `val/` y `test/`.
2. Ejecutar la primera entrega para reproducir la exploración y línea base histórica.
3. Ejecutar `02_comparacion_modelos_cnn.ipynb` para entrenar la CNN y MobileNetV2 con augmentation solo en `train/`.
4. Usar `val/` para parada temprana y mantener `test/` reservado para la comparación final.
5. Consultar los resultados históricos y su advertencia de particiones en [reports/second_cut_results.md](reports/second_cut_results.md); reemplazarlos por una nueva ejecución comparable en `test` antes del informe final.
6. Mover lógica reutilizable a `src/` y versionar modelos solo si tamaño y licencia lo permiten.

## Dependencias

| Paquete | Uso |
| --- | --- |
| `gdown` | Descarga del ZIP de Google Drive. |
| `opencv-python`, `numpy` | Imágenes, HSV e histogramas. |
| `pandas`, `scikit-learn` | Resúmenes, regresión logística y métricas. |
| `matplotlib`, `seaborn` | EDA y visualizaciones. |
| `scikit-image` | Descriptores LBP de la primera entrega. |
| `tensorflow` | CNN propia, augmentation y MobileNetV2 en la segunda entrega. |
| `jupyter`, `Pillow` | Notebooks y manejo de imágenes. |

Las dependencias se declaran en `requirements.txt`; toda dependencia adicional debe registrarse allí.

## Reproducibilidad, licencia y uso responsable

- No uses `test/` para ajustar o seleccionar modelos.
- Datos locales, ZIP, resultados temporales y pesos pesados están ignorados por Git.
- Registra fuente, versión de datos, semilla, transformaciones y métricas en el notebook o reporte correspondiente.
- Documenta IA generativa en [AI_USE_LOG.md](AI_USE_LOG.md) y adjunta el chat/evidencia en `reports/ai/` si no contiene información sensible.
- CC BY 4.0 aplica al dataset citado, no presupone una licencia para el código. Antes de redistribuir el código, define su licencia explícitamente.
