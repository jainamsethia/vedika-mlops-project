from pathlib import Path

import joblib
import numpy as np

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "house_price_model.joblib"
FEATURES = ["area", "bedrooms", "bathrooms", "age", "distance_to_city"]


def load_model():
    if not MODEL_PATH.exists():
        from app.train import train_model

        train_model()
    return joblib.load(MODEL_PATH)


def predict(features: dict[str, float]) -> float:
    model = load_model()
    values = np.array([[features[name] for name in FEATURES]], dtype=float)
    return float(model.predict(values)[0])
