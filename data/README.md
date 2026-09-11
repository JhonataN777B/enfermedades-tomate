# Datos

Esta carpeta contiene datos pequeños, archivos de ejemplo y documentación de adquisición. Los conjuntos de imágenes grandes deben descargarse localmente y no versionarse.

Para cada fuente, documenta:

- URL o referencia de origen y fecha de acceso.
- Licencia y condiciones de uso.
- Clases, número de imágenes y criterios de calidad.
- División de entrenamiento, validación y prueba, evitando fuga de datos entre plantas o capturas relacionadas.

Estructura local sugerida (ignoradas por Git):

```text
data/
  raw/
  interim/
  processed/
```
