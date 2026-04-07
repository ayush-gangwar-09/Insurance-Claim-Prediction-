import joblib
import pandas as pd

# Load trained premium prediction model
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
premium_prediction = joblib.load(
    os.path.join(BASE_DIR, "models", "premium_model.pkl")
)


def predict_premium(df: pd.DataFrame):
    """
    Input columns:
    age, sex, bmi, children, smoker, region
    """
    prediction = premium_prediction.predict(df)
    return float(prediction[0])