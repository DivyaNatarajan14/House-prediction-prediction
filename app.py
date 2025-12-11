import pandas as pd
import streamlit as st
import joblib

# -------------------------------
# Load Model
# -------------------------------
model = joblib.load("xgb_model.jb")

# -------------------------------
# Page Config & Style
# -------------------------------
st.set_page_config(page_title="House Price Prediction", layout="centered")

st.markdown("""
    <style>
        body {
            background-color: #f5f5f5;
        }
        .main-card {
            background-color: white;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
        }
        .prediction-box {
            background-color: #e9ffe9;
            padding: 18px;
            border-left: 5px solid #2e8b57;
            border-radius: 8px;
            font-size: 18px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# Title
# -------------------------------
st.title("🏠 House Price Prediction")
st.write("Fill the details below to estimate the house selling price.")

# -------------------------------
# Input Features
# -------------------------------
inputs = [
    'OverallQual', 'GrLivArea', 'GarageArea', '1stFlrSF',
    'FullBath', 'YearBuilt', 'YearRemodAdd', 'Fireplaces',
    'BsmtFinSF1', 'WoodDeckSF', 'OpenPorchSF', 'LotArea', 'CentralAir'
]

input_data = {}

# -------------------------------
# Input Form (Two-Column)
# -------------------------------
st.markdown("<div class='main-card'>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

for i, feature in enumerate(inputs):
    with col1 if i % 2 == 0 else col2:

        if feature == "CentralAir":
            input_data[feature] = st.selectbox(
                "Central Air Conditioning?",
                ["Yes", "No"],
                key=f"select_{feature}"
            )

        else:
            input_data[feature] = st.number_input(
                feature,
                value=0.0,
                step=1.0 if feature in ['OverallQual', 'FullBath', 'Fireplaces'] else 0.1,
                key=f"num_{feature}"
            )

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------
# Predict Button
# -------------------------------
if st.button("🔍 Predict House Price"):
    # Convert CentralAir Yes/No to 1/0
    input_data['CentralAir'] = 1 if input_data['CentralAir'] == "Yes" else 0

    # Convert dictionary to DataFrame
    input_df = pd.DataFrame([input_data], columns=inputs)

    # Predict house price
    prediction = model.predict(input_df)[0]

    # Display result
    st.markdown(
        f"<div class='prediction-box'> Predicted House Price: ${prediction:,.2f} </div>",
        unsafe_allow_html=True
    )
