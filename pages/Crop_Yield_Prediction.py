import streamlit as st
import numpy as np
import joblib

st.set_page_config(
    page_title="Crop Yield Prediction",
    page_icon="📈",
    layout="wide"
)

with open("assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# Load models
crop_encoder = joblib.load(
    "models/Yield/crop_encoder.pkl"
)

soil_encoder = joblib.load(
    "models/Yield/soil_encoder.pkl"
)

model = joblib.load(
    "models/Yield/yield_prediction_model.pkl"
)

scaler = joblib.load(
    "models/Yield/yield_scaler.pkl"
)

st.title("📈 Crop Yield Prediction")

st.image(
    "assets/yield_banner.jpg",
    use_container_width=True
)

st.write(
    "Predict crop production using environmental and soil conditions."
)

left, right = st.columns(2)

with left:

    crop = st.selectbox(
        "🌾 Select Crop",
        crop_encoder.classes_
    )

    soil = st.selectbox(
        "🌱 Soil Type",
        soil_encoder.classes_
    )

    soil_pH = st.number_input(
        "Soil pH",
        min_value=0.0,
        max_value=14.0
    )

    temperature = st.number_input(
        "Temperature (°C)"
    )

    humidity = st.number_input(
        "Humidity (%)"
    )

with right:

    wind_speed = st.number_input(
        "Wind Speed"
    )

    N = st.number_input(
        "Nitrogen (N)"
    )

    P = st.number_input(
        "Phosphorus (P)"
    )

    K = st.number_input(
        "Potassium (K)"
    )

    soil_quality = st.number_input(
        "Soil Quality"
    )

st.write("")

if st.button("🚀 Predict Yield"):

    crop_val = crop_encoder.transform(
        [crop]
    )[0]

    soil_val = soil_encoder.transform(
        [soil]
    )[0]

    features = np.array([
        [
            crop_val,
            soil_val,
            soil_pH,
            temperature,
            humidity,
            wind_speed,
            N,
            P,
            K,
            soil_quality
        ]
    ])

    features = scaler.transform(
        features
    )

    prediction = model.predict(
        features
    )[0]

    st.markdown(
        f"""
        <div class='result-card'>
        <h2>📈 Estimated Yield</h2>
        <h1>{prediction:.2f} Tons/Hectare</h1>
        <p>Model R² Score: 0.976</p>
        </div>
        """,
        unsafe_allow_html=True
    )
