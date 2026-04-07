import joblib
import pandas as pd

# Load trained fraud detection model
import os
import joblib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "models", "fraud_model.pkl")

fraud_detection = joblib.load(model_path)


def predict_fraud(df: pd.DataFrame):
    """
    Input columns:
    amount, oldbalanceOrg, newbalanceOrig,
    oldbalanceDest, newbalanceDest,
    orig_diff, dest_diff, orig_zero, dest_unchanged
    """
    prediction = fraud_detection.predict(df)
    return int(prediction[0])