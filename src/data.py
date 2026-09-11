"""Utilidades para obtener y localizar el dataset de hojas de tomate."""

from pathlib import Path
from zipfile import ZipFile
import argparse


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


def main() -> None:
    """Expone la descarga del dataset como comando de módulo."""
    parser = argparse.ArgumentParser(
        description="Descarga y valida el dataset de enfermedades en hojas de tomate."
    )
    parser.add_argument(
        "--download",
        action="store_true",
        help="descarga y descomprime el ZIP público de Google Drive",
    )
    parser.add_argument(
        "--destination",
        default="data/raw",
        help="carpeta local de descarga (por defecto: data/raw)",
    )
    args = parser.parse_args()
    if not args.download:
        parser.error("usa --download para obtener el dataset")

    dataset_root = download_dataset(args.destination)
    print(f"Dataset disponible en: {dataset_root}")


if __name__ == "__main__":
    main()
