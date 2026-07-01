import streamlit as st
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

ASSETS = BASE_DIR / "assets"

st.set_page_config(
    page_title="RUL Research and Benchmark",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state for interactive navigation
if "active_step" not in st.session_state:
    st.session_state.active_step = "eda"

with st.container(border=True):
    st.subheader("⚙️ Development Workflow")
    st.caption("Click on any phase below to explore the project pipeline and source notebooks.")
    st.write("")
    
    step_col1, step_col2, step_col3, step_col4 = st.columns(4, gap="small")

    with step_col1:
        if st.button(
            "1️⃣ EDA", 
            use_container_width=True, 
            type="primary" if st.session_state.active_step == "eda" else "secondary"
        ):
            st.session_state.active_step = "eda"
            st.rerun()

    with step_col2:
        if st.button(
            "2️⃣ Feature Engineering", 
            use_container_width=True, 
            type="primary" if st.session_state.active_step == "fe" else "secondary"
        ):
            st.session_state.active_step = "fe"
            st.rerun()

    with step_col3:
        if st.button(
            "3️⃣ Modeling", 
            use_container_width=True, 
            type="primary" if st.session_state.active_step == "model" else "secondary"
        ):
            st.session_state.active_step = "model"
            st.rerun()

    with step_col4:
        if st.button(
            "4️⃣ Evaluation", 
            use_container_width=True, 
            type="primary" if st.session_state.active_step == "eval" else "secondary"
        ):
            st.session_state.active_step = "eval"
            st.rerun()

    st.divider()
    
    # PHASE 1
    if st.session_state.active_step == "eda":
        st.markdown("### 📖 :blue[Phase 1: Exploratory Data Analysis]")
        st.write("")
        col_text, col_action = st.columns([5, 2], gap="large")
        
        with col_text:
            st.markdown("A comprehensive exploratory analysis was conducted to understand the NASA C-MAPSS dataset, including univariate, bivariate, and multivariate analysis, sensor behaviour, degradation trends, and statistical relationships. The complete analysis is documented in the accompanying Jupyter Notebook.")
        
        with col_action:
            with st.container(border=True):
                st.caption("📂 Github Repository")
                st.link_button(
                    "📒 EDA Notebook",
                    "https://github.com/Aryan-Kaisth/Turbofan-Prognostics/blob/main/notebooks/01_data_exploration.ipynb",
                    use_container_width=True
                )
        
    # PHASE 2
    elif st.session_state.active_step == "fe":
        st.markdown("### 🛠️ :green[Phase 2: Feature Engineering]")
        st.write("")
        col_text, col_action = st.columns([5, 2], gap="large")
        
        with col_text:
            st.markdown("This phase includes preprocessing, feature creation, feature transformation, and feature selection, providing high-quality inputs for Remaining Useful Life (RUL) prediction. The complete workflow is documented in the accompanying Jupyter Notebook.")
        
        with col_action:
            with st.container(border=True):
                st.caption("📂 Github Repository")
                st.link_button(
                    "📗 Feature Engineering Notebook",
                    "https://github.com/Aryan-Kaisth/Turbofan-Prognostics/blob/main/notebooks/02_feature_engineering.ipynb",
                    use_container_width=True
                )
        
    # PHASE 3
    elif st.session_state.active_step == "model":
        st.markdown("### 👾 :violet[Phase 3: Model Development & Experimentation]")
        st.write("")
        col_text, col_action = st.columns([5, 2], gap="large")
        
        with col_text:
            st.markdown("""
            This phase covers the structural training of our predictive models across both paradigms. 
            We systematically evaluate high-efficiency tabular models (such as CatBoost and Random Forests) 
            against sequential deep learning frameworks (LSTMs and Temporal Convolutional Networks) to capture 
            complex time-series degradation signatures.
            """)
        
        with col_action:
            with st.container(border=True):
                st.caption("📂 Github Repository")
                st.link_button(
                    "📕 Model Development Notebook",
                    "https://github.com/Aryan-Kaisth/Turbofan-Prognostics/blob/main/notebooks/03_model_building.ipynb",
                    use_container_width=True
                )
        
        st.write("")
        
        # Isolated full-width container showcasing the purpose of MLflow tracking runs
        with st.container(border=True):
            st.markdown("### :blue[📈 MLflow Tracking]")
            st.markdown("""
            To maintain structural transparency and total research reproducibility, every model variation is monitored in real-time. 
            This tracking block captures localized hyperparameter weights, comparative evaluation scores between training architectures, 
            and loss convergence boundaries across the execution runs.
            """)
            st.link_button(
                "🧪 Open Live MLflow Server Dashboard",
                "",
                type="secondary"
            )
        
    # PHASE 4
    elif st.session_state.active_step == "eval":
        st.markdown("### 🎯 :orange[Phase 4: Evaluation Metrics & Validation]")
        st.markdown("To measure model performance under both statistical and safety-critical aerospace conditions, we evaluate our predictions using four core metrics:")
        st.write("")
        
        eval_col_left, eval_col_right = st.columns(2, gap="medium")
        
        with eval_col_left:
            with st.container(border=True):
                st.markdown("""
                **:red[NASA S-Score (Asymmetric Penalty Score)]:** The most critical metric for this project. Unlike standard metrics, it is asymmetric—it penalizes late RUL predictions (overestimating remaining life, which causes mid-flight failures) much more severely than early predictions (underestimating remaining life, which just leads to early maintenance).
                """)
            with st.container(border=True):
                st.markdown("""
                **:blue[Root Mean Squared Error (RMSE)]:** Measures the average magnitude of the prediction error. It gives a clear, practical idea of how many flight cycles the model's predictions miss by, on average.
                """)
                
        with eval_col_right:
            with st.container(border=True):
                st.markdown("""
                **:orange[Mean Squared Error (MSE)]:** The foundation for RMSE. Because it squares the errors before averaging them, it heavily penalizes large outlier mistakes, helping us spot models that make occasional catastrophic errors.
                """)
            with st.container(border=True):
                st.markdown("""
                **:green[Adjusted R² (Coefficient of Determination)]:** Measures how well the model explains the variance in engine degradation. Because we are explicitly experimenting with varying feature counts (16 vs. 75 columns), Adjusted R² is crucial because it accounts for the number of predictors used, ensuring that adding more columns actually improves predictive value rather than just inflating the score.
                """)