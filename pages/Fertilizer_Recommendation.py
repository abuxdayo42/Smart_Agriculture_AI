import streamlit as st

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

st.title("🌱 Fertilizer Recommendation")

st.image(
    "assets/fertilizer_banner.jpg",
    use_container_width=True
)

st.markdown("---")

st.info("""
### 🚀 DevOps Demonstration Version

This page demonstrates the Fertilizer
Recommendation interface.

The trained Machine Learning model has been
removed to reduce Docker image size.

The complete AI version remains available in the
original project.
""")

st.markdown("---")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Reliability", "98%")

with c2:
    st.metric("Docker", "Ready")

with c3:
    st.metric("CI/CD", "Ready")

st.markdown("---")

st.subheader("Original Features")

st.write("""
✔ Soil Analysis

✔ Nutrient Analysis

✔ Crop Selection

✔ AI Recommendation

✔ Smart Fertilizer Suggestion
""")

st.warning(
    "Recommendation functionality is disabled in the Docker Demonstration version."
)
