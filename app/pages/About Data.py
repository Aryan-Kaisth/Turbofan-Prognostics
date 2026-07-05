import streamlit as st
import pandas as pd
from pathlib import Path

# SYSTEM CONFIGURATION
ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / "assets"

st.set_page_config(
    page_title="About CMAPSS Data",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

logo_col, title_col = st.columns([1, 9], gap="small")

with logo_col:
    st.markdown("<div style='padding-top: 12px;'></div>", unsafe_allow_html=True)
    st.image(ASSETS / "R.png", width=120)

with title_col:
    st.title("NASA C-MAPSS Dataset Overview")
    st.caption("Detailed information regarding the turbofan engine degradation simulation data.")

st.markdown("---")

# DATASET OVERVIEW ARCHITECTURE
with st.container(border=True):
    st.markdown(
        """
        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 16px;">
            <img src="https://png.pngtree.com/png-vector/20220309/ourmid/pngtree-create-disk-mainframe-big-data-vector-png-image_35660428.png" width="35" style="object-fit: contain;">
            <h3 style="margin: 0; padding: 0; font-size: 1.35rem; font-weight: 600; color: #ffffff;">About Dataset</h3>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("""
    Data sets consists of multiple multivariate time series. Each data set is further divided into :blue[training] and :green[test] subsets. Each time series is from a different engine i.e., the data can be considered to be from a fleet of engines of the same type. 
    Each engine starts with different degrees of initial wear and manufacturing variation which is unknown to the user. This wear and variation is considered normal, i.e., it is not considered a fault condition. 
    There are three operational settings that have a substantial effect on engine performance. These settings are also included in the data. The data is contaminated with sensor noise.
    """)
    
    st.write("")
    
    data_split_col1, data_split_col2 = st.columns(2, gap="medium")
    
    with data_split_col1:
        with st.container(border=True):
            st.markdown("### 🔵 :blue[Training Set: Run-to-Failure]")
            st.markdown("""
            The engine operates normally at the start and develops a fault at some point. The telemetry recording continues uninterrupted **until total system failure**. This provides the model with the complete degradation lifecycle for pattern learning.
            """)
            
    with data_split_col2:
        with st.container(border=True):
            st.markdown("### 🟢 :green[Test Set: Randomly Truncated]")
            st.markdown("""
            The time-series recording is intentionally **cut off at a random operational cycle prior to failure**. The data ends abruptly at an arbitrary point, and the model must infer the remaining cycle count from this blind window.
            """)

    st.write("")

st.write("")

# PHYSICAL SCHEMATIC DISPLAY
col1, col2 = st.columns(2)

with col1:
    st.image(
        "https://www.nasa.gov/wp-content/uploads/2022/05/hytec-engine-callouts-trimmed.png", 
        caption="NASA HyTEC Engine Callouts",
        width='stretch'
    )

with col2:
    st.image(
        ASSETS / "engine.png", 
        caption="Local Engine Asset",
        width='stretch'
    )

st.write("")

# SUB-DATASET MATRIX CARDS
with st.container(border=True):
    st.subheader("📊 Sub-Dataset Configurations")
    st.write("")
    
    card_fd1, card_fd2, card_fd3, card_fd4 = st.columns(4, gap="medium")
    
    with card_fd1:
        with st.container(border=True):
            st.markdown("### ✈️ :blue[FD001]")
            st.markdown("**Train Trajectories:** 100")
            st.markdown("**Test Trajectories:** 100")
            st.markdown("**Operating Regimes:** ONE (Sea Level)")
            st.markdown("**Fault Modes:** High-Pressure Compressor")

    with card_fd2:
        with st.container(border=True):
            st.markdown("### ✈️ :orange[FD002]")
            st.markdown("**Train Trajectories:** 260")
            st.markdown("**Test Trajectories:** 259")
            st.markdown("**Operating Regimes:** SIX (Multi-Envelope)")
            st.markdown("**Fault Modes:** High-Pressure Compressor")

    with card_fd3:
        with st.container(border=True):
            st.markdown("### ✈️ :violet[FD003]")
            st.markdown("**Train Trajectories:** 100")
            st.markdown("**Test Trajectories:** 100")
            st.markdown("**Operating Regimes:** ONE (Sea Level)")
            st.markdown("**Fault Modes:** HPC & Fan Assembly")

    with card_fd4:
        with st.container(border=True):
            st.markdown("### ✈️ :red[FD004]")
            st.markdown("**Train Trajectories:** 248")
            st.markdown("**Test Trajectories:** 249")
            st.markdown("**Operating Regimes:** SIX (Multi-Envelope)")
            st.markdown("**Fault Modes:** HPC & Fan Assembly")

st.write("")

# EXPLORATORY DATA ANALYSIS INTEGRATION PANEL
with st.container(border=True):
    st.markdown("### 🔍 EDA Report")
    st.markdown("""
    I conducted a comprehensive exploratory data analysis (EDA) on the engine telemetry. The complete analysis, including visualizations and key insights, is documented below.
    """)
    st.write("")
    
    st.link_button(
        label="📒 Open EDA Jupyter Notebook",
        url="https://github.com/Aryan-Kaisth/Turbofan-Prognostics/blob/main/notebooks/01_data_exploration.ipynb",
        type="primary"
    )

st.write("")