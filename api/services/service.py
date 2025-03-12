import pickle
import os
import numpy as np

MODEL_PATH = "models/trained/risk_predictor.pkl"

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("Trained model not found. Train the model first.")
    
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    return model

def predict_risk(patient_data):
    # Ensure this function correctly processes the input
    model = load_model()  # Make sure this function loads the model correctly
    risk_score = model.predict([patient_data])  # Ensure 'patient_data' is correctly formatted
    return risk_score[0]  # Return the first prediction


