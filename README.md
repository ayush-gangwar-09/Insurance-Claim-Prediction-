# 🚀 Life Insurance Claim Prediction System

An end-to-end Machine Learning project that predicts insurance claim approval by combining fraud detection, risk segmentation, premium prediction, and claim approval models.



## 🔥 Features

* 🛑 Fraud Detection (Rule-based + ML-based)
* 📊 Risk Segmentation using Clustering
* 💰 Premium Prediction
* ✅ Claim Approval Prediction
* 🌐 Full-stack integration (Frontend + Flask API)



## 🧠 Tech Stack

* Frontend: HTML, CSS, JavaScript
* Backend: Python, Flask
* Machine Learning: Scikit-learn
* Deployment: Render




## 📁 Project Structure

```
Insurance_Claim_Prediction/
│
├── Backend/
│   ├── src/
│   │   ├── fraud.py
│   │   ├── risk.py
│   │   ├── premium.py
│   │   ├── approval.py
│   │   ├── pipeline.py
│   │   └── __init__.py
│   │
│   ├── models/
│   │   ├── fraud_model.pkl
│   │   ├── risk_model.pkl
│   │   ├── premium_model.pkl
│   │   ├── approval_model.pkl
│   │   └── scaler.pkl
│   │
│   ├── app.py
│   └── requirements.txt
│
├── Frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── README.md
```




## ⚙️ How It Works

1. User enters customer and transaction details
2. Data is sent to Flask API
3. Pipeline executes:

   * Fraud Check
   * Risk Prediction
   * Premium Calculation
   * Claim Approval
4. Result is returned and displayed on UI




## 🚀 Run Locally

1. Clone repo
   git clone https://github.com/ayush-gangwar-09/Insurance-Claim-Prediction-.git

2. Go to project folder
   cd insurance-claim-prediction

3. Install dependencies
   cd Backend
   pip install -r requirements.txt

4. Run backend
   python app.py

5. Open frontend
   Open index.html in browser



## 🌐 Deployment

* Backend deployed on Render
* Frontend can be deployed on Netlify



## 💡 Key Highlights

* Modular ML architecture (separate models + pipeline)
* Real-world insurance workflow simulation
* Clean UI with modern design
* Scalable and production-ready structure



## 📌 Future Improvements

* Add charts and visualization
* Add authentication system
* Convert frontend to React
* Deploy using Docker and AWS



## 👨‍💻 Author
**Ayush Kumar**

 **⭐ If you like this project, give it a star!**
