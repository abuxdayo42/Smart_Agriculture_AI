import streamlit as st

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

st.title("📈 Crop Yield Prediction")

st.image(
    "assets/yield_banner.jpg",
    use_container_width=True
)

st.markdown("---")

st.info("""
### 🚀 DevOps Demonstration Version

This page demonstrates the Crop Yield Prediction
interface.

Machine Learning models have been removed for
Docker optimization.

The original AI version contains the complete
prediction system.
""")

st.markdown("---")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Model", "Random Forest")

with c2:
    st.metric("R² Score", "0.976")

with c3:
    st.metric("Docker", "Ready")

st.markdown("---")

st.subheader("Original Features")

st.write("""
✔ Crop Selection

✔ Soil Analysis

✔ Weather Parameters

✔ Yield Estimation

✔ AI Prediction
""")

st.warning(
    "Prediction functionality is disabled in the Docker Demonstration version."
)
