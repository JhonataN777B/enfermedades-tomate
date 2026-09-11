# Datos

Esta carpeta contiene datos pequeños, archivos de ejemplo y documentación de adquisición. Los conjuntos de imágenes grandes deben descargarse localmente y no versionarse.

## Dataset del proyecto

- Fuente: [Google Drive](https://drive.google.com/file/d/1iR-_h-xHfI5F_m3J98sSu0jXPJtbExVx/view?usp=sharing)
- Identificador de archivo: `1iR-_h-xHfI5F_m3J98sSu0jXPJtbExVx`
- Formato esperado: archivo ZIP con la carpeta `Dataset/` y las particiones `train/`, `val/` y `test/`.
- Descarga: el notebook usa `gdown` para obtener y descomprimir el archivo en Google Colab.

Antes de reutilizar o distribuir los datos, confirmar su licencia y atribución con la fuente original.

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
  Dataset/
```
