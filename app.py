import streamlit as st
import joblib
import numpy as np

model = joblib.load("water_potability_model.pkl")
scaler = joblib.load("water_potability_scaler.pkl")

st.title("💧 Water Potability Predictor")

ph = st.slider("pH", 0.0, 14.0, 7.0)
hardness = st.number_input("Hardness", value=150.0)
solids = st.number_input("Solids", value=20000.0)
chloramines = st.number_input("Chloramines", value=7.0)
sulfate = st.number_input("Sulfate", value=333.0)
conductivity = st.number_input("Conductivity", value=400.0)
organic_carbon = st.number_input("Organic Carbon", value=14.0)
trihalomethanes = st.number_input("Trihalomethanes", value=66.0)
turbidity = st.number_input("Turbidity", value=3.9)

if st.button("Predict"):
    features = np.array([[ph, hardness, solids, chloramines,
                          sulfate, conductivity, organic_carbon,
                          trihalomethanes, turbidity]])
    scaled = scaler.transform(features)
    result = model.predict(scaled)[0]
    if result == 1:
        st.success("✅ Water is safe to drink")
    else:
        st.error("❌ Water is NOT safe to drink")
