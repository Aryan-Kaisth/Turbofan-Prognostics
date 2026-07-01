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

# SUB-DATASET BENCHMARKING HUBS (REDESIGNED)
tab_fd001, tab_fd002, tab_fd003, tab_fd004, tab_summary = st.tabs([
    "✈️ FD001 (Sea Level / Single Fault)",
    "✈️ FD002 (Multi-Regime / Single Fault)",
    "✈️ FD003 (Sea Level / Dual Fault)",
    "✈️ FD004 (Multi-Regime / Dual Fault)",
    "🏆 Overall Benchmark Summary"
])

# SUB-DATASET HUB: FD001
with tab_fd001:
    st.write("")
    
    # Split the description and profile matrix into clean columns
    col_text, col_profile = st.columns([5, 2], gap="large")
    
    with col_text:
        st.markdown("### 📊 Sub-Dataset FD001 Overview")
        st.markdown("""
        **FD001** is the baseline benchmark subset of the NASA C-MAPSS dataset. It contains engine degradation data collected under a **single operating condition** with **a single fault mode**. Since both the operating environment and degradation pattern remain consistent, FD001 exhibits the lowest variability among all benchmark subsets.
        """)
        
    with col_profile:
        with st.container(border=True):
            st.markdown("⚙️ **Operational Profile**")
            st.markdown("- **Environment:** Sea Level (Single)\n- **Fault Modes:** HPC Degradation\n- **Variability:** Low Baseline")

    st.divider()
    
    # Clean workspace nested tabs
    fd001_ml, fd001_dl, fd001_comp = st.tabs(["⚙️ Machine Learning", "🧠 Deep Learning", "🔄 Comparison"])
    
    with fd001_ml:
        st.write("")
        st.markdown("#### Machine Learning Approach")
        st.info("Placeholder: Display your ML model tracking parameters (e.g., CatBoost Regressor, Random Forests, feature engineering runs from 16 to 75 columns) here.")
        
    with fd001_dl:
        st.write("")
        st.markdown("#### Deep Learning Architectures")
        st.info("Placeholder: Display your deep learning metrics (e.g., LSTM, Temporal Convolutional Networks, Attention layers) here.")
        
    with fd001_comp:
        st.write("")
        st.markdown("#### Performance Comparison Matrix")
        st.info("Placeholder: Drop your comparative metrics and model evaluation visualizations for FD001 here.")

# SUB-DATASET HUB: FD002
with tab_fd002:
    st.write("")
    col_text, col_profile = st.columns([5, 2], gap="large")
    
    with col_text:
        st.markdown("### 📊 Sub-Dataset FD002 Evaluation Hub")
        st.markdown("""
        **FD002** increases the complexity by introducing **multiple operating conditions** while retaining **a single fault mode**. The varying operating environments cause greater variation in sensor measurements, requiring predictive models to distinguish between changes caused by operating conditions and those resulting from engine degradation.
        """)
        
    with col_profile:
        with st.container(border=True):
            st.markdown("⚙️ **Operational Profile**")
            st.markdown("- **Environment:** Multi-Regime (6 Conditions)\n- **Fault Modes:** HPC Degradation\n- **Variability:** Moderate / Operational")

    st.divider()
    
    fd002_ml, fd002_dl, fd002_comp = st.tabs(["⚙️ Machine Learning", "🧠 Deep Learning", "🔄 Comparison"])
    
    with fd002_ml:
        st.write("")
        st.markdown("#### Machine Learning Models")
        st.info("Placeholder: Display your ML model metrics tailored for multi-regime operational settings here.")
        
    with fd002_dl:
        st.write("")
        st.markdown("#### Deep Learning Architectures")
        st.info("Placeholder: Display your deep learning model configurations designed for multi-regime settings here.")
        
    with fd002_comp:
        st.write("")
        st.markdown("#### Performance Comparison Matrix")
        st.info("Placeholder: Drop your comparative metrics and model evaluation visualizations for FD002 here.")

# SUB-DATASET HUB: FD003
with tab_fd003:
    st.write("")
    col_text, col_profile = st.columns([5, 2], gap="large")
    
    with col_text:
        st.markdown("### 📊 Sub-Dataset FD003 Evaluation Hub")
        st.markdown("""
        **FD003** maintains **a single operating condition** but introduces **multiple fault modes**. Different degradation mechanisms produce distinct sensor signatures, making the prediction task more challenging. Models evaluated on this subset must learn to generalize across multiple degradation patterns while operating under consistent environmental conditions.
        """)
        
    with col_profile:
        with st.container(border=True):
            st.markdown("⚙️ **Operational Profile**")
            st.markdown("- **Environment:** Sea Level (Single)\n- **Fault Modes:** HPC & Fan Degradation\n- **Variability:** Moderate / Structural")

    st.divider()
    
    fd003_ml, fd003_dl, fd003_comp = st.tabs(["⚙️ Machine Learning", "🧠 Deep Learning", "🔄 Comparison"])
    
    with fd003_ml:
        st.write("")
        st.markdown("#### Machine Learning Models")
        st.info("Placeholder: Display your ML model metrics tested under dual fault degradation profiles here.")
        
    with fd003_dl:
        st.write("")
        st.markdown("#### Deep Learning Architectures")
        st.info("Placeholder: Display your deep learning network configurations capturing dual fault characteristics here.")
        
    with fd003_comp:
        st.write("")
        st.markdown("#### Performance Comparison Matrix")
        st.info("Placeholder: Drop your comparative metrics and model evaluation visualizations for FD003 here.")

# SUB-DATASET HUB: FD004
with tab_fd004:
    st.write("")
    col_text, col_profile = st.columns([5, 2], gap="large")
    
    with col_text:
        st.markdown("### 📊 Sub-Dataset FD004 Evaluation Hub")
        st.markdown("""
        **FD004** combines **multiple operating conditions** with **multiple fault modes**. The simultaneous variation in operating environments and degradation mechanisms results in highly complex sensor behaviour, making this dataset the most comprehensive benchmark for evaluating the robustness and generalization of RUL prediction models.
        """)
        
    with col_profile:
        with st.container(border=True):
            st.markdown("⚙️ **Operational Profile**")
            st.markdown("- **Environment:** Multi-Regime (6 Conditions)\n- **Fault Modes:** HPC & Fan Degradation\n- **Variability:** Maximum Complexity")

    st.divider()
    
    fd004_ml, fd004_dl, fd004_comp = st.tabs(["⚙️ Machine Learning", "🧠 Deep Learning", "🔄 Comparison"])
    
    with fd004_ml:
        st.write("")
        st.markdown("#### Machine Learning Models")
        st.info("Placeholder: Display your ML model architectures dealing with full operational complexity here.")
        
    with fd004_dl:
        st.write("")
        st.markdown("#### Deep Learning Architectures")
        st.info("Placeholder: Display your deep learning frameworks testing structural boundaries under maximum stress here.")
        
    with fd004_comp:
        st.write("")
        st.markdown("#### Performance Comparison Matrix")
        st.info("Placeholder: Drop your comparative metrics and model evaluation visualizations for FD004 here.")

# GLOBAL BENCHMARK SUMMARY
with tab_summary:
    st.write("")
    st.markdown("### 🏆 Global Cross-Dataset Leaderboard")
    st.caption("Consolidated evaluation matrix summarizing the peak performance configurations across all NASA C-MAPSS subsets.")
    st.write("")
    
    with st.container(border=True):
        st.subheader("📋 Top Performing Configurations Summary")
        st.markdown(
            "This space serves as your ultimate performance matrix summary, highlighting the optimal "
            "algorithmic selections discovered during execution profiling."
        )