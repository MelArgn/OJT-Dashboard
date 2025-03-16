import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# 1) COLOR PALETTE
# -----------------------------
colors = [
    "#ef7c8e",  # Hot Pink
    "#fae8e0",  # Cream
    "#b6e2d3",  # Spearmint
    "#d8a7b1",  # Rosewater
    "#fbe7c6",  # Yellow
    "#b4f8c8",  # Mint
    "#a0e7e5",  # Tiffany Blue
    "#ffaebc"   # Light Hot Pink
]

# -----------------------------
# 2) LOAD DATA FUNCTIONS
# -----------------------------
def load_data():
    """Returns three DataFrames: performance, training hours, and operational proficiency"""
    performance_df = pd.DataFrame({
        "Student": [
            "Boatwright Caleel", "Dwayne Pinkard", "Wade Eric", "Matthews Keithan", "Martinez Randell",
            "Brown Christopher", "Courtney Floyd", "Dudley Craig", "Wakefield Daniel", "Aaron Richardson",
            "Soloman Richards", "Wayne Tate", "Taron Stover", "Verneda Dyson", "Anthony Jon Currie",
            "Andrew Thomas", "Vivian Dillard", "Hitcherson Mazie", "Andre Miller", "Diamond Jordan",
            "Farooq Rafeeq", "Aiyana Waddell", "Benjamin Littlejohn", "Anthony Mcpherson", "Winston Richards",
            "Taylor India"
        ],
        "Performance Score (%)": [
            98, 98, 98, 98, 97.8,
            97.3, 97.3, 97, 96, 95,
            94, 93, 92, 92, 92,
            92, 89.2, 89, 89.7, 88,
            87.5, 88, 88, 88, 85.4,
            83
        ]
    })

    training_hours_df = pd.DataFrame({
        "Student": performance_df["Student"],
        "Training Hours": [
            142, 86.9, 57.3, 121.7, 138,
            137, 128, 80, 94.6, 52,
            121.7, 57.3, 9.79, None, 137,
            90, 44, 79.3, 85.2, 86.5,
            44.7, 84, 82, 44, 38.8,
            44
        ],
        "Focus Area": [
            "Mainline/Yard Mix", "Yard Operations", "Mainline/Yard Mix (85/15)", "Mainline", "Yard Operations",
            "Mainline", "Yard", "Mainline", "Mainline", "Mainline",
            "Mainline/Yard Mix", "Mainline/Yard Mix (85/15)", "Mainline Operations", None, "Yard Operations",
            "Mainline", "Mainline", "Yard", "Technical Inspections", "Mainline",
            "Yard/Technical", "Mainline", "Yard Operations", "Mainline", "Yard Operations",
            "Yard/Technical"
        ]
    })
    training_hours_df["Focus Area"] = (
        training_hours_df["Focus Area"]
        .astype(str)
        .str.replace(r"\(.*\)", "", regex=True)
        .str.strip()
        .replace({"None": None})
    )

    safety_data = {
        "Boatwright Caleel": (100, 92),
        "Dwayne Pinkard": (97, 78),
        "Wade Eric": (100, 78),
        "Matthews Keithan": (100, 85),
        "Martinez Randell": (100, 92),
        "Brown Christopher": (100, 85),
        "Courtney Floyd": (91, 72),
        "Dudley Craig": (93, 75),
        "Wakefield Daniel": (95, 88),
        "Aaron Richardson": (None, None),
        "Soloman Richards": (100, 85),
        "Wayne Tate": (100, 85),
        "Taron Stover": (100, 85),
        "Verneda Dyson": (100, 78),
        "Anthony Jon Currie": (92, 74),
        "Andrew Thomas": (95, 89),
        "Vivian Dillard": (100, 88),
        "Hitcherson Mazie": (93, 75),
        "Andre Miller": (89, 70),
        "Diamond Jordan": (100, 78),
        "Farooq Rafeeq": (88, 70),
        "Aiyana Waddell": (89, 68),
        "Benjamin Littlejohn": (87, 68),
        "Anthony Mcpherson": (90, 55),
        "Winston Richards": (87, 70),
        "Taylor India": (91, 55)
    }
    operational_proficiency_df = pd.DataFrame({
        "Student": performance_df["Student"],
        "Safety Compliance (%)": [safety_data[s][0] for s in performance_df["Student"]],
        "TSG Compliance (%)": [safety_data[s][1] for s in performance_df["Student"]]
    })

    return performance_df, training_hours_df, operational_proficiency_df

