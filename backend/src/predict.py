import joblib
import os
import numpy as np

# Resolve model paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "model", "fake_news_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "model", "vectorizer.pkl")

# Load once when module loads
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)


def predict_news(text):
    """
    Takes article text and returns:
    prediction, confidence
    """

    vector = vectorizer.transform([text])

    pred = model.predict(vector)[0]

    proba = model.predict_proba(vector)[0]

    confidence = round(np.max(proba) * 100, 2)

    if pred == 1:
        result = "REAL NEWS"
    else:
        result = "FAKE NEWS"

    return result, confidence