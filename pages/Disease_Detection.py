import streamlit as st

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

st.title("🌿 Plant Disease Detection")

st.image(
    "assets/disease_banner.jpg",
    use_container_width=True
)

st.markdown("---")

st.info(
    """
### 🚀 DevOps Demonstration Version

This page demonstrates the user interface of the
Plant Disease Detection module.

For this Docker demonstration the trained Deep
Learning model has been removed to keep the
Docker image lightweight.

The complete AI version is available in the
original project.
"""
)

st.markdown("---")

c1, c2, c3 = st.columns(3)

with c1:
    st.success("✅ Docker Ready")

with c2:
    st.success("✅ GitHub Ready")

with c3:
    st.success("✅ CI/CD Ready")

st.markdown("---")

st.subheader("Original Module Features")

st.write("""
✔ Upload Plant Leaf Image

✔ Deep Learning Disease Classification

✔ Treatment Recommendation

✔ Organic Solution

✔ Prevention Guidelines
""")

st.warning(
    "Prediction functionality is disabled in the Docker Demonstration version."
)