def load_instructor_feedback_data():
    """Returns instructor feedback DataFrame"""
    feedback_df = pd.DataFrame({
        "Student": [
            "Verneda Dyson", "Vivian Dillard", "Wayne Tate", "Soloman Richards", "Wade Eric",
            "Martinez Randell", "Taron Stover", "Boatwright Caleel", "Matthews Keithan", "Hitcherson Mazie",
            "Brown Christopher", "Wakefield Daniel", "Aiyana Waddell", "Benjamin Littlejohn", "Andre Miller",
            "Diamond Jordan", "Dwayne Pinkard", "Aaron Richardson", "Farooq Rafeeq", "Anthony Mcpherson",
            "Dudley Craig", "Anthony Jon Currie", "Taylor India", "Winston Richards"
        ],
        "Positive (%)": [
            75, 70, 72, 64, 80,
            92, 83, 90, 100, 57,
            93, 62, 64, 55, 85,
            66, 76, 55, 44, 88,
            69, 72, 60, 58
        ],
        "Neutral (%)": [
            0, 7, 10, 15, 10,
            0, 5, 7, 0, 17,
            5, 30, 20, 21, 10,
            21, 12, 30, 33, 5,
            25, 20, 22, 24
        ],
        "Constructive (%)": [
            25, 23, 18, 21, 10,
            8, 12, 3, 0, 26,
            2, 8, 16, 24, 5,
            13, 12, 15, 23, 7,
            6, 8, 18, 18
        ],
        "Notable Feedback": [
            "Exceptional Lunar Signal Verification Skills Require Shop Protocol Focus",
            "Weather Protocol Implementation Remains Critical Gap",
            "Customer Notifications Need Urgent Improvement",
            "Advanced Weather Protocol Needed",
            "Strong Above Standard Performance",
            "Engine Operation Specialist",
            "Radio Compliance Mastered",
            "Signaling Mastery Achieved",
            "Operation Specialist",
            "TSG Policy Clarification Needed",
            "Weather Protocol Mastery",
            "Coupling/Uncoupling Needs",
            "Lane Variation Approaches",
            "Attention Specialist",
            "Coupling/Uncoupling Needs",
            "TSG/Technical Approach",
            "Radio Protocol Mastery Signal Variation",
            "Weather Protocol Implementation",
            "Yard/Technical Proficiency",
            "Speed Regulation Critical",
            "Shop Error Protocols",
            "Mainline Operations Mastery",
            "Radio Protocol Mastery",
            "Speed Regulation Critical"
        ]
    })
    return feedback_df

# ------------------------------------------------
# LOAD DATA
# ------------------------------------------------
performance_df, training_hours_df, operational_proficiency_df = load_data()
feedback_df = load_instructor_feedback_data()

# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------
st.set_page_config(layout="wide")

