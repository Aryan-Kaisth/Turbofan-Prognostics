import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Benchmark",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Benchmark Study")
st.divider()

with st.container(border=True):
    st.subheader("📋 Experimental Framework & Objectives")
    st.markdown("""
    This section presents a systematic comparative evaluation of multiple predictive modelling approaches for Remaining Useful Life (RUL) estimation on the NASA C-MAPSS dataset. Each model was developed and assessed under a consistent experimental framework, ensuring fair comparison through identical data preparation, validation strategies, and evaluation metrics.

    The objective of this benchmarking study is not only to identify the highest-performing model but also to understand the strengths, limitations, and practical trade-offs of different modelling approaches. All experiments were tracked using MLflow to ensure reproducibility, transparency, and objective comparison throughout the development process.
    """)

    st.image(r'assets\bench.png', width=500)

st.write("")

# ==========================================
if "active_step" not in st.session_state:
    st.session_state.active_step = "Prep"

st.subheader("🛠️ Architecture & Modeling Pipeline")
st.caption("Click on any phase block below to explore our core pipeline engineering steps.")

# Create 5 equal columns to map out the entire workflow layout side-by-side
step_col1, step_col2, step_col3, step_col4, step_col5 = st.columns(5)

with step_col1:
    # Highlighting the active button by switching its button type to primary
    if st.button(
        "1️⃣ Data Prep", 
        use_container_width=True, 
        type="primary" if st.session_state.active_step == "Prep" else "secondary"
    ):
        st.session_state.active_step = "Prep"

with step_col2:
    if st.button(
        "2️⃣ Features", 
        use_container_width=True, 
        type="primary" if st.session_state.active_step == "Features" else "secondary"
    ):
        st.session_state.active_step = "Features"

with step_col3:
    if st.button(
        "3️⃣ Modeling", 
        use_container_width=True, 
        type="primary" if st.session_state.active_step == "Modeling" else "secondary"
    ):
        st.session_state.active_step = "Modeling"

with step_col4:
    if st.button(
        "4️⃣ MLflow Logs", 
        use_container_width=True, 
        type="primary" if st.session_state.active_step == "MLflow" else "secondary"
    ):
        st.session_state.active_step = "MLflow"

with step_col5:
    if st.button(
        "5️⃣ Evaluation", 
        use_container_width=True, 
        type="primary" if st.session_state.active_step == "Evaluation" else "secondary"
    ):
        st.session_state.active_step = "Evaluation"


# Displaying the focal content panel based on the button selected above
with st.container(border=True):
    if st.session_state.active_step == "Prep":
        st.markdown("### 📥 Phase 1: Data Ingestion & Preprocessing")
        st.markdown("Loading multivariate time-series data, handling initial degrees of unknown engine wear, and isolating sensor noise profiles.")
        # st.image("assets/pipeline_step1.png", caption="Data Preprocessing Flowchart", use_container_width=True)
        
    elif st.session_state.active_step == "Features":
        st.markdown("### ⚙️ Phase 2: Feature Engineering & Column Configuration")
        st.markdown("Extracting rolling statistics, lagging features, and running sensitivity tests comparing operational tracking widths ranging from 16 to 75 columns.")
        # st.image("assets/pipeline_step2.png", caption="Feature Selection Matrix", use_container_width=True)
        
    elif st.session_state.active_step == "Modeling":
        st.markdown("### 🤖 Phase 3: Model Architecture Exploration")
        st.markdown("Pitting classical boosting algorithms (CatBoost) against Deep Learning architectures (LSTMs/TCNs) under a shared evaluation structure.")
        # st.image("assets/pipeline_step3.png", caption="Model Topology Layout", use_container_width=True)
        
    elif st.session_state.active_step == "MLflow":
        st.markdown("### 📊 Phase 4: MLflow Experiment Tracking")
        st.markdown("Logging parameters, hyperparameter optimization paths, Balanced Accuracy metrics, and asymmetric NASA penalty scores for absolute reproducibility.")
        # st.image("assets/pipeline_step4.png", caption="MLflow Run Visuals", use_container_width=True)
        
    elif st.session_state.active_step == "Evaluation":
        st.markdown("### 🏆 Phase 5: Global Deployment Evaluation")
        st.markdown("Consolidating performance boundaries across all four distinct sub-datasets (FD001 - FD004) to finalize the absolute best meta-ensemble configurations.")
        # st.image("assets/pipeline_step5.png", caption="Final Deployment Metrics", use_container_width=True)

st.write("")
# ==========================================

