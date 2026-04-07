from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from src.pipeline import run_pipeline
app = Flask(__name__)
CORS(app)   


# ---------------- HOME ROUTE ----------------
@app.route("/")
def home():
    return "Life Insurance Claim Prediction API is running"


# ---------------- PREDICTION ROUTE ----------------
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    print("Incoming Data:", data)  


    # basic validation
    if not data:
        return jsonify({"error": "No data received"}), 400

    if "transaction" not in data or "customer" not in data:
        return jsonify({"error": "Invalid input format"}), 400

    try:
        result = run_pipeline(
            transaction_data=data["transaction"],
            customer_data=data["customer"]
        )
        return jsonify(result)

    except Exception as e:
        return jsonify({
            "error": "Prediction failed",
            "details": str(e)
        }), 500


# ---------------- RUN APP (RENDER SAFE) ----------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)