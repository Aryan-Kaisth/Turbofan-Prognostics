import streamlit as st

st.set_page_config(
    page_title="RUL Research and Benchmark",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

_, banner_col, _ = st.columns([1, 5, 1])
with banner_col:
    st.image('assets\Video Project.gif', use_container_width=True)

st.title("Turbofan-Prognostics")
st.caption("Aircraft engine degradation modeling and Remaining Useful Life (RUL) prediction using multivariate sensor time-series from the NASA C-MAPSS benchmark.")

st.markdown("---")

with st.container(border=True):
    st.subheader("💡 What is Remaining Useful Life (RUL)?")
    
    st.markdown("""
    Remaining Useful Life (RUL) refers to the estimated amount of operational life remaining before a machine reaches a predefined failure threshold or is no longer able to perform its intended function reliably. 
    Rather than focusing only on whether a machine is healthy or faulty, RUL provides an estimate of **how much useful life remains** based on its current operating condition.
    
    ### But Why?
    Every mechanical system undergoes gradual degradation throughout its lifetime. Continuous exposure to factors such as friction, thermal stress, pressure variations, material fatigue, and vibration slowly affects the condition of internal components. 
    This degradation is progressive, meaning the machine rarely transitions from a healthy state to complete failure without exhibiting measurable changes in its behavior.
    Modern industrial equipment is equipped with numerous sensors that continuously monitor these changes. As components wear, sensor measurements begin to deviate from their normal operating patterns, providing valuable insights into the health of the system. 
    By analyzing these degradation patterns, it becomes possible to estimate the remaining operational life of the equipment before failure occurs.
    """)

st.write("") 

with st.container(border=True):
    st.subheader("Introducing TurboFan Prognostics")
    
    st.markdown("""
    **TurboFan Prognostics** is a comprehensive machine learning benchmark and research project focused on predicting the **Remaining Useful Life (RUL)** of aircraft turbofan engines using the NASA C-MAPSS benchmark dataset. 
    The primary objective of this project is to systematically investigate how different predictive modelling approaches perform in estimating engine degradation while developing a deeper understanding of the data, the underlying degradation process, and the challenges associated with RUL prediction.
    """)
    
    st.write("")