import streamlit as st
import joblib
import pandas as pd

model = joblib.load("model/rf_churn_model.pkl")

st.title("Customer Churn Prediction")

tenure = st.number_input("Tenure", min_value=0)
monthly = st.number_input("Monthly Charges", min_value=0.0)

if st.button("Predict"):
    X = pd.DataFrame({
        "tenure": [tenure],
        "MonthlyCharges": [monthly]
    })
    pred = model.predict(X)
    st.write("Churn:", "Yes" if pred[0] == 1 else "No")
