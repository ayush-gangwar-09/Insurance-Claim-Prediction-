import os
import joblib
import pandas as pd

# Load trained model and scaler
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
kmeans = joblib.load(os.path.join(BASE_DIR, "models", "risk_model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "models", "scaler.pkl"))

# EXACT feature order used during training
RISK_FEATURES = ["age", "bmi", "smoker"]


def predict_risk(df: pd.DataFrame):
    """
    Input columns:
    age, bmi, smoker
    """

    # 1️⃣ Enforce column order
    df_ordered = df[RISK_FEATURES]

    # 2️⃣ DROP FEATURE NAMES 
    X = df_ordered.to_numpy()

    # 3️⃣ Scale + Predict
    X_scaled = scaler.transform(X)
    cluster = kmeans.predict(X_scaled)

    return int(cluster[0])
