import streamlit as st
import pandas as pd
import mlflow
import plotly.express as px
from pathlib import Path

# SYSTEM CONFIGURATION
ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / "assets"

st.set_page_config(
    page_title="Benchmark Hub",
    page_icon="📊",
    layout="wide"
)

# Dynamic environment path handling for MLflow database location
DB_PATH = ROOT / "notebooks" / "mlflow.db"
mlflow.set_tracking_uri(f"sqlite:///{DB_PATH.as_posix()}")

st.title("📊 Benchmark Study")
st.caption("Systematic validation engine for Remaining Useful Life (RUL) estimation models.")
st.divider()

# FRAMEWORK OVERVIEW
with st.container(border=True):
    st.subheader("📋 Experimental Framework & Objectives")
    st.markdown("""
    This section presents a systematic comparative evaluation of multiple predictive modelling approaches for Remaining Useful Life (RUL) estimation on the NASA C-MAPSS dataset. Each model was developed and assessed under a consistent experimental framework, ensuring fair comparison through identical data preparation, validation strategies, and evaluation metrics.

    The objective of this benchmarking study is not only to identify the highest-performing model but also to understand the strengths, limitations, and practical trade-offs of different modelling approaches. All experiments were tracked using MLflow to ensure reproducibility, transparency, and objective comparison throughout the development process.
    """)
    st.image(ASSETS / "bench.png", width=500)

st.write("")

# CORE EVALUATION METRICS & VALIDATION FRAMEWORK
with st.container(border=True):
    st.subheader("🎯 Model Validation Criteria")
    st.markdown("""
    To guarantee strict statistical accountability and satisfy safety-critical aerospace constraints, models are cross-evaluated across four core dimensions. This combination ensures that models are optimized for absolute numerical accuracy as well as operational risk mitigation.
    """)
    st.write("")
    
    metric_row1_col1, metric_row1_col2 = st.columns(2, gap="medium")
    metric_row2_col1, metric_row2_col2 = st.columns(2, gap="medium")
    
    with metric_row1_col1:
        with st.container(border=True):
            st.markdown("#### 🚨 :red[NASA S-Score (Asymmetric Penalty)]")
            st.markdown("""
            The primary domain-specific validation constraint. Unlike standard symmetric error equations, it applies an asymmetric exponential penalty to error residuals ($d_i = \hat{y}_i - y_i$). 
            Overestimating RUL (late maintenance triggers causing potential mid-flight engine failure) is penalized significantly harder than underestimating RUL (early maintenance triggers leading to minor economic overhead).
            """)
            st.latex(r"S = \begin{cases} \sum_{i=1}^{N} (e^{-\frac{d_i}{13}} - 1) & \text{for } d_i < 0 \\ \sum_{i=1}^{N} (e^{\frac{d_i}{10}} - 1) & \text{for } d_i \ge 0 \end{cases}")
            
    with metric_row1_col2:
        with st.container(border=True):
            st.markdown("#### 🔵 :blue[R² Score (Coefficient of Determination)]")
            st.markdown("""
            Quantifies the proportion of target variance explained by the underlying model predictions relative to a baseline mean model. 
            It measures how well the model fits the overall shape of the engine degradation curve, serving as a critical indicator of global predictive performance.
            """)
            st.latex(r"R^2 = 1 - \frac{\sum_{i=1}^{N}(y_i - \hat{y}_i)^2}{\sum_{i=1}^{N}(y_i - \bar{y})^2}")
            
    with metric_row2_col1:
        with st.container(border=True):
            st.markdown("#### 🟠 :orange[Root Mean Squared Error (RMSE)]")
            st.markdown("""
            Measures the standard deviation of the prediction residuals, mapping model error back to the original operational flight cycle unit. 
            It offers a direct, clear representation of how many cycles the model's predictions miss by, on average.
            """)
            st.latex(r"RMSE = \sqrt{\frac{1}{N}\sum_{i=1}^{N}(\hat{y}_i - y_i)^2}")
            
    with metric_row2_col2:
        with st.container(border=True):
            st.markdown("#### 🟢 :green[Mean Squared Error (MSE)]")
            st.markdown("""
            The foundational loss engine driving our optimization steps. By squaring the individual error residuals before computing the mean, it amplifies and heavily penalizes large out-of-bounds prediction mistakes, surfacing models susceptible to catastrophic outlier failures.
            """)
            st.latex(r"MSE = \frac{1}{N}\sum_{i=1}^{N}(\hat{y}_i - y_i)^2")

st.write("")

