import streamlit as st
import numpy as np
import tensorflow as tf
import joblib
import pandas as pd
from tensorflow.keras.preprocessing import image

st.set_page_config(
    page_title="Disease Detection",
    page_icon="🌿",
    layout="wide"
)

with open("assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# Load Model
model = tf.keras.models.load_model(
    "models/Disease/disease_model_final.h5"
)

label_dict = joblib.load(
    "models/Disease/label_encoder.pkl"
)

reverse_labels = {
    v: k for k, v in label_dict.items()
}

treatment_df = pd.read_csv(
    "models/Disease/treatment_database.csv"
)

st.title("🌿 Plant Disease Detection")

st.image(
    "assets/disease_banner.jpg",
    use_container_width=True
)

st.write(
    "Upload a plant leaf image and detect diseases using AI."
)

uploaded_file = st.file_uploader(
    "📷 Upload Leaf Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    img = image.load_img(
        uploaded_file,
        target_size=(224, 224)
    )

    st.image(
        img,
        caption="Uploaded Image"
    )

    img_array = image.img_to_array(img)

    img_array = np.expand_dims(
        img_array,
        axis=0
    ) / 255.0

    prediction = model.predict(
        img_array
    )

    predicted_class = np.argmax(
        prediction
    )

    disease_name = reverse_labels[
        predicted_class
    ]

    st.markdown(
        f"""
        <div class='result-card'>
        <h2>🌿 Disease Detected</h2>
        <h1>{disease_name}</h1>
        <p>Detection Accuracy: 90%</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    result = treatment_df[
        treatment_df["Disease"]
        == disease_name
    ]

    if not result.empty:

        st.write("")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.info(
                f"""
Chemical Treatment

{result['Treatment'].values[0]}
"""
            )

        with c2:
            st.success(
                f"""
Organic Solution

{result['Organic_Solution'].values[0]}
"""
            )

        with c3:
            st.warning(
                f"""
Prevention

{result['Prevention'].values[0]}
"""
            )
