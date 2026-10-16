# Reportes y figuras

Contiene material legible por personas: fichas técnicas, métricas, figuras exportadas, presentaciones y evidencia de IA. No es un directorio para datos ni checkpoints.

```text
reports/
├── baseline_hsv.md
├── second_cut_results.md
├── figures/       # gráficos con procedencia
└── ai/            # chats o evidencia depurada de IA generativa
```

Cada reporte debe indicar objetivo, fuente/versión del dataset, partición evaluada, preprocesamiento, modelo, semilla, métricas y limitaciones. No publiques resultados de validación como resultados de prueba.

`second_cut_results.md` registra los valores que aparecen en el material del segundo corte y advierte que el baseline se midió en validación, mientras que los modelos profundos se midieron en test. No uses sus métricas como una comparación directa entre los tres modelos.
