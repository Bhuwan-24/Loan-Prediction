import streamlit as st
import joblib
import numpy as np
import pandas as pd

model = joblib.load("loan_model.pkl")

st.title("Loan Prediction App 🚀")

st.write("Enter applicant details below:")

married = st.selectbox("Married", ["Yes", "No"])
dependents = st.number_input("Dependents", min_value=0, max_value=5, value=0)
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
app_income = st.number_input("Applicant Income")
co_income = st.number_input("Coapplicant Income")
loan_amount = st.number_input("Loan Amount")
loan_term = st.number_input("Loan Amount Term")
credit_history = st.selectbox("Credit History", [1.0, 0.0])
property_area = st.selectbox("Property Area", ["Urban", "Rural", "Semiurban"])

married = 1 if married == "Yes" else 0
education = 1 if education == "Graduate" else 0
self_employed = 1 if self_employed == "Yes" else 0

pa_urban = 1 if property_area == "Urban" else 0
pa_rural = 1 if property_area == "Rural" else 0
pa_semiurban = 1 if property_area == "Semiurban" else 0

features = np.array([[
    married,
    dependents,
    education,
    self_employed,
    app_income,
    co_income,
    loan_amount,
    loan_term,
    credit_history,
    pa_rural,
    pa_semiurban,
    pa_urban
]])

if st.button("Predict Loan Status"):
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("Loan Approved ✅")
    else:
        st.error("Loan Rejected ❌")