# ------------------------------------------------
# UPDATED CUSTOM CSS (LIGHT GRAY BORDERS)
# ------------------------------------------------
st.markdown(
    """
    <style>
    body {
        margin: 0;
        padding: 0;
    }
    .stApp {
        background-color: #e3e8f0;
        color: #1f1f1f;
        margin: 0;
        padding: 0;
    }
    .css-18e3th9, .css-10trblm, .css-1dp5vir, .css-1cpxqw2, .css-12oz5g7 {
        color: #1f1f1f !important;
    }
    div[data-testid="stPlotlyChart"] {
        border: 2px solid #cccccc !important;  /* Light Gray */
        padding: 1.5rem !important;
        margin-bottom: 3rem !important;
        border-radius: 5px;
        background-color: #ffffff;
    }
    div[data-testid="stPyplotChart"] {
        border: 2px solid #cccccc !important;  /* Light Gray */
        padding: 1.5rem !important;
        margin-bottom: 3rem !important;
        border-radius: 5px;
        background-color: #ffffff;
    }
    .stSubheader {
        margin-bottom: 2rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------------------------------
# TITLE & SIDEBAR
# ------------------------------------------------
st.title("WMATA OJT RVO 25-01 Student Operator Training Dashboard")
st.sidebar.title("Filters")

# ------------------------------------------------
# FILTER LOGIC
# ------------------------------------------------
filter_all = st.checkbox("Filter entire dashboard by selected student?")
all_option = "All Students"
all_students = list(performance_df["Student"].unique()) + list(feedback_df["Student"].unique())
all_students = sorted(set(all_students), key=lambda x: x or "")
student_list = [all_option] + all_students
selected_student = st.selectbox("Select a Student", student_list)

def filter_df(df, student):
    if student == all_option:
        return df
    else:
        return df[df["Student"] == student]

if filter_all and selected_student != all_option:
    perf_df_filtered = filter_df(performance_df, selected_student)
    train_df_filtered = filter_df(training_hours_df, selected_student)
    op_df_filtered = filter_df(operational_proficiency_df, selected_student)
    feedback_df_filtered = filter_df(feedback_df, selected_student)
else:
    perf_df_filtered = performance_df
    train_df_filtered = training_hours_df
    op_df_filtered = operational_proficiency_df
    feedback_df_filtered = feedback_df

# ------------------------------------------------
# UPDATED PLOTLY LAYOUT FUNCTION
# ------------------------------------------------
def update_plotly_layout(fig, bg_color="#ffffff", font_color="#1f1f1f"):
    fig.update_layout(
        paper_bgcolor=bg_color,
        plot_bgcolor=bg_color,
        font_color=font_color,
        margin=dict(l=20, r=20, t=40, b=20),
        xaxis=dict(
            title_font=dict(color=font_color),
            tickfont=dict(color=font_color)
        ),
        yaxis=dict(
            title_font=dict(color=font_color),
            tickfont=dict(color=font_color)
        )
    )

# ------------------------------------------------
# VISUALIZATIONS
# ------------------------------------------------
# 1) Performance Insights
st.subheader("Performance Insights")
fig_performance = px.bar(
    perf_df_filtered,
    x="Performance Score (%)",
    y="Student",
    orientation='h',
    title="Student Performance Scores",
    color_discrete_sequence=[colors[0]]
)
fig_performance.update_layout(
    height=900,
    bargap=0.2,
    yaxis=dict(categoryorder='array', categoryarray=perf_df_filtered["Student"].tolist())
)
update_plotly_layout(fig_performance)
st.plotly_chart(fig_performance, use_container_width=True)

# 2) Heatmap
if len(perf_df_filtered) > 1:
    perf_matrix = perf_df_filtered.set_index("Student").T
    fig_heatmap, ax = plt.subplots(figsize=(16, 3))
    sns.heatmap(
        perf_matrix,
        cmap="coolwarm",
        annot=True,
        fmt=".1f",
        linewidths=0.5,
        ax=ax,
        cbar_kws={'label': 'Performance Score (%)'}
    )
    ax.set_title("Student Performance Heatmap (Horizontal)", fontsize=16, color="#1f1f1f")
    ax.tick_params(axis='x', colors='#1f1f1f')
    ax.tick_params(axis='y', colors='#1f1f1f')
    for spine in ax.spines.values():
        spine.set_edgecolor('#1f1f1f')
    ax.set_facecolor("#ffffff")
    fig_heatmap.patch.set_facecolor("#ffffff")
    st.pyplot(fig_heatmap)
else:
    st.write("Heatmap not displayed (only one student selected).")

# 3) Scatter Plot
fig_scatter = px.scatter(
    perf_df_filtered.merge(train_df_filtered, on="Student", how="inner"),
    x="Training Hours",
    y="Performance Score (%)",
    title="Training Hours vs. Performance Score",
    color="Focus Area",
    color_discrete_sequence=colors
)
update_plotly_layout(fig_scatter)
st.plotly_chart(fig_scatter, use_container_width=True)

# 4) Training Hours Analysis
st.subheader("Training Hours Analysis")
fig_hist_hours = px.histogram(
    train_df_filtered,
    x="Training Hours",
    nbins=10,
    range_x=[0, 150],
    title="Distribution of Training Hours",
    hover_data=["Student"],
    color_discrete_sequence=[colors[1]]
)
update_plotly_layout(fig_hist_hours)
st.plotly_chart(fig_hist_hours, use_container_width=True)

# 5) Training Hours by Student
st.subheader("Training Hours by Student")
fig_strip = px.strip(
    train_df_filtered,
    x="Training Hours",
    y="Student",
    hover_name="Student",
    title="Training Hours by Student",
    color_discrete_sequence=[colors[3]]
)
fig_strip.update_layout(
    height=900,
    yaxis=dict(categoryorder='array', categoryarray=train_df_filtered["Student"].tolist())
)
update_plotly_layout(fig_strip)
st.plotly_chart(fig_strip, use_container_width=True)

# 6) Individual Performance Scores
st.subheader("Individual Performance Scores")
fig_perf_new = px.bar(
    perf_df_filtered,
    x="Student",
    y="Performance Score (%)",
    title="Individual Performance Scores",
    hover_data=["Student", "Performance Score (%)"],
    color_discrete_sequence=[colors[2]]
)
sorted_students = perf_df_filtered.sort_values("Performance Score (%)", ascending=False)["Student"].tolist()
fig_perf_new.update_layout(
    height=900,
    bargap=0.2,
    xaxis=dict(tickangle=45, categoryorder='array', categoryarray=sorted_students)
)
update_plotly_layout(fig_perf_new)
st.plotly_chart(fig_perf_new, use_container_width=True)

# 7) Focus Areas Pie Chart
fig_pie = px.pie(
    train_df_filtered,
    names="Focus Area",
    title="Focus Areas Breakdown",
    color="Focus Area",
    color_discrete_sequence=colors
)
update_plotly_layout(fig_pie)
st.plotly_chart(fig_pie, use_container_width=True)

# 8) Training Hours Box Plot
fig_box = px.box(
    train_df_filtered,
    x="Focus Area",
    y="Training Hours",
    title="Training Hour Ranges by Focus Area",
    color_discrete_sequence=[colors[5]]
)
update_plotly_layout(fig_box)
st.plotly_chart(fig_box, use_container_width=True)

# 9) Safety Compliance
st.subheader("Safety Compliance Scores")
fig_safety = px.bar(
    op_df_filtered,
    x="Safety Compliance (%)",
    y="Student",
    orientation='h',
    title="Individual Safety Compliance Scores",
    color_discrete_sequence=[colors[6]]
)
fig_safety.update_layout(
    height=900,
    bargap=0.2,
    yaxis=dict(categoryorder='array', categoryarray=op_df_filtered["Student"].tolist())
)
update_plotly_layout(fig_safety)
st.plotly_chart(fig_safety, use_container_width=True)

# 10) TSG Compliance
st.subheader("TSG Compliance Scores")
fig_tsg = px.bar(
    op_df_filtered,
    x="TSG Compliance (%)",
    y="Student",
    orientation='h',
    title="Individual TSG Compliance Scores",
    color_discrete_sequence=[colors[7]]
)
fig_tsg.update_layout(
    height=900,
    bargap=0.2,
    yaxis=dict(categoryorder='array', categoryarray=op_df_filtered["Student"].tolist())
)
update_plotly_layout(fig_tsg)
st.plotly_chart(fig_tsg, use_container_width=True)

# 11) TSG Bubble Chart
low_tsg_df = op_df_filtered[op_df_filtered["TSG Compliance (%)"] < 75]
fig_low_tsg = px.scatter(
    low_tsg_df,
    x="TSG Compliance (%)",
    y="Student",
    size="TSG Compliance (%)",
    title="Bubble Chart: TSG Compliance < 75%",
    color_discrete_sequence=[colors[0]]
)
update_plotly_layout(fig_low_tsg)
st.plotly_chart(fig_low_tsg, use_container_width=True)

# 12) Drill-down Table
st.subheader("Drill-down Table")
full_details = (
    performance_df
    .merge(training_hours_df, on="Student", how="left")
    .merge(operational_proficiency_df, on="Student", how="left")
)
table_data = full_details[full_details["Student"] == selected_student] if selected_student != all_option else full_details
st.dataframe(table_data, use_container_width=True)

# 13) Instructor Feedback
st.subheader("Instructor Feedback Analysis")
melted_feedback = feedback_df_filtered.melt(
    id_vars=["Student", "Notable Feedback"],
    value_vars=["Positive (%)", "Neutral (%)", "Constructive (%)"],
    var_name="Feedback Type",
    value_name="Percentage"
)
fig_feedback = px.bar(
    melted_feedback,
    x="Student",
    y="Percentage",
    color="Feedback Type",
    hover_data=["Notable Feedback"],
    title="Instructor Feedback Analysis",
    barmode="stack",
    color_discrete_sequence=["#90EE90", "#FFD700", "#FFB6C1"]
)
update_plotly_layout(fig_feedback)
fig_feedback.update_layout(xaxis=dict(tickangle=45), height=800)
st.plotly_chart(fig_feedback, use_container_width=True)
