import streamlit as st
import pandas as pd

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

ASSETS = BASE_DIR / "assets"

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

col1, col2 = st.columns(2)

with col1:
    st.image(
        "https://www.nasa.gov/wp-content/uploads/2022/05/hytec-engine-callouts-trimmed.png", 
        caption="NASA HyTEC Engine Callouts",
        use_container_width=True
    )

with col2:
    st.image(
        ASSETS / "engine.png", 
        caption="Local Engine Asset",
        use_container_width=True
    )

st.write("")

with st.container(border=True):
    st.subheader("📊 Sub-Dataset Configurations")
    st.write("")
    
    # Render 4 side-by-side operational cards instead of flat table rows
    card_fd1, card_fd2, card_fd3, card_fd4 = st.columns(4, gap="medium")
    
    with card_fd1:
        with st.container(border=True):
            st.markdown("### :blue[FD001.txt]")
            st.markdown("**Train Trajectories:** 100")
            st.markdown("**Test Trajectories:** 100")
            st.markdown("**Operating Conditions:** ONE (Sea Level)")
            st.markdown("**Fault Modes:** ONE (HPC Degradation)")

    with card_fd2:
        with st.container(border=True):
            st.markdown("### :blue[FD002.txt]")
            st.markdown("**Train Trajectories:** 260")
            st.markdown("**Test Trajectories:** 259")
            st.markdown("**Operating Conditions:** SIX")
            st.markdown("**Fault Modes:** ONE (HPC Degradation)")

    with card_fd3:
        with st.container(border=True):
            st.markdown("### :blue[FD003.txt]")
            st.markdown("**Train Trajectories:** 100")
            st.markdown("**Test Trajectories:** 100")
            st.markdown("**Operating Conditions:** ONE (Sea Level)")
            st.markdown("**Fault Modes:** TWO (HPC & Fan Degradation)")

    with card_fd4:
        with st.container(border=True):
            st.markdown("### :blue[FD004.txt]")
            st.markdown("**Train Trajectories:** 248")
            st.markdown("**Test Trajectories:** 249")
            st.markdown("**Operating Conditions:** SIX")
            st.markdown("**Fault Modes:** TWO (HPC & Fan Degradation)")

st.write("")

import streamlit as st

