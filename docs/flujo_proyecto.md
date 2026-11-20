# Flujo del proyecto

![Diagrama visual del flujo del proyecto](flujo_proyecto.svg)

La imagen muestra las etapas, los modelos comparados, el uso separado de `train`, `val` y `test`, y la ruta de despliegue del modelo final. Mermaid se conserva debajo como fuente editable.

```mermaid
flowchart TD
    A[Descargar dataset CC BY 4.0] --> B[Verificar train / val / test]
    B --> C[Exploración visual y balance]
    C --> D[Preprocesamiento BGR a HSV]
    D --> E[Histograma 3D 8x8x8 = 512 características]
    E --> F[Línea base: regresión logística]
    E --> G[MLP simple]
    E --> H[Deep MLP HSV]
    B --> I[CNN y MobileNetV2 comparativas]
    H --> J[Validación y selección]
    J --> K[Test reservado]
    K --> L[Métricas, matriz de confusión y estrés de iluminación]
    H --> M[Modelo Keras y API FastAPI]
    M --> N[Interfaz web de demostración]
```

## Reglas de evaluación

- `train`: ajuste de parámetros y aumento de datos.
- `val`: selección de arquitectura y seguimiento durante el desarrollo.
- `test`: una sola evaluación final, sin ajustar decisiones posteriores.
- El flujo no sustituye la validación agronómica en campo.
