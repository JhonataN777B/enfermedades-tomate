"""Utilidades para obtener y localizar el dataset de hojas de tomate."""

from pathlib import Path
from zipfile import ZipFile


DATASET_FILE_ID = "1iR-_h-xHfI5F_m3J98sSu0jXPJtbExVx"
SPLITS = ("train", "val", "test")


def download_dataset(destination: str | Path = "data/raw") -> Path:
    """Descarga y descomprime el ZIP público de Google Drive.

    Devuelve la ruta a la carpeta `Dataset`. Requiere ``gdown``.
    """
    import gdown

    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=True)
    archive = destination / "dataset_tomato.zip"
    gdown.download(id=DATASET_FILE_ID, output=str(archive), quiet=False)

    with ZipFile(archive) as zipped_data:
        zipped_data.extractall(destination)

    return find_dataset_root(destination)


def find_dataset_root(path: str | Path) -> Path:
    """Localiza una carpeta Dataset que contenga train, val y test."""
    path = Path(path)
    candidates = (path, path / "Dataset", path / "dataset_tomato" / "Dataset")
    for candidate in candidates:
        if candidate.is_dir() and all((candidate / split).is_dir() for split in SPLITS):
            return candidate
    raise FileNotFoundError(
        f"No se encontró Dataset con las particiones {SPLITS} bajo: {path}"
    )
