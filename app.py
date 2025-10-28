# app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from pathlib import Path

# -------------------------------
# Page setup
# -------------------------------
st.set_page_config(
    page_title="Crop Yield Predictor",
    page_icon="🌾",
    layout="wide"
)

# -------------------------------
# Load local CSS (with fallback)
# -------------------------------
css = Path("style.css")
if css.exists():
    st.markdown(f"<style>{css.read_text()}</style>", unsafe_allow_html=True)

# -------------------------------
# Title
# -------------------------------
st.title("🌾 Crop Yield Predictor")
st.caption("Interactive tool to predict yield and explore the impact of irrigation and fertilizer.")

# -------------------------------
# Load trained pipeline
# -------------------------------
MODEL_PATH = "crop_yield_model.pkl"

@st.cache_resource
def load_model(path: str):
    if not os.path.exists(path):
        return None, f"Model file not found at: {path}"
    try:
        model = joblib.load(path)
        return model, None
    except Exception as e:
        return None, f"Failed to load model: {e}"

model, load_err = load_model(MODEL_PATH)
if load_err:
    st.error(load_err)
    st.stop()

# -------------------------------
# Sidebar inputs
# -------------------------------
st.sidebar.header("Input Parameters")

rainfall_mm = st.sidebar.number_input(
    "Rainfall (mm)", min_value=0.0, max_value=2000.0, value=550.0, step=1.0
)
temperature_celsius = st.sidebar.number_input(
    "Temperature (°C)", min_value=-5.0, max_value=50.0, value=27.5, step=0.1
)
days_to_harvest = st.sidebar.number_input(
    "Days to harvest", min_value=30, max_value=300, value=105, step=1
)
fertilizer_used = st.sidebar.checkbox("Fertilizer used", value=True)
irrigation_used = st.sidebar.checkbox("Irrigation used", value=True)

# Build input row
input_row = pd.DataFrame([{
    "Rainfall_mm": rainfall_mm,
    "Temperature_Celsius": temperature_celsius,
    "Fertilizer_Used": fertilizer_used,
    "Irrigation_Used": irrigation_used,
    "Days_to_Harvest": days_to_harvest,
}])

# -------------------------------
# Tabs for outputs
# -------------------------------
tab_pred, tab_insight, tab_about = st.tabs(["Prediction", "Insights", "About"])

# -------------------------------
# Prediction Tab
# -------------------------------
with tab_pred:
    st.subheader("Predicted Yield")
    if st.button("Predict yield", use_container_width=True):
        try:
            pred = float(np.squeeze(model.predict(input_row)))
            st.metric("🌱 Predicted Yield", f"{pred:.2f} t/ha")
        except Exception as e:
            st.error(f"Prediction failed: {e}")
            st.caption("Ensure input columns/dtypes match the trained pipeline.")

# -------------------------------
# Insights Tab
# -------------------------------
with tab_insight:
    st.subheader("Impact of Practices")
    try:
        # Baseline
        pred_base = float(np.squeeze(model.predict(input_row)))

        # Irrigation scenarios
        pred_no_irrig = float(np.squeeze(model.predict(input_row.assign(Irrigation_Used=False))))
        pred_irrig = float(np.squeeze(model.predict(input_row.assign(Irrigation_Used=True))))
        diff_irrig = pred_irrig - pred_no_irrig

        # Fertilizer scenarios
        pred_no_fert = float(np.squeeze(model.predict(input_row.assign(Fertilizer_Used=False))))
        pred_fert = float(np.squeeze(model.predict(input_row.assign(Fertilizer_Used=True))))
        diff_fert = pred_fert - pred_no_fert

        # Responsive metric layout
        col1, col2, col3 = st.columns([1, 1, 1], gap="medium")
        col1.metric("Baseline Yield", f"{pred_base:.2f} t/ha")
        col2.metric("With Irrigation", f"{pred_irrig:.2f} t/ha", f"{diff_irrig:+.2f}")
        col3.metric("With Fertilizer", f"{pred_fert:.2f} t/ha", f"{diff_fert:+.2f}")

        # Sensitivity slider for rainfall
        st.divider()
        st.subheader("Rainfall Sensitivity")
        rain_span = st.slider(
            "Adjust rainfall (mm)", 0, 2000, int(rainfall_mm), 50, key="rain_slider"
        )
        row_rain = input_row.copy()
        row_rain["Rainfall_mm"] = rain_span
        pred_rain = float(np.squeeze(model.predict(row_rain)))
        st.write(f"At {rain_span} mm rainfall, predicted yield = **{pred_rain:.2f} t/ha**")

    except Exception as e:
        st.error(f"Insight calculation failed: {e}")

# -------------------------------
# About Tab
# -------------------------------
with tab_about:
    st.subheader("About this App")
    st.markdown("""
    This app demonstrates a machine learning pipeline for predicting crop yield.

    **Features used:**
    - Rainfall (mm)
    - Temperature (°C)
    - Days to harvest
    - Fertilizer used
    - Irrigation used
    
    **Insights from analysis:**
    - Fertilizer boosts yield by ~1.5 tons/ha.
    - Irrigation improves yield by ~1.2 tons/ha.
    - Rainfall and temperature strongly influence crop choice and yield.
    """)
