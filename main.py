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
# 🚉 3. MAIN PAGE TITLE & SUBTITLE
# ----------------------------------------------------------------------------
st.title("🚇 Technical Training and Development (Rail Vehicle Operator 25-01 - On the Job Training)")
st.subheader("📊 STUDENT OPERATOR TRAINING PERFORMANCE ANALYSIS")

# ----------------------------------------------------------------------------
# 📄 4. BASIC INFO / EXEC SUMMARY
# ----------------------------------------------------------------------------
st.markdown("""
**WMATA OJT RVO 25-01 Student Operator Training Performance Analysis**  
📅 **Prepared for**: WMATA Leadership  
📆 **Date**: March 14, 2025  
""")

st.markdown("""
### 🏆 Executive Summary
This comprehensive analysis evaluates all **26 student operators'** training performance from **October to November 2024**.  
It highlights:
- 🚉 **Operational readiness**  
- ⏳ **Training investments**  
- ✅ **Proficiency levels**  
- 🎤 **Instructor feedback**  
- 🛠 **Key development priorities**  

The goal is to enhance training efficiency, optimize instructor contributions, and ensure full preparedness for **independent operations**.
""")

# ----------------------------------------------------------------------------
# 🔍 5. SECTION 1: KEY COHORT INSIGHTS & AREAS FOR IMPROVEMENT
# ----------------------------------------------------------------------------
with st.expander("📌 Key Cohort Insights & Areas for Improvement", expanded=True):
    st.markdown("""
    ### 🔹 Key Cohort Insights  
    - 📊 **Performance Range**: 83% – 98%  
    - ⏳ **Training Investment**: 9.79 – 142 hours  
      - *Taron Stover at 9.79h becomes new low-end benchmark*
    - ⚠️ **Critical Gap**: 19/26 operators (73%) require third-car recovery protocol training  
    - 🎤 **New Benchmark**: 7 operators achieved 100% radio compliance  

    ### ⚠️ Areas for Improvement  
    - 🚆 **Third-Car Recovery**: 19 operators below 32% completion  
    - 🌧 **Inclement Weather Readiness**: 13 operators at ≤28% exposure  
    - 📖 **TSG Compliance**: 9 operators below 75% threshold  
    - 🎙 **Radio Deficits**: 24% of the cohort require protocol remediation  
    """)

# ----------------------------------------------------------------------------
# 📊 6. SECTION 2: PERFORMANCE INSIGHTS
# ----------------------------------------------------------------------------
st.markdown("### 📊 Performance Insights")

# 6.1 Overall Student Performance Comparison
with st.expander("🏅 1. Overall Student Performance Comparison", expanded=False):
    st.markdown("""
    **🔹 Analysis**  
    - 🏆 **98% Tier (5 operators)**: Maintained perfect safety compliance and TSG scores ≥85%.  
    - 🚦 **90–97% Tier (8 operators)**: Strong performance but require reinforcement in complex yard maneuvers.  
    - 🚉 **83–89% Tier (9 operators)**: Struggle with concurrent tasks (avg 2.4 assists/run), requiring additional instructor-led drills.  
    - ⚠️ **Critical Divergence**: Operators with <50 hours of training score 19% lower on recovery operations than peers (*p<0.05*), affecting response time in emergency scenarios.  
    - 📉 **New Finding**: Operators below 75% TSG compliance demonstrate 47% more procedural hesitations, leading to increased instructor intervention.
    """)

# 6.2 Training Hours Distribution
with st.expander("⏳ 2. Training Hours Distribution", expanded=False):
    st.markdown("""
    **📊 Critical Findings**  
    - 🕒 **Hour-Effectiveness Threshold**: 90+ hours required for 95% TSG compliance.  
    - 🚦 Operators with **90+ hours of training** exhibit higher proficiency in complex yard operations.  
    - ⚠️ Operators with **<50 hours of training** struggle with emergency recovery protocols, scoring 19% lower in related assessments.  
    - 🔄 **High variability** in training exposure impacts TSG compliance, with those below 75% requiring additional supervised drills.  
    - 🏆 **Yard Focus Advantage**: Martinez Randell achieved **97.8% readiness** with **138 hours** through precision yard training.  
    - 🎙 **Radio Protocol Challenge**: Farooq Rafeeq required **44.7 hours (27% above cohort avg)** to address communication deficits.
    """)

# 6.3 Operational Proficiency Breakdown
with st.expander("⚙️ 3. Operational Proficiency Breakdown", expanded=False):
    st.markdown("""
    **📌 Pattern Identification**  
    - 🔄 **Safety-TSG Disconnect**: 6 operators now achieve **100% safety compliance** but show **≤78% TSG mastery**.  
    - ⚠️ **High-Risk Group**: 9 operators below **75% TSG** require **2.3x more corrective actions** than peers.
    """)

# 6.4 Instructor Feedback Analysis
with st.expander("🎤 4. Instructor Feedback Analysis", expanded=False):
    st.markdown("""
    **📢 Instructor Feedback Patterns**  
    - ⏳ Operators with **>20% neutral feedback** (Diamond Jordan, Taylor India) show **14% slower task initiation**.  
    - 🏆 **92% positive feedback** (Martinez Randell) correlates with **97.8% operational readiness**.  
    - 📖 **Neutral feedback** primarily from non-critical task pauses (e.g., radio channel confirmation).  
    - ⚠️ **Constructive feedback** tied to procedural execution speed or compliance gaps.
    """)

# 6.5 Key Development Priorities
with st.expander("🚀 5. Key Development Priorities", expanded=False):
    st.markdown("""
    **📊 Analysis**  
    - 🔄 **Skill Stacking Requirement**  
      - 🏆 Operators completing **third-car recovery + weather preparedness** achieve **94.6% operational readiness**, reinforcing the need for **combined training approaches**.  
      - ❌ Isolated skill training results in **only 83.1% readiness**, highlighting the benefits of an **integrated training curriculum**.  

    - 📡 **Resource Allocation**  
      - 🎮 **7000-series simulator time** reduces skill gaps **62% faster** than classroom training, demonstrating its effectiveness in accelerating proficiency.  
      - 🏆 **Operators with simulator exposure** outperform peers in **hands-on assessments by 18.8%**, underscoring the need for increased simulator availability.
    """)

# ----------------------------------------------------------------------------
# ℹ️ 7. FOOTER / INFO BOX
# ----------------------------------------------------------------------------
st.info("📌 Use the sidebar to navigate between this Main page and the Charts page.")
