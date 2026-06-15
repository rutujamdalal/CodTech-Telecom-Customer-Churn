# CodTech-Telecom-Customer-Churn
# CODTECH IT SOLUTIONS INTERNSHIP PROGRAM

## 📋 Intern Information
* **Full Name:** Rutuja Makrant Dalal
* **Intern ID:** [Enter Your CODTECH Intern ID Here]
* **Domain:** Data Analytics Intern
* **Duration:** 4 Weeks
* **Project Name:** Telecom Customer Churn Prediction with Interactive Dashboard

---

## 🎯 Project Scope & Overview
This project addresses a critical business challenge in the telecommunications sector: predicting customer churn (attrition). Using a dataset containing customer profiles, an end-to-end Machine Learning pipeline was constructed to identify high-risk accounts. 

The objective is to equip business stakeholders with a predictive tool to proactively deploy targeted retention strategies (e.g., promotional offers for month-to-month subscribers) before customer contract cancellation occurs.

### Key Deliverables:
1. **Exploratory Data Analysis (EDA):** Uncovering data relationships using visual analytics (`matplotlib`/`seaborn`).
2. **Predictive Modeling:** Training a **Random Forest Classifier** to assess customer departure risk.
3. **Web Application Deployment:** Constructing a live user dashboard using **Streamlit** for real-time model interaction.

---

## 🛠️ Core Technologies & Tools Used
* **Programming Language:** Python
* **Libraries for Data Processing & EDA:** Pandas, NumPy, Matplotlib, Seaborn
* **Machine Learning Framework:** Scikit-Learn
* **Model Serialization:** Pickle
* **Deployment Frontend:** Streamlit Web Server Architecture

---

## 📈 Methodology & Implementation Steps

### 1. Data Cleaning & Preprocessing
* Handled a data type anomaly in the `TotalCharges` column where blank spaces coerced the column into text format.
* Converted empty strings to `NaN` values and cleaned missing rows to refine the dataset.
* Dropped non-predictive features (`customerID`).

### 2. Exploratory Data Analysis (EDA) Insights
* **Contract Risk Factor:** Visualizations revealed that the overwhelming majority of churned customers are on **Month-to-month contracts**.
* **Tenure Vulnerability:** Chart analysis demonstrated a lower median tenure for departing clients, indicating that customer attrition occurs heavily during the initial months of onboarding.

### 3. Feature Engineering & Modeling
* Executed One-Hot Encoding via `pd.get_dummies()` to seamlessly convert categorical text markers into binary arrays (1s and 0s).
* Split the dataset into a train-test ratio utilizing stratification to preserve class proportions across both splits.
* Trained a **Random Forest Classifier** to build the underlying prediction engine.

### 4. Interactive Application Design
* Saved and pickled the model artifacts (`churn_model.pkl`, `model_features.pkl`).
* Engineered a clean, dual-column input layout UI in `app.py` allowing manual slider adjustments for charges/tenure and categorical option selectors for support variables.
* Integrated real-time predictive computation yielding immediate green (Loyal) or red (High Risk) validation metrics.

---
*Developed as part of the CODTECH IT Solutions Data Science Internship.*
