# Enfermedades en hojas de tomate

Proyecto de visión por computador para clasificar seis condiciones foliares del tomate mediante descriptores HSV y redes neuronales. Reúne los avances 1 y 2 y la actualización final con el **Deep MLP HSV**, el modelo Keras y una demo web.

> Uso académico y de investigación. Las predicciones son orientativas y no sustituyen el diagnóstico de un ingeniero agrónomo.

## Resultado final

El modelo recibe un histograma 3D HSV normalizado de 512 características y clasifica `Bacterial_spot`, `Early_blight`, `Late_blight`, `Leaf_Mold`, `Septoria_leaf_spot` y `Healthy`.

| Modelo | Partición | Accuracy | F1 macro |
| --- | --- | ---: | ---: |
| Regresión logística HSV | Validación | 90,62% | 90,46% |
| MLP simple HSV | Validación | 97,75% | 97,75% |
| **Deep MLP HSV** | **Test reservado** | **97,37%** | **97,36%** |

Consulta el detalle, los riesgos y la prueba de iluminación en [`MODEL_CARD.md`](MODEL_CARD.md).

## Estructura

```text
├── app.py                         # API FastAPI para inferencia
├── index.html                     # Demo web
├── requirements.txt               # Dependencias
├── MODEL_CARD.md                  # Ficha técnica final
├── AI_USE_LOG.md                  # Bitácora consolidada de IA
├── data/                          # Contrato, atribución y referencias
├── models/                        # Modelo Keras y documentación
├── notebooks/                     # Avances 1, 2 y notebook final
├── reports/                       # Resultados, figuras y evidencia IA
├── docs/flujo_proyecto.md         # Diagrama y reglas de evaluación
└── src/                           # Descarga y extracción HSV
```

## Dataset

Se utiliza [Processed Tomato Leaf Disease Image Dataset](https://doi.org/10.17632/3zwdw6y4pn.1), derivado de PlantVillage y publicado por Mendeley Data bajo [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). El dataset completo no se versiona; las instrucciones están en [`data/README.md`](data/README.md).

## Instalación y ejecución

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m src.data --download --destination data/raw
jupyter notebook notebooks/Proyecto_Profundizacion_3_Enfermedades_en_hojas_de_tomate_final.ipynb
```

Para la demo web, desde la raíz:

```powershell
uvicorn app:app --reload
```

La API carga `models/Tomate_DeepMLP_HSV.keras`. Para notebooks en Windows, usa WSL2 o Google Colab si TensorFlow no es compatible con la instalación nativa.

## Flujo metodológico

1. Descargar y validar `train`, `val` y `test`.
2. Explorar balance, imágenes, iluminación y textura.
3. Convertir BGR a HSV y extraer 512 bins normalizados.
4. Comparar regresión logística, MLP, CNN y MobileNetV2.
5. Seleccionar con `val` y evaluar una sola vez sobre `test`.
6. Documentar métricas, errores, estrés de iluminación y límites de uso.

El diagrama completo está en [`docs/flujo_proyecto.md`](docs/flujo_proyecto.md).

## Documentación final

- [`MODEL_CARD.md`](MODEL_CARD.md) y [versión visual](reports/figures/Model_Card_Tomate_DeepMLP_HSV.png).
- [`AI_USE_LOG.md`](AI_USE_LOG.md) y [`reports/ai/resumen_uso_ia.md`](reports/ai/resumen_uso_ia.md).
- [`reports/second_cut_results.md`](reports/second_cut_results.md): resultados históricos y advertencia de comparabilidad.
- [`notebooks/README.md`](notebooks/README.md): protocolo de reproducción.

## Reproducibilidad y responsabilidad

- No usar `test` para ajustar hiperparámetros.
- Registrar semilla, versión de datos, transformaciones y dependencias.
- No versionar dataset, entornos virtuales, cachés ni resultados temporales.
- Atribuir el dataset en informes y redistribuciones.
- No usar el sistema para prescribir tratamientos agrícolas.