with st.container(border=True):
    st.subheader("🔍 Detailed Feature Reference")
    st.markdown("""
    According to the source documentation, the C-MAPSS simulator monitors a total of 58 outputs. 
    A subset of **21 sensor measurements** and **3 operational settings** were extracted to construct the 26 data columns.
    """)
    st.write("")
    
    # Split the reference into 3 digestible interactive tabs
    tab_id, tab_settings, tab_sensors = st.tabs([
        "🆔 Core Identifiers", 
        "⚙️ Operational Settings", 
        "📡 Telemetry Sensor Streams"
    ])
    
    # TAB 1
    with tab_id:
        st.write("")
        id_col1, id_col2 = st.columns(2, gap="medium")
        with id_col1:
            with st.container(border=True):
                st.markdown("#### **Column 1: Unit (Engine ID)**")
                st.markdown("**Category:** Fleet Identifier | **Unit:** —")
                st.caption("Unique identification index assigned to each individual engine asset within the fleet. Used to isolate and group independent time-series trajectories from nominal operation up to structural failure.")
        with id_col2:
            with st.container(border=True):
                st.markdown("#### **Column 2: Cycle**")
                st.markdown("**Category:** Temporal Anchor | **Unit:** Cycles")
                st.caption("Discrete flight counter tracking elapsed operational cycles. Each cycle encapsulates a complete flight profile (takeoff, cruise, and landing), serving as the primary time-step axis for progressive wear modeling.")

    # TAB 2
    with tab_settings:
        st.write("")
        set_col1, set_col2, set_col3 = st.columns(3, gap="small")
        with set_col1:
            with st.container(border=True):
                st.markdown("#### **Column 3: Setting 1**")
                st.markdown("**Parameter:** Flight Altitude")
                st.markdown("**Range:** 0 - 42K ft. | **Unit:** ft")
                st.caption("Dictates ambient atmospheric pressure and environmental density boundaries, which heavily scale base sensor telemetry distributions.")
        with set_col2:
            with st.container(border=True):
                st.markdown("#### **Column 4: Setting 2**")
                st.markdown("**Parameter:** Mach Number")
                st.markdown("**Range:** 0 - 0.84 | **Unit:** Mach")
                st.caption("Indicates true flight airspeed relative to the speed of sound, defining aerodynamic loading and inlet ram air pressure coefficients.")
        with set_col3:
            with st.container(border=True):
                st.markdown("#### **Column 5: Setting 3**")
                st.markdown("**Parameter:** Throttle Resolver Angle (TRA)")
                st.markdown("**Range:** 20 - 100 | **Unit:** °")
                st.caption("Measures raw pilot power demand inputs, directly regulating core fuel schedules and baseline thermodynamic cycle intensity.")

    # TAB 3
    with tab_sensors:
        st.write("")
        st.markdown("##### Select any sensor channel below to inspect its exact telemetry definition:")
        
        sensor_lookup = {
            "T2 (Column 6)": (
                "Total Temperature at Fan Inlet", 
                "Tracks the stagnation temperature of the ambient air entering the engine face intake boundary.", 
                "°R"
            ),
            "T24 (Column 7)": (
                "Total Temperature at LPC Outlet", 
                "Measures the temperature of the air mass at the exit interface of the Low-Pressure Compressor stage.", 
                "°R"
            ),
            "T30 (Column 8)": (
                "Total Temperature at HPC Outlet", 
                "Measures the temperature of the working fluid at the discharge of the High-Pressure Compressor, directly at the combustor inlet.", 
                "°R"
            ),
            "T50 (Column 9)": (
                "Total Temperature at LPT Outlet", 
                "Tracks the gas path temperature at the exhaust exit of the Low-Pressure Turbine stage.", 
                "°R"
            ),
            "P2 (Column 10)": (
                "Pressure at Fan Inlet", 
                "Tracks the total stagnation pressure of the air entering the engine face, incorporating ambient pressure and ram air effects.", 
                "psia"
            ),
            "P15 (Column 11)": (
                "Total Pressure in Bypass-Duct", 
                "Measures the total pressure profile inside the secondary cold-stream bypass duct housing.", 
                "psia"
            ),
            "P30 (Column 12)": (
                "Total Pressure at HPC Outlet", 
                "Measures the peak total pressure achieved by the compressor stages, recorded at the exit of the High-Pressure Compressor.", 
                "psia"
            ),
            "Nf (Column 13)": (
                "Physical Fan Speed", 
                "Logs the actual mechanical rotational speed of the low-pressure spool assembly (connecting the fan and the low-pressure turbine).", 
                "rpm"
            ),
            "Nc (Column 14)": (
                "Physical Core Speed", 
                "Logs the actual mechanical rotational speed of the high-pressure core spool shaft (connecting the core compressor and high-pressure turbine).", 
                "rpm"
            ),
            "epr (Column 15)": (
                "Engine Pressure Ratio (P50/P2)", 
                "Represents the dimensionless ratio of the total turbine discharge pressure relative to the engine face inlet pressure.", 
                "—"
            ),
            "Ps30 (Column 16)": (
                "Static Pressure at HPC Outlet", 
                "Measures the static force pressure of the compressed air stream within the combustor diffuser section.", 
                "psia"
            ),
            "phi (Column 17)": (
                "Ratio of Fuel Flow to Ps30", 
                "Represents the computed ratio of the engine's primary fuel mass flow rate relative to the core static discharge pressure.", 
                "pps/psi"
            ),
            "NRf (Column 18)": (
                "Corrected Fan Speed", 
                "The mechanical rotational speed of the low-pressure spool mathematically adjusted to a standard atmospheric reference temperature.", 
                "rpm"
            ),
            "NRc (Column 19)": (
                "Corrected Core Speed", 
                "The mechanical rotational speed of the high-pressure core spool mathematically adjusted to a standard day temperature baseline.", 
                "rpm"
            ),
            "BPR (Column 20)": (
                "Bypass Ratio", 
                "Represents the volumetric flow rate ratio of air routed through the cold bypass channel relative to the hot combustion core channel.", 
                "—"
            ),
            "farB (Column 21)": (
                "Burner Fuel-Air Ratio", 
                "Represents the calculated mass ratio of injected fuel relative to the total core air mass flow rate inside the main burner zone.", 
                "—"
            ),
            "htBleed (Column 22)": (
                "Bleed Enthalpy", 
                "Logs the calculated heat energy metric across the engine's customer bleed air extraction ports.", 
                "—"
            ),
            "Nf_dmd (Column 23)": (
                "Demanded Fan Speed", 
                "The exact target low-pressure spool rotational speed commanded by the digital engine control software logic.", 
                "rpm"
            ),
            "PCNfR_dmd (Column 24)": (
                "Demanded Corrected Fan Speed", 
                "The target temperature-corrected low-pressure spool speed requested by the automated control loop baseline.", 
                "rpm"
            ),
            "W31 (Column 25)": (
                "HPT Coolant Bleed", 
                "Measures the mass flow rate of secondary cooling air diverted into the high-pressure turbine blades.", 
                "lbm/s"
            ),
            "W32 (Column 26)": (
                "LPT Coolant Bleed", 
                "Measures the mass flow rate of secondary cooling air routed to the structural components of the low-pressure turbine section.", 
                "lbm/s"
            )
        }
        
        selected_sensor = st.selectbox(
            "Telemetry Stream Selector", 
            options=list(sensor_lookup.keys()),
            label_visibility="collapsed"
        )
        
        # Safely unpack the updated 3-part feature metadata
        full_title, detailed_desc, unit_measure = sensor_lookup[selected_sensor]
        with st.container(border=True):
            inspect_l, inspect_r = st.columns([3, 1])
            with inspect_l:
                st.markdown(f"### 📡 Sensor Channel: **{selected_sensor.split(' ')[0]}**")
                st.markdown(f"**Parameter Label:** {full_title}")
                st.markdown(f"**Context:** {detailed_desc}")
            with inspect_r:
                st.metric(label="Measurement Unit", value=unit_measure)
                
    st.write("")

    left_spacer, center_col, right_spacer = st.columns([1, 2, 1])
    with center_col:
        st.image(
            ASSETS / "diagram.png", 
            caption="Engine Diagram",
            use_container_width=False
        )

st.write("")

st.link_button(
    label="🔗 Download Dataset",
    url="https://data.nasa.gov/dataset/cmapss-jet-engine-simulated-data",
    type="primary"
)