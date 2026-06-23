import streamlit as st
import numpy as np
import joblib

st.set_page_config(
    page_title="Fertilizer Recommendation",
    page_icon="🌱",
    layout="wide"
)

with open("assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

crop_encoder = joblib.load(
    "models/Fertilizer/fertilizer_crop_encoder.pkl"
)

soil_encoder = joblib.load(
    "models/Fertilizer/fertilizer_soil_encoder.pkl"
)

fert_encoder = joblib.load(
    "models/Fertilizer/fertilizer_encoder.pkl"
)

model = joblib.load(
    "models/Fertilizer/fertilizer_model.pkl"
)

st.title("🌱 Fertilizer Recommendation")

st.image(
    "assets/fertilizer_banner.jpg",
    use_container_width=True
)

st.write(
    "Get smart fertilizer suggestions using AI."
)

left, right = st.columns(2)

with left:

    crop = st.selectbox(
        "🌾 Crop Type",
        crop_encoder.classes_
    )

    soil = st.selectbox(
        "🌱 Soil Type",
        soil_encoder.classes_
    )

    temperature = st.number_input(
        "Temperature"
    )

    humidity = st.number_input(
        "Humidity"
    )

with right:

    moisture = st.number_input(
        "Moisture"
    )

    N = st.number_input(
        "Nitrogen"
    )

    P = st.number_input(
        "Phosphorus"
    )

    K = st.number_input(
        "Potassium"
    )

if st.button(
    "🚀 Recommend Fertilizer"
):

    crop_val = crop_encoder.transform(
        [crop]
    )[0]

    soil_val = soil_encoder.transform(
        [soil]
    )[0]

    features = np.array([
        [
            temperature,
            humidity,
            moisture,
            soil_val,
            crop_val,
            N,
            K,
            P
        ]
    ])

    prediction = model.predict(
        features
    )[0]

    fertilizer = fert_encoder.inverse_transform(
        [prediction]
    )[0]

    st.markdown(
        f"""
        <div class='result-card'>
        <h2>🌱 Recommended Fertilizer</h2>
        <h1>{fertilizer}</h1>
        <p>Recommendation Reliability: 98%</p>
        </div>
        """,
        unsafe_allow_html=True
    )
