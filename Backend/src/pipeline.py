

import pandas as pd

from src.fraud import predict_fraud
from src.risk import predict_risk
from src.premium import predict_premium
from src.approval import predict_approval

# Constants 
PREMIUM_THRESHOLD = 4700
LOW_RISK_CLUSTERS = [0, 1]


def run_pipeline(transaction_data: dict, customer_data: dict):

    # ================= FRAUD CHECK =================
    txn_df = pd.DataFrame([transaction_data])
    fraud = predict_fraud(txn_df)

    # 🔴 RULE-BASED FRAUD
    if (
        transaction_data["amount"] >= 150000
        and transaction_data["type"] in [1, 4]
    ):
        return {
            "status": "Rejected",
            "reason": "Fraudulent Transaction (Rule-Based)"
        }

    # 🔴 ML-BASED FRAUD
    if fraud == 1:
        return {
            "status": "Rejected",
            "reason": "Fraudulent Transaction (ML-Based)"
        }

    # ================= CUSTOMER DATA =================
    cust_df = pd.DataFrame([customer_data])

    # Risk Segmentation
    risk_cluster = predict_risk(
        cust_df[["age", "bmi", "smoker"]]
    )

    # Premium Prediction
    premium = predict_premium(
        cust_df[["age", "sex", "bmi", "children", "smoker", "region"]]
    )

    # ================= BUSINESS RULE =================
    if premium <= PREMIUM_THRESHOLD and risk_cluster in LOW_RISK_CLUSTERS:
        return {
            "fraud": "No Fraud",
            "risk_cluster": risk_cluster,
            "predicted_premium": premium,
            "claim_status": "Approved (Business Rule)"
        }

    # ================= ML APPROVAL =================
    approval_df = cust_df[
        ["age", "sex", "bmi", "children", "smoker", "region"]
    ].copy()

    approval_df["charges"] = premium

    approval = predict_approval(approval_df)

    return {
        "fraud": "No Fraud",
        "risk_cluster": risk_cluster,
        "predicted_premium": premium,
        "claim_status": "Approved" if approval == 1 else "Rejected"
    }