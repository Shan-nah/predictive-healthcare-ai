from flask import Flask, jsonify, request
from api.services.service import load_model, predict_risk

app = Flask(__name__)
model = load_model()

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["features"]
    prediction = predict_risk(model, [data])
    return jsonify({"risk_score": prediction})

if __name__ == "__main__":
    app.run(debug=True)
