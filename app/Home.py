import streamlit as st

st.set_page_config(
    page_title="RUL Research and Benchmark",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

left, right = st.columns([4, 3], gap="large")

with left:
    # Use vertical padding alignment to balance the text with the asset window
    st.markdown("<div style='padding-top: 25px;'></div>", unsafe_allow_html=True)
    st.title("Turbofan-Prognostics")
    st.markdown(
        "Aircraft engine degradation modeling and Remaining Useful Life (RUL) prediction "
        "using multivariate sensor time-series from the NASA C-MAPSS benchmark."
    )

with right:
    # Fixed slash to prevent escape character bugs while keeping your filename
    st.image('assets/iqy49grs.png', use_container_width=True)

st.divider()

with st.container(border=True):
    st.subheader("📋 Project Overview")
    
    st.markdown("""
    TurboFan Prognostics is a benchmark and research project focused on predicting the Remaining Useful Life (RUL) of aircraft engines using the NASA C-MAPSS time-series dataset.
    The goal of this project isn't just to build a single predictive model, but to systematically evaluate how different feature engineering choices, data transformations, and modeling approaches impact performance when estimating engine degradation.
    """)

st.write("")

with st.container(border=True):
    st.subheader("💡 What is RUL & Why It Matters?")
    
    st.markdown("""
    **Remaining Useful Life (RUL)** is the estimated number of operational cycles (or flights) an engine component has left before it degrades past a safe performance threshold. Rather than treating asset health as a simple binary state (Healthy vs. Faulty), RUL treats it as a continuous, dynamic countdown based on historical and real-time wear.
    """)
    
    st.write("")
    st.markdown("#### Why Predicting RUL is Critical?")
    
    # PREMIUM PRESENTATION FIX: Splitting vertical text walls into matching horizontal cards
    why_col1, why_col2, why_col3 = st.columns(3, gap="medium")

    with why_col1:
        with st.container(border=True):
            st.markdown("#### :blue[Aerospace Safety & Risk Mitigation]")
            st.markdown("""
            In aviation, unexpected equipment failure during operation can be catastrophic. Accurately tracking RUL provides a critical, reliable safety window to ground and service an engine before an incident occurs.
            """)
            
    with why_col2:
        with st.container(border=True):
            st.markdown("#### :blue[Optimized Maintenance Economics]")
            st.markdown("""
            Servicing an engine too early wastes millions in perfectly functional hardware lifespan. Servicing it too late causes severe secondary damage and unscheduled operational downtime. RUL estimation targets the optimal economic sweet spot.
            """)
            
    with why_col3:
        with st.container(border=True):
            st.markdown("#### :blue[The Shift to Condition-Based Maintenance]")
            st.markdown("""
            It allows engineering teams to move away from rigid, legacy calendar schedules (e.g., servicing an engine every X months regardless of its actual health) and transition to data-driven maintenance triggered by real-time component stress and wear patterns.
            """)

    img_spacer_left, img_core_col, img_spacer_right = st.columns([1, 2, 1])
    
    with img_core_col:
        # Render the degradation curve asset
        st.image("assets/Asset-Deterioration-Profile@2x.png", use_container_width=True)
        
        # The exact text from your image formatted cleanly with a subtle caption style
        st.markdown("""
        *The distance between $A$ and $B$ is the asset's RUL. This concept is easy enough to understand visually, 
        but in practice, it can become complicated depending on the data and information available on a specific asset.*
        """)

st.write("")

with st.container(border=True):
    st.subheader("🔢 Mathematical Formulation")
    st.markdown("In time-series prognostics, the ground truth Remaining Useful Life (RUL) at a specific flight cycle $t$ is modeled using two primary approaches:")
    
    # 2-Column layout to cleanly separate the two mathematical theories
    form_col1, form_col2 = st.columns(2, gap="medium")
    
    with form_col1:
        with st.container(border=True):
            st.markdown("### :red[1. Standard Linear RUL]")
            st.markdown("The absolute countdown until functional failure. It assumes degradation begins immediately from the very first flight cycle:")
            st.latex(r"RUL_t = t_{fail} - t")
            st.caption("Where $t_{fail}$ is the total operational cycles completed at failure, and $t$ is the current cycle.")
            
    with form_col2:
        with st.container(border=True):
            st.markdown("### :violet[2. Piecewise RUL]")
            st.markdown("Accounts for the reality that a healthy engine does not show signs of physical wear early in its life. The target is capped at an upper threshold ($RUL_{max}$):")
            st.latex(r"RUL_t = \min(RUL_{max}, \, t_{fail} - t)")
            st.caption("This bounds the early-stage target values (commonly set between 125 and 130 cycles) until progressive degradation begins.")

    img_spacer_left, img_core_col, img_spacer_right = st.columns([1, 4, 1])
    
    with img_core_col:
        # Render the degradation curve asset
        st.image("assets\piecewsie_linear_rul.png", width=1000)
        
        left, centre, right = st.columns([1, 1.3, 1])
        with centre:
            st.markdown("""
            *Standard Linear RUL vs Piecewise (Rectified) RUL*
            """)

st.write("")