import streamlit as st

if
st.set_page_config(
    page_title="Smart Agriculture AI",
    page_icon="🌱",
    layout="wide"
)

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>",
                unsafe_allow_html=True)

st.markdown("""
<div class='hero-title'>
🌱 Smart Agriculture AI System
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='hero-sub'>
Precision Farming Powered by Artificial Intelligence
</div>
""", unsafe_allow_html=True)

st.image(
    "assets/hero_banner.jpg",
    use_container_width=True
)

st.write("")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class='metric-card'>
        <div class='metric-number'>90%</div>
        <div class='metric-label'>
        Disease Detection Accuracy
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='metric-card'>
        <div class='metric-number'>0.976</div>
        <div class='metric-label'>
        Yield Prediction R² Score
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='metric-card'>
        <div class='metric-number'>98%</div>
        <div class='metric-label'>
        Fertilizer Recommendation
        </div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("## 🚀 AI Modules")

c1, c2, c3 = st.columns(3)

with c1:
    st.success("""
🌿 Disease Detection

Detect crop diseases using Deep Learning
""")

with c2:
    st.info("""
📈 Crop Yield Prediction

Estimate future agricultural yield
""")

with c3:
    st.warning("""
🌱 Fertilizer Recommendation

Get intelligent fertilizer suggestions
""")

st.markdown("---")

st.markdown("""
### 🌱 Smart Agriculture AI System

AI-Powered Platform for:

✅ Plant Disease Detection

✅ Crop Yield Forecasting

✅ Fertilizer Recommendation

AI Lab Project 2026
""")
