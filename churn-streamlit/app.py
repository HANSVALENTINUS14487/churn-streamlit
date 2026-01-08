import streamlit as st
import joblib
import pandas as pd

model = joblib.load("model_churn.pkl")

st.title("Prediksi Churn Pelanggan")

tenure = st.number_input("Tenure (bulan)", 0, 72)
monthly = st.number_input("Monthly Charges", 0.0)
contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])

data = pd.DataFrame({
    "tenure": [tenure],
    "MonthlyCharges": [monthly],
    "Contract": [contract]
})

if st.button("Prediksi"):
    pred = model.predict(data)[0]
    st.success("Churn" if pred == 1 else "Tidak Churn")