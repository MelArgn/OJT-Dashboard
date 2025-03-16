import os
import streamlit as st

# ----------------------------------------------------------------------------
# 1. LOGO PATH
#    Use a raw string (r"…") or double backslashes to avoid escape-sequence issues in Windows paths
# ----------------------------------------------------------------------------
LOGO_PATH = "images/logo.jpg"  # Ensure this matches your upload path

if os.path.exists(LOGO_PATH):
    st.sidebar.image(LOGO_PATH, width=150)  # Adjust width as needed
else:
    st.sidebar.write("Logo not found. Please upload 'logo.jpg' to the images/ folder.")

# ----------------------------------------------------------------------------
# 2. PAGE CONFIGURATION
#    Sets the page title, icon, layout, and sidebar state.
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="Technical Training and Development (Rail Vehicle Operator 25-01 - On the Job Training)",
    page_icon="🚇",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------------------------------
# 3. LOGO IN THE SIDEBAR
#    Display the logo at a specific width so it looks more balanced.
# ----------------------------------------------------------------------------
st.sidebar.image(LOGO_PATH, width=150)  # Adjust width as desired (e.g., 120, 200)

# ----------------------------------------------------------------------------
# 4. MAIN PAGE TITLE & SUBTITLE
# ----------------------------------------------------------------------------
st.title("Technical Training and Development (Rail Vehicle Operator 25-01 - On the Job Training)")
st.subheader("STUDENT OPERATOR TRAINING PERFORMANCE ANALYSIS")

# ----------------------------------------------------------------------------
# 5. BASIC INFO / EXEC SUMMARY
# ----------------------------------------------------------------------------
st.markdown("""
**WMATA OJT RVO 25-01 Student Operator Training Performance Analysis**  
**Prepared for**: WMATA Leadership  
**Date**: March 14, 2025  
""")

st.markdown("""
### Executive Summary
This comprehensive analysis evaluates all 26 student operators' training performance from **October to November 2024**. 
It highlights operational readiness, training investments, proficiency levels, instructor feedback, and key development priorities. 
The data-driven insights aim to enhance training efficiency, optimize instructor contributions, and ensure full preparedness for **independent operations**.
""")

# ----------------------------------------------------------------------------
# 6. SECTION 1: KEY COHORT INSIGHTS & AREAS FOR IMPROVEMENT
# ----------------------------------------------------------------------------
with st.expander("Key Cohort Insights & Areas for Improvement", expanded=True):
    st.markdown("""
    **Key Cohort Insights**  
    - **Performance Range**: 83% – 98%  
    - **Training Investment**: 9.79 – 142 hours 
      - *Taron Stover at 9.79h becomes new low-end benchmark*
    - **Critical Gap**: 19/26 operators (73%) require third-car recovery protocol
    - **New Benchmark**: 7 operators achieve 100% radio compliance  

    **Areas for Improvement**  
    - **Third-Car Recovery**: 19 operators below 32% completion  
    - **Inclement Weather Readiness**: 13 operators at ≤28% exposure  
    - **TSG Compliance**: 9 operators below 75% threshold  
    - **Radio Deficits**: 24% of the cohort require protocol remediation  
    """)

# ----------------------------------------------------------------------------
# 7. SECTION 2: PERFORMANCE INSIGHTS
# ----------------------------------------------------------------------------
st.markdown("### Performance Insights")

# 2.1 Overall Student Performance Comparison
with st.expander("1. Overall Student Performance Comparison", expanded=False):
    st.markdown("""
    **Analysis**  
    - **98% Tier (5 operators)**: Maintained perfect safety compliance and TSG scores ≥85%.  
    - **90–97% Tier (8 operators)**: Strong performance but require reinforcement in complex yard maneuvers.  
    - **83–89% Tier (9 operators)**: Struggle with concurrent tasks (avg 2.4 assists/run), requiring additional instructor-led drills.  
    - **Critical Divergence**: Operators with <50 hours of training score 19% lower on recovery operations than peers (*p<0.05*), affecting response time in emergency scenarios.  
    - **New Finding**: Operators below 75% TSG compliance demonstrate 47% more procedural hesitations, leading to increased instructor intervention.
    """)

# 2.2 Training Hours Distribution
with st.expander("2. Training Hours Distribution", expanded=False):
    st.markdown("""
    **Critical Findings**  
    - **Hour-Effectiveness Threshold**: 90+ hours required for 95% TSG compliance.  
    - Operators with 90+ hours of training exhibit higher proficiency in complex yard operations.  
    - Operators with <50 hours of training struggle with emergency recovery protocols, scoring 19% lower in related assessments.  
    - High variability in training exposure impacts TSG compliance, with those below 75% requiring additional supervised drills.  
    - **Yard Focus Advantage**: Martinez Randell achieved 97.8% readiness with 138 hours through precision yard training.  
    - **Radio Protocol Challenge**: Farooq Rafeeq required 44.7 hours (27% above cohort avg) to address communication deficits.
    """)

# 2.3 Operational Proficiency Breakdown
with st.expander("3. Operational Proficiency Breakdown", expanded=False):
    st.markdown("""
    **Pattern Identification**  
    - **Safety-TSG Disconnect**: 6 operators now achieve 100% safety compliance but show ≤78% TSG mastery.  
    - **High-Risk Group**: 9 operators below 75% TSG require 2.3x more corrective actions than peers.
    """)

# 2.4 Instructor Feedback Analysis
with st.expander("4. Instructor Feedback Analysis", expanded=False):
    st.markdown("""
    **Pattern Identification**  
    - Operators with >20% neutral feedback (Diamond Jordan, Taylor India) show 14% slower task initiation.  
    - 92% positive feedback (Martinez Randell) correlates with 97.8% operational readiness.  
    - Neutral feedback primarily from non-critical task pauses (e.g., radio channel confirmation).  
    - Constructive feedback tied to procedural execution speed or compliance gaps.
    """)

# 2.5 Key Development Priorities
with st.expander("5. Key Development Priorities", expanded=False):
    st.markdown("""
    **Analysis**  
    - **Skill Stacking Requirement**  
      - Operators completing third-car recovery + weather preparedness achieve 94.6% operational readiness, reinforcing the need for combined training approaches.  
      - Isolated skill training results in only 83.1% readiness, highlighting the benefits of an integrated training curriculum.
    - **Resource Allocation**  
      - 7000-series simulator time reduces skill gaps 62% faster than classroom training, demonstrating its effectiveness in accelerating proficiency.  
      - Operators with simulator exposure outperform peers in hands-on assessments by 18.8%, underscoring the need for increased simulator availability.
    """)

# ----------------------------------------------------------------------------
# 8. FOOTER / INFO BOX
# ----------------------------------------------------------------------------
st.info("Use the sidebar to navigate between this Main page and the Charts page.")