# EXPERIMENT RETRIEVAL ENGINE
def render_experiment_leaderboard(dataset_keyword: str):
    """Queries backend database and renders performance metrics with Plotly charts."""
    try:
        all_experiments = mlflow.search_experiments()
        target_exp_ids = [
            exp.experiment_id for exp in all_experiments 
            if dataset_keyword.lower() in exp.name.lower()
        ]
        
        if target_exp_ids:
            df_runs = mlflow.search_runs(experiment_ids=target_exp_ids)
        else:
            all_exp_ids = [exp.experiment_id for exp in all_experiments]
            df_runs = mlflow.search_runs(
                experiment_ids=all_exp_ids, 
                filter_string=f"attributes.run_name LIKE '%{dataset_keyword}%'"
            )
            
        if df_runs is not None and not df_runs.empty:
            name_col = [c for c in df_runs.columns if 'run_name' in c or 'runName' in c]
            metric_cols = [c for c in df_runs.columns if c.startswith('metrics.')]
            
            df_clean = df_runs[name_col + metric_cols].copy()
            df_clean.columns = [
                c.replace('metrics.', '').replace('run_name', 'Model Configuration').replace('tags.mlflow.runName', 'Model Configuration') 
                for c in df_clean.columns
            ]
            
            st.markdown(f"### 📋 Experiment Runs ({dataset_keyword})")
            st.caption("Comprehensive evaluation metrics pulled directly from logged training histories.")
            st.write("")
            
            st.dataframe(df_clean, hide_index=True, use_container_width=True)
            
            st.write("")
            st.markdown("### 📉 Compare Runs")
            
            available_metrics = [col for col in df_clean.columns if col != 'Model Configuration']
            
            if available_metrics:
                default_idx = available_metrics.index('test_rmse') if 'test_rmse' in available_metrics else 0
                
                selected_metric = st.selectbox(
                    "Select Metric to Plot:",
                    options=available_metrics,
                    index=default_idx,
                    key=f"metric_select_{dataset_keyword}"
                )
                
                st.write("")
                chart_col1, chart_col2 = st.columns(2, gap="large")
                
                with chart_col1:
                    with st.container(border=True):
                        st.markdown(f"##### Bar Chart View ({selected_metric})")
                        
                        fig_bar = px.bar(
                            df_clean,
                            x="Model Configuration",
                            y=selected_metric,
                            color="Model Configuration",
                            template="plotly_dark",
                            labels={selected_metric: selected_metric},
                            color_discrete_sequence=px.colors.qualitative.Pastel
                        )
                        fig_bar.update_layout(
                            xaxis=dict(type="category"),
                            showlegend=False,
                            margin=dict(l=20, r=20, t=20, b=20)
                        )
                        st.plotly_chart(fig_bar, use_container_width=True)
                        
                with chart_col2:
                    with st.container(border=True):
                        st.markdown(f"##### Line Chart View ({selected_metric})")
                        
                        fig_line = px.line(
                            df_clean,
                            x="Model Configuration",
                            y=selected_metric,
                            markers=True,
                            template="plotly_dark"
                        )
                        fig_line.update_traces(line=dict(color="#FF4B4B", width=3), marker=dict(size=8, color="#FFFFFF"))
                        fig_line.update_layout(
                            xaxis=dict(type="category"),
                            margin=dict(l=20, r=20, t=20, b=20)
                        )
                        st.plotly_chart(fig_line, use_container_width=True)
                
                st.write("")
                with st.container(border=True):
                    st.markdown("##### Scatter Plot View")
                    st.caption("Analyze correlation boundaries and coordinate trade-offs between two target evaluation dimensions.")
                    st.write("")
                    
                    if len(available_metrics) >= 2:
                        scat_param_col1, scat_param_col2 = st.columns(2)
                        with scat_param_col1:
                            x_axis_metric = st.selectbox(
                                "Horizontal Axis (X):", 
                                options=available_metrics, 
                                index=default_idx,
                                key=f"x_scat_{dataset_keyword}"
                            )
                        with scat_param_col2:
                            y_axis_metric = st.selectbox(
                                "Vertical Axis (Y):", 
                                options=available_metrics, 
                                index=default_idx,
                                key=f"y_scat_{dataset_keyword}"
                            )
                        
                        fig_scatter = px.scatter(
                            df_clean,
                            x=x_axis_metric,
                            y=y_axis_metric,
                            color="Model Configuration",
                            hover_name="Model Configuration",
                            template="plotly_dark",
                            labels={x_axis_metric: x_axis_metric, y_axis_metric: y_axis_metric},
                            color_discrete_sequence=px.colors.qualitative.Safe
                        )
                        fig_scatter.update_traces(marker=dict(size=14, line=dict(width=1, color='White')))
                        fig_scatter.update_layout(
                            margin=dict(l=20, r=20, t=20, b=20),
                            height=380 
                        )
                        st.plotly_chart(fig_scatter, use_container_width=True)
                    else:
                        st.info("Multi-metric coordinate charting requires at least two distinct logged run metrics.")
            else:
                st.warning("No numeric evaluation metrics are available in the current run logs to plot.")
            
        else:
            st.info(f"No experimental records or metrics matched target configuration: {dataset_keyword}")
            
    except Exception as e:
        st.error(f"Metadata Retrieval Pipeline Failure: {e}")
        st.caption("Verify tracking environment file-system read permissions to the target database instance.")

# CORE WORKSPACE NAVIGATION
tab_fd001, tab_fd003 = st.tabs([
    "✈️ FD001 (Sea Level / Single Fault)",
    "✈️ FD003 (Sea Level / Dual Fault)"
])

# SUB-DATASET HUB: FD001
with tab_fd001:
    st.write("")
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
    
    fd001_ml, fd001_dl, fd001_exp = st.tabs(["⚙️ Machine Learning", "🧠 Deep Learning", "🔄 MLflow Experiments"])
    
    with fd001_ml:
        st.write("")
        st.markdown("""
        * **HistGBM**
        * **ExtraTrees**
        * **CatBoost**
        * **XGBoost**
        * **LightGBM**
        """)
        
    with fd001_dl:
        st.write("")
        st.markdown("""
        * **TabM**
        * **RealMLP**
        * **ResNet**
        """)
        
    with fd001_exp:
        st.write("")
        render_experiment_leaderboard("FD001")

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
    
    fd003_ml, fd003_dl, fd003_exp = st.tabs(["⚙️ Machine Learning", "🧠 Deep Learning", "🔄 MLflow Experiments"])
    
    with fd003_ml:
        st.write("")
        st.markdown("""
        * **HistGBM**
        * **ExtraTrees**
        * **CatBoost**
        * **XGBoost**
        * **LightGBM**
        """)
        
    with fd003_dl:
        st.write("")
        st.markdown("""
        * **TabM**
        * **RealMLP**
        * **ResNet**
        """)
        
    with fd003_exp:
        st.write("")
        render_experiment_leaderboard("FD003")