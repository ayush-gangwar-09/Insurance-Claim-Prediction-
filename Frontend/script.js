// ---------------- RISK BADGE ----------------
function getRiskBadge(risk) {
    if (risk === 0) return '<span class="badge low">Low Risk 🟢</span>';
    if (risk === 1) return '<span class="badge medium">Medium Risk 🟡</span>';
    if (risk === 2) return '<span class="badge high">High Risk 🔴</span>';
    return '<span class="badge">Unknown</span>';
}


// ---------------- MAIN PREDICT FUNCTION ----------------
function predict() {

    const resultDiv = document.getElementById("result");

    // Loading state
    resultDiv.innerHTML = '<div class="loading">Predicting...</div>';

    // Get values
    const amount = Number(document.getElementById("amount").value);
    const age = Number(document.getElementById("age").value);
    const bmi = Number(document.getElementById("bmi").value);

    // Basic validation
    if (!amount || !age || !bmi) {
        resultDiv.innerHTML = "⚠️ Please fill all required fields";
        return;
    }

    // Build request data
    const data = {
        transaction: {
            step: 1,
            type: Number(document.getElementById("type").value),
            amount: amount,

            oldbalanceOrg: 100000,
            newbalanceOrig: 100000 - amount,

            oldbalanceDest: 50000,
            newbalanceDest: 50000 + amount,

            orig_diff: amount,
            dest_diff: amount,

            orig_zero: 0,
            dest_unchanged: 0
        },

        customer: {
            age: age,
            sex: Number(document.getElementById("sex").value),
            bmi: bmi,
            children: Number(document.getElementById("children").value),
            smoker: Number(document.getElementById("smoker").value),
            region: Number(document.getElementById("region").value)
        }
    };

    // API call
    fetch("https://insurance-claim-prediction-1qvx.onrender.com/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(result => {

        console.log("API Response:", result); // debug

        // Handle backend error
        if (result.error) {
            resultDiv.innerHTML = `⚠️ ${result.error}`;
            return;
        }

        // Safe extraction
        const risk = result.risk ?? result.risk_cluster ?? -1;
        const claim = result.claim_status ?? result.claim ?? "Unknown";
        const premium = result.predicted_premium ?? result.premium ?? "N/A";
        const fraud = result.fraud ?? "N/A";

        // Render result
        resultDiv.innerHTML = `
            <p><b>Fraud:</b> ${fraud}</p>
            <p><b>Risk:</b> ${getRiskBadge(risk)}</p>
            <p><b>Premium:</b> ₹${premium}</p>
            <p><b>Claim:</b> 
                <span class="${claim.includes("Approved") ? "approved" : "rejected"}">
                    ${claim}
                </span>
            </p>
        `;
    })
    .catch((err) => {
        console.error(err);
        resultDiv.innerHTML = "⚠️ Server Error";
    });
}                                                                                                                                                                                       