import joblib
import pandas as pd

# Load trained claim approval model
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
claim_approval = joblib.load(os.path.join(BASE_DIR, "models", "approval_model.pkl"))


def predict_approval(df: pd.DataFrame):
    """
    Input columns:
    age, sex, bmi, children, smoker, region, charges
    """
    prediction = claim_approval.predict(df)
    return int(prediction[0])