# Creating the core layout branches matching your design hierarchy
tab_fd001, tab_fd002, tab_fd003, tab_fd004, tab_summary = st.tabs([
    "✈️ FD001 (Sea Level / Single Fault)",
    "✈️ FD002 (Multi-Regime / Single Fault)",
    "✈️ FD003 (Sea Level / Dual Fault)",
    "✈️ FD004 (Multi-Regime / Dual Fault)",
    "🏆 Overall Benchmark Summary"
])

# FD001
with tab_fd001:
    st.markdown("### Sub-Dataset FD001")

    st.info("""
    **FD001** is the baseline benchmark subset of the NASA C-MAPSS dataset. It contains engine degradation data collected under a **single operating condition** with **a single fault mode**. Since both the operating environment and degradation pattern remain consistent, FD001 exhibits the lowest variability among all benchmark subsets.
    """)
    
    # Nested navigation tabs for the sub-sections
    fd001_ml, fd001_dl, fd001_comp = st.tabs(["⚙️ Machine Learning", "🧠 Deep Learning", "🔄 Comparison"])
    
    with fd001_ml:
        st.markdown("#### Machine Learning Approach")
        st.info("Placeholder: Display your ML model tracking parameters (e.g., CatBoost Regressor, Random Forests, feature engineering runs from 16 to 75 columns) here.")
        
    with fd001_dl:
        st.markdown("#### Deep Learning Architectures")
        st.info("Placeholder: Display your deep learning metrics (e.g., LSTM, Temporal Convolutional Networks, Attention layers) here.")


# FD002
with tab_fd002:
    st.markdown("### Sub-Dataset FD002 Evaluation Hub")
    st.info("""
    **FD002** increases the complexity by introducing **multiple operating conditions** while retaining **a single fault mode**. The varying operating environments cause greater variation in sensor measurements, requiring predictive models to distinguish between changes caused by operating conditions and those resulting from engine degradation.
    """)
    
    fd002_ml, fd002_dl, fd002_comp = st.tabs(["⚙️ Machine Learning", "🧠 Deep Learning", "🔄 Comparison"])
    
    with fd002_ml:
        st.markdown("#### Machine Learning Models")
        st.info("Placeholder: Display your ML model metrics tailored for multi-regime operational settings here.")
        
    with fd002_dl:
        st.markdown("#### Deep Learning Architectures")
        st.info("Placeholder: Display your deep learning model configurations designed for multi-regime settings here.")


# FD003
with tab_fd003:
    st.markdown("### Sub-Dataset FD003 Evaluation Hub")
    st.info("""
    **FD003** maintains **a single operating condition** but introduces **multiple fault modes**. Different degradation mechanisms produce distinct sensor signatures, making the prediction task more challenging. Models evaluated on this subset must learn to generalize across multiple degradation patterns while operating under consistent environmental conditions.
    """)
    
    fd003_ml, fd003_dl, fd003_comp = st.tabs(["⚙️ Machine Learning", "🧠 Deep Learning", "🔄 Comparison"])
    
    with fd003_ml:
        st.markdown("#### Machine Learning Models")
        st.info("Placeholder: Display your ML model metrics tested under dual fault degradation profiles here.")
        
    with fd003_dl:
        st.markdown("#### Deep Learning Architectures")
        st.info("Placeholder: Display your deep learning network configurations capturing dual fault characteristics here.")

# FD004
with tab_fd004:
    st.markdown("### Sub-Dataset FD004 Evaluation Hub")
    st.info("""
    **FD004** combines **multiple operating conditions** with **multiple fault modes**. The simultaneous variation in operating environments and degradation mechanisms results in highly complex sensor behaviour, making this dataset the most comprehensive benchmark for evaluating the robustness and generalization of RUL prediction models.
    """)
    
    fd004_ml, fd004_dl, fd004_comp = st.tabs(["⚙️ Machine Learning", "🧠 Deep Learning", "🔄 Comparison"])
    
    with fd004_ml:
        st.markdown("#### Machine Learning Models")
        st.info("Placeholder: Display your ML model architectures dealing with full operational complexity here.")
        
    with fd004_dl:
        st.markdown("#### Deep Learning Architectures")
        st.info("Placeholder: Display your deep learning frameworks testing structural boundaries under maximum stress here.")


# summary
with tab_summary:
    st.markdown("### 🏆 Global Cross-Dataset Leaderboard")
    st.caption("Consolidated evaluation matrix summarizing the peak performance configurations across all NASA C-MAPSS subsets.")
    
    st.write("")
    
    # Simple setup template to showcase the global comparison chart or leaderboard table later
    with st.container(border=True):
        st.subheader("📋 Top Performing Configurations Summary")
        st.markdown(
            "This space serves as your ultimate performance matrix summary, highlighting the optimal "
            "algorithmic selections discovered during execution profiling."
        )