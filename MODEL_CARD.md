# Model Card: Tomate Deep MLP (HSV Descriptor)

## 1. Detalles del modelo

- **Nombre:** Tomate Deep MLP (HSV Descriptor)
- **Equipo:** David Garzón, Jhonatan Molina y Kevin Comba
- **Fecha:** noviembre de 2026
- **Tipo:** red neuronal totalmente conectada (Deep MLP) para clasificación multiclase a partir de histogramas HSV.
- **Licencia de referencia:** CC BY 4.0 para el dataset; uso académico y de investigación.

### Arquitectura

El modelo recibe 512 características de un histograma 3D HSV normalizado y usa:

1. `Dense(512)` + Batch Normalization + Dropout `0.4` + ReLU.
2. `Dense(256)` + Batch Normalization + Dropout `0.3` + ReLU.
3. `Dense(128)` + Batch Normalization + Dropout `0.3` + ReLU.
4. `Dense(6)` + Softmax.

Como complemento interpretativo se exploró MobileNetV2 con Grad-CAM sobre `out_relu`; no forma parte de la entrada del MLP.

## 2. Uso previsto y restricciones

El modelo es una herramienta académica de cribado inicial para seis clases: mancha bacteriana, tizón temprano, tizón tardío, moho foliar, septoria y hoja sana. Está pensado para estudiantes, investigadores y pruebas de concepto con iluminación controlada.

No es un diagnóstico agronómico. No debe usarse para prescribir fungicidas, bactericidas o erradicar plantas sin validación de un ingeniero agrónomo y análisis fitopatológico de campo.

## 3. Datos y preprocesamiento

El dataset es *Processed Tomato Leaf Disease Dataset*, derivado de PlantVillage y publicado en [Mendeley Data](https://doi.org/10.17632/3zwdw6y4pn.1), bajo CC BY 4.0. Contiene 6.557 imágenes distribuidas aproximadamente en `train` (70%), `val` (15%) y `test` (15%): 4.586, 981 y 990 imágenes, respectivamente.

Cada imagen se convierte de BGR a HSV y se resume con un histograma 3D de `8 × 8 × 8 = 512` bins. El aumento de datos se aplica únicamente durante el entrenamiento de las redes convolucionales comparativas.

## 4. Métricas y benchmark

| Modelo | Partición | Accuracy | F1 macro |
| --- | --- | ---: | ---: |
| Regresión logística HSV | Validación | 90,62% | 90,46% |
| MLP simple HSV | Validación | 97,75% | 97,75% |
| **Deep MLP HSV** | Validación | **97,25%** | **97,25%** |
| **Deep MLP HSV** | Test reservado | **97,37%** | **97,36%** |

Las cifras corresponden al notebook final y deben interpretarse junto con la partición indicada. El test se mantuvo reservado para la evaluación final.

En el test, la clase sana mostró separación perfecta en el reporte final. La principal dificultad aparece entre tizón temprano y tizón tardío, porque el histograma global conserva color pero pierde la distribución espacial de las lesiones.

## 5. Robustez, limitaciones y riesgos

La prueba de estrés sobre el canal V de HSV evidenció alta sensibilidad a la iluminación: el accuracy cayó a **13,66%** con factor `0,4×` y a **44,24%** con `1,4×`, frente a **97,25%** en la condición de referencia.

Limitaciones principales:

- sesgo hacia imágenes controladas de PlantVillage;
- ausencia de información espacial y de forma;
- degradación fuerte bajo sombras o sobreexposición;
- riesgo de falsos negativos en enfermedades de propagación rápida.

## 6. Trabajo futuro

- Combinar HSV con LBP o GLCM.
- Incorporar variaciones de brillo y contraste o usar CIELAB.
- Validar con imágenes de invernadero y campo abierto.
- Reportar intervalos de confianza y calibración antes de cualquier uso operativo.

La versión visual está disponible en [`reports/figures/Model_Card_Tomate_DeepMLP_HSV.png`](reports/figures/Model_Card_Tomate_DeepMLP_HSV.png).
