"""Extracción de características para la línea base clásica."""

from pathlib import Path

import cv2
import numpy as np


IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg"}


def extract_hsv_features(image_path: str | Path, bins: tuple[int, int, int] = (8, 8, 8)) -> np.ndarray | None:
    """Devuelve un histograma HSV 3D normalizado, o ``None`` si no se lee la imagen."""
    image = cv2.imread(str(image_path))
    if image is None:
        return None
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    histogram = cv2.calcHist([hsv], [0, 1, 2], None, bins, [0, 180, 0, 256, 0, 256])
    cv2.normalize(histogram, histogram)
    return histogram.flatten()


def load_split_features(dataset_root: str | Path, split: str) -> tuple[np.ndarray, np.ndarray, list[str]]:
    """Carga histogramas HSV, etiquetas y clases ordenadas de una partición."""
    split_path = Path(dataset_root) / split
    if not split_path.is_dir():
        raise FileNotFoundError(f"No existe la partición: {split_path}")

    classes = sorted(item.name for item in split_path.iterdir() if item.is_dir())
    features: list[np.ndarray] = []
    labels: list[str] = []
    for class_name in classes:
        for image_path in (split_path / class_name).iterdir():
            if image_path.suffix.lower() in IMAGE_SUFFIXES:
                feature = extract_hsv_features(image_path)
                if feature is not None:
                    features.append(feature)
                    labels.append(class_name)

    return np.asarray(features), np.asarray(labels), classes
