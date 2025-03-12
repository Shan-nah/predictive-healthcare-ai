import streamlit as st
import requests

st.title("Predictive Healthcare AI")

age = st.number_input("Age", min_value=0, max_value=120, value=30)
gender = st.radio("Gender", ["Male", "Female"])
bp = st.number_input("Blood Pressure", min_value=50, max_value=200, value=120)
cholesterol = st.number_input("Cholesterol", min_value=100, max_value=300, value=200)

if st.button("Predict Risk"):
    input_data = [age, 1 if gender == "Male" else 0, bp, cholesterol]
    response = requests.post("http://127.0.0.1:8000/predict", json={"features": input_data})
    
    # Debugging print statements
    st.write("Response Status Code:", response.status_code)
    st.write("Response Content:", response.text)
    
    try:
        risk_score = response.json().get("risk_score", "No risk_score in response")
        st.write(f"Predicted Risk Score: {risk_score}")
    except requests.exceptions.JSONDecodeError:
        st.error("Error: The response is not valid JSON.")
