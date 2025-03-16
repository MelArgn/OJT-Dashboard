import streamlit as st
import os

# ----------------------------------------------------------------------------
# ✅ 1. PAGE CONFIGURATION (Must be the first Streamlit command)
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="Technical Training and Development (Rail Vehicle Operator 25-01 - On the Job Training)",
    page_icon="🚇",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------------------------------
# ✅ 2. LOGO HANDLING (Supports jpg/png)
# ----------------------------------------------------------------------------
LOGO_PATHS = ["images/metro.jpg", "images/metro.png"]

# Check for available logo format
logo_found = False
for path in LOGO_PATHS:
    if os.path.exists(path):
        st.sidebar.image(path, width=150)
        logo_found = True
        break

if not logo_found:
    st.sidebar.warning("⚠️ Logo not found. Please upload 'metro.jpg' or 'metro.png' to the images/ folder.")

# ----------------------------------------------------------------------------
# ✅ 3. MAIN PAGE TITLE & SUBTITLE
# ----------------------------------------------------------------------------
st.title("Technical Training and Development (Rail Vehicle Operator 25-01 - On the Job Training)")
st.subheader("📊 STUDENT OPERATOR TRAINING PERFORMANCE ANALYSIS")

# ----------------------------------------------------------------------------
# ✅ 4. EXECUTIVE SUMMARY
# ----------------------------------------------------------------------------
st.markdown("""
**WMATA OJT RVO 25-01 Student Operator Training Performance Analysis**  
**Prepared for**: WMATA Leadership  
**Date**: March 14, 2025  
""")

st.markdown("""
### 📌 Executive Summary
This analysis evaluates the training performance of **26 student operators** from **October to November 2024**.  
It highlights:
- 🚉 Operational readiness  
- ⏳ Training investments  
- ✅ Proficiency levels  
- 🎤 Instructor feedback  
- 🛠️ Key development priorities  

The goal is to enhance training efficiency, optimize instructor guidance, and ensure readiness for **independent operations**.
""")

# ----------------------------------------------------------------------------
# ✅ 5. SECTION 1: KEY COHORT INSIGHTS & AREAS FOR IMPROVEMENT
# ----------------------------------------------------------------------------
with st.expander("🔍 Key Cohort Insights & Areas for Improvement", expanded=True):
    st.markdown("""
    **📊 Key Cohort Insights**  
    - **Performance Range**: 83% – 98%  
    - **Training Investment**: 9.79 – 142 hours  
    - **Critical Gap**: 19/26 operators (73%) require third-car recovery protocol training  
    - **New Benchmark**: 7 operators achieved 100% radio compliance  

    **⚠️ Areas for Improvement**  
    - **Third-Car Recovery**: 19 operators below 32% completion  
    - **Inclement Weather Readiness**: 13 operators at ≤28% exposure  
    - **TSG Compliance**: 9 operators below 75% threshold  
    - **Radio Deficits**: 24% of the cohort require protocol remediation  
    """)

# ----------------------------------------------------------------------------
# ✅ 6. INSTRUCTIONS & NAVIGATION HELP
# ----------------------------------------------------------------------------
st.info("ℹ️ Use the sidebar to navigate between this Main page and the Charts page.")
