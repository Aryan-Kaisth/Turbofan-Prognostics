import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="About CMAPSS Data",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

logo_col, title_col = st.columns([1, 9], gap="small")

with logo_col:
    # Add a tiny bit of markdown padding to drop the logo down slightly
    st.markdown("<div style='padding-top: 12px;'></div>", unsafe_allow_html=True)
    st.image("https://data.nasa.gov/img/NASA_logo.png", width=100)

with title_col:
    st.title("NASA C-MAPSS Dataset Overview")
    st.caption("Detailed information regarding the turbofan engine degradation simulation data.")

st.markdown("---")

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
    
    The engine is operating normally at the start of each time series, and develops a fault at some point during the series. In the :blue[training] set, the fault grows in magnitude until system failure. In the :green[test] set, the time series ends some time prior to system failure. 
    """)

    st.info("""
    The objective of the competition is to predict the number of remaining operational cycles before failure in the test set, i.e., the number of operational cycles after the last cycle that the engine will continue to operate. 
    Also provided a vector of true Remaining Useful Life (RUL) values for the test data.
    """)

st.write("")
col1, col2 = st.columns(2)

with col1:
    st.image(
        r"https://www.nasa.gov/wp-content/uploads/2022/05/hytec-engine-callouts-trimmed.png", 
        caption="NASA HyTEC Engine Callouts",
        use_container_width=True
    )

with col2:
    st.image(
        r"assets\engine.png", 
        caption="Local Engine Asset",
        use_container_width=True
    )

st.write("")

with st.container(border=True):
    st.subheader("🔍 Detailed Feature Reference")
    st.markdown("""
    According to the source documentation, the C-MAPSS simulator monitors a total of 58 outputs. 
    A subset of **21 sensor measurements** and **3 operational settings** were extracted to construct the 26 data columns.
    """)
    
    # Constructing the comprehensive 26 column map dataframe
    feature_map = {
        "Column Index": [f"Column {i}" for i in range(1, 27)],
        "Category": ["Identifier"]*2 + ["Operational Setting"]*3 + ["Sensor Measurement"]*21,
        "Symbol": [
            "Unit", "Cycle", "Setting 1", "Setting 2", "Setting 3", 
            "T2", "T24", "T30", "T50", "P2", "P15", "P30", "Nf", "Nc", 
            "epr", "Ps30", "phi", "NRf", "NRc", "BPR", "farB", "htBleed", 
            "Nf_dmd", "PCNfR_dmd", "W31", "W32"
        ],
        "Feature Name / Description": [
            "Unit Number (Engine ID)", "Time in Operational Cycles",
            "Altitude (Range: 0 - 42K ft.)", "Mach Number (Range: 0 - 0.84)", "Throttle Resolver Angle (TRA, Range: 20 - 100)",
            "Total temperature at fan inlet", "Total temperature at LPC outlet", "Total temperature at HPC outlet", "Total temperature at LPT outlet",
            "Pressure at fan inlet", "Total pressure in bypass-duct", "Total pressure at HPC outlet", "Physical fan speed", "Physical core speed",
            "Engine pressure ratio (P50/P2)", "Static pressure at HPC outlet", "Ratio of fuel flow to Ps30", "Corrected fan speed", "Corrected core speed",
            "Bypass Ratio", "Burner fuel-air ratio", "Bleed Enthalpy",
            "Demanded fan speed", "Demanded corrected fan speed", "HPT coolant bleed", "LPT coolant bleed"
        ],
        "Unit": [
            "—", "Cycles", "ft", "Mach", "°", 
            "°R", "°R", "°R", "°R", "psia", "psia", "psia", "rpm", "rpm", 
            "—", "psia", "pps/psi", "rpm", "rpm", "—", "—", "—", 
            "rpm", "rpm", "lbm/s", "lbm/s"
        ]
    }
    
    df_features = pd.DataFrame(feature_map)
    
    # Render with Streamlit's data table component, enabling filtering and column sorting
    st.dataframe(
        df_features, 
        hide_index=True, 
        use_container_width=True,
        column_config={
            "Column Index": st.column_config.TextColumn(help="Exact position in the space-separated text file."),
            "Category": st.column_config.TextColumn(help="The nature of the feature column.")
        }
    )
    
    st.caption("⚠️ Note: Internal performance tracking dimensions (such as Exhaust Gas Temperature margin and component Stall Margins) were utilized strictly to compute the simulation run lifetime limits and were excluded from these participant feature sets.")

    left_spacer, center_col, right_spacer = st.columns([1, 2, 1])

    with center_col:
        st.image(
            r"assets\diagram.png", 
            caption="Engine Diagram",
            use_container_width=False
        )

st.write("")

with st.container(border=True):
    st.subheader("📊 Sub-Dataset Configurations")
    
    subset_data = {
        "Sub-Dataset": ["FD001.txt", "FD002.txt", "FD003.txt", "FD004.txt"],
        "Train Trajectories": [100, 260, 100, 248],
        "Test Trajectories": [100, 259, 100, 249],
        "Operating Conditions": ["ONE (Sea Level)", "SIX", "ONE (Sea Level)", "SIX"],
        "Fault Modes": ["ONE (HPC Degradation)", "ONE (HPC Degradation)", "TWO (HPC & Fan Degradation)", "TWO (HPC & Fan Degradation)"]
    }
    
    df = pd.DataFrame(subset_data)
    st.dataframe(df, hide_index=True, use_container_width=True)

st.write("") 

st.link_button(
    label="🔗 Download Dataset",
    url="https://data.nasa.gov/dataset/cmapss-jet-engine-simulated-data",
    type="primary"
)