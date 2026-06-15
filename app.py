import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Set up page title and icon
st.set_page_config(page_title="Customer Churn Predictor", page_icon="🔮", layout="centered")

st.title("🔮 Telecom Customer Churn Prediction App")
st.write("Enter customer details below to predict their likelihood of leaving.")

# 1. Load the saved model and features checklist
@st.cache_resource
def load_saved_artifacts():
    with open('churn_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    with open('model_features.pkl', 'rb') as features_file:
        features = pickle.load(features_file)
    return model, features

try:
    model, model_features = load_saved_artifacts()
except FileNotFoundError:
    st.error("Model files not found! Please run your Jupyter notebook cells to save the models first.")
    st.stop()

# 2. Build the User Inputs Interface
st.header("📋 Customer Demographics & Contract Details")

col1, col2 = st.columns(2)

with col1:
    contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    tenure = st.slider("Tenure (Months with company)", min_value=1, max_value=72, value=12)
    monthly_charges = st.number_input("Monthly Charges ($)", min_value=10.0, max_value=150.0, value=65.0)

with col2:
    internet_service = st.selectbox("Internet Service Provider", ["DSL", "Fiber optic", "No"])
    tech_support = st.selectbox("Has Tech Support?", ["Yes", "No", "No internet service"])
    payment_method = st.selectbox("Payment Method", [
        "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
    ])

# 3. Create a dictionary to format input to match training dataframe structure
input_data = {
    'SeniorCitizen': 0, 'tenure': tenure, 'MonthlyCharges': monthly_charges,
    'TotalCharges': tenure * monthly_charges, 
    'gender_Male': 0, 'Partner_Yes': 0, 'Dependents_Yes': 0, 'PhoneService_Yes': 1,
    'MultipleLines_No phone service': 0, 'MultipleLines_Yes': 0,
    'InternetService_Fiber optic': 1 if internet_service == "Fiber optic" else 0,
    'InternetService_No': 1 if internet_service == "No" else 0,
    'OnlineSecurity_No internet service': 1 if internet_service == "No" else 0,
    'OnlineSecurity_Yes': 0, 'OnlineBackup_No internet service': 1 if internet_service == "No" else 0,
    'OnlineBackup_Yes': 0, 'DeviceProtection_No internet service': 1 if internet_service == "No" else 0,
    'DeviceProtection_Yes': 0, 'TechSupport_No internet service': 1 if internet_service == "No" else 0,
    'TechSupport_Yes': 1 if tech_support == "Yes" else 0,
    'StreamingTV_No internet service': 1 if internet_service == "No" else 0,
    'StreamingTV_Yes': 0, 'StreamingMovies_No internet service': 1 if internet_service == "No" else 0,
    'StreamingMovies_Yes': 0, 
    'Contract_One year': 1 if contract == "One year" else 0,
    'Contract_Two year': 1 if contract == "Two year" else 0,
    'PaperlessBilling_Yes': 1,
    'PaymentMethod_Credit card (automatic)': 1 if payment_method == "Credit card (automatic)" else 0,
    'PaymentMethod_Electronic check': 1 if payment_method == "Electronic check" else 0,
    'PaymentMethod_Mailed check': 1 if payment_method == "Mailed check" else 0
}

# Turn input data into a DataFrame matching original format layout 
input_df = pd.DataFrame([input_data])
input_df = input_df[model_features] 

# 4. Predict button logic
st.markdown("---")
if st.button("🔮 Predict Churn Status", use_container_width=True):
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1] * 100
    
    if prediction == 1:
        st.error(f"⚠️ **High Churn Risk!** This customer is highly likely to leave. (Probability: {probability:.1f}%)")
    else:
        st.success(f"✅ **Loyal Customer!** This customer is likely to stay. (Probability of leaving: {probability:.1f}%)")