import os
import streamlit as st

# ----------------------------------------------------------------------------
# ✅ 1. PAGE CONFIGURATION (This must be the first Streamlit command)
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="Technical Training and Development (Rail Vehicle Operator 25-01 - On the Job Training)",
    page_icon="🚇",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------------------------------
# ✅ 2. LOGO HANDLING
#    - Ensures the logo is displayed correctly in the sidebar.
# ----------------------------------------------------------------------------
LOGO_PATH = "images/metro.jpg"

if os.path.exists(LOGO_PATH):
    st.sidebar.image(LOGO_PATH, width=150)  # Adjust width if needed
else:
    st.sidebar.warning("⚠️ Logo not found. Please upload 'metro.jpg' to the images/ folder.")

# ----------------------------------------------------------------------------
# ✅ 3. MAIN PAGE TITLE & SUBTITLE
# ----------------------------------------------------------------------------
st.title("Technical Training and Development (Rail Vehicle Operator 25-01 - On the Job Training)")
st.subheader("STUDENT OPERATOR TRAINING PERFORMANCE ANALYSIS")

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
# ✅ 6. SECTION 2: PERFORMANCE INSIGHTS
# ----------------------------------------------------------------------------
st.markdown("### 📈 Performance Insights")

# 6.1 Overall Student Performance
with st.expander("📊 1. Overall Student Performance Comparison", expanded=False):
    st.markdown("""
    **🔹 Key Observations**  
    - **98% Tier (5 operators)**: Maintained perfect safety compliance and TSG scores ≥85%.  
    - **90–97% Tier (8 operators)**: Strong performers, but need improvement in complex yard maneuvers.  
    - **83–89% Tier (9 operators)**: Struggled with multi-tasking (avg 2.4 assists per run).  
    - **Training Hour Impact**: Operators with **<50 hours** scored **19% lower** on recovery tasks.  
    - **TSG Compliance Insight**: Operators **<75% compliance** required **47% more instructor intervention**.
    """)

# 6.2 Training Hours Distribution
with st.expander("⏳ 2. Training Hours Distribution", expanded=False):
    st.markdown("""
    **📊 Key Takeaways**  
    - **90+ Hours Needed**: Operators with **≥90 hours** reached **95% TSG compliance**.  
    - **Training Hour Variability**: Those with **<50 hours** struggled in emergency recovery protocols.  
    - **Yard Focus Success**: Martinez Randell (97.8%) benefited from **138 hours** in precision yard training.  
    - **Communication Challenge**: Farooq Rafeeq spent **27% more hours** on radio protocol remediation.
    """)

# 6.3 Operational Proficiency Breakdown
with st.expander("🛠️ 3. Operational Proficiency Breakdown", expanded=False):
    st.markdown("""
    **📌 Trends Identified**  
    - **Safety vs. TSG Mismatch**: 6 operators achieved **100% safety compliance** but **≤78% TSG mastery**.  
    - **High-Risk Operators**: 9 students with **<75% TSG compliance** required **2.3x more corrective actions**.
    """)

# 6.4 Instructor Feedback Analysis
with st.expander("🎤 4. Instructor Feedback Analysis", expanded=False):
    st.markdown("""
    **📝 Instructor Comments & Patterns**  
    - Operators with **>20% neutral feedback** (e.g., Diamond Jordan) had **14% slower task initiation**.  
    - **92% positive feedback** (Martinez Randell) correlated with **97.8% operational readiness**.  
    - **Constructive feedback** primarily targeted procedural execution speed and compliance gaps.
    """)

# 6.5 Key Development Priorities
with st.expander("🚀 5. Key Development Priorities", expanded=False):
    st.markdown("""
    **🔑 Training Optimization Strategies**  
    - **Skill Stacking**: Operators completing **third-car recovery + weather preparedness** reached **94.6% readiness**.  
    - **Simulator Benefits**:  
      - Hands-on simulator exposure reduced skill gaps **62% faster** than classroom training.  
      - Operators using the **7000-series simulator** outperformed peers by **18.8%** in real-world assessments.
    """)

# ----------------------------------------------------------------------------
# ✅ 7. FOOTER / NAVIGATION HELP
# ----------------------------------------------------------------------------
st.info("ℹ️ Use the sidebar to navigate between this Main page and the Charts page.")
