<p align="left">
  <img src="assets\readme_banner.png" width="80%">
</p>

### 🤓 Overview

Aircraft engine prognostics plays a critical role in predictive maintenance by estimating the Remaining Useful Life (RUL) of an engine before failure. Accurate RUL prediction helps reduce maintenance costs, improve operational safety, and minimize unexpected downtime.

This repository presents a comprehensive benchmark study on RUL prediction using the NASA C-MAPSS turbofan engine dataset. Multiple Machine Learning and Deep Learning models are systematically evaluated across different operating conditions and fault modes to understand their performance under varying degradation scenarios. The benchmark includes experiments for both Linear and Piecewise (Rectified) RUL target formulations, enabling a detailed comparison of modeling approaches on multivariate time series data.

To complement the benchmark, the project also includes an interactive web application that enables users to explore the complete study through an intuitive interface. The application provides an overview of the problem statement, detailed dataset exploration, preprocessing methodology, experimental workflow, benchmark results, and an integrated MLflow dashboard for browsing experiments, comparing models, visualizing metrics, and reviewing logged artifacts.

---

### 🎯 Target Formulations

To provide a comprehensive evaluation of predictive models, the study considers two Remaining Useful Life (RUL) target formulations: **Linear RUL** and **Piecewise (Rectified) RUL**.

**Standard Linear RUL**: The Linear RUL formulation assumes that the remaining useful life decreases linearly from the beginning of an engine's operational cycle until failure. Each cycle is assigned its exact remaining number of cycles, allowing the model to learn the complete degradation trajectory throughout the engine's lifetime. This formulation preserves the full degradation information.

**Piecewise (Rectified) RUL**: In practice, aircraft engines do not begin degrading immediately after entering service. The Piecewise RUL formulation assigns a constant maximum RUL during the healthy operating phase and decreases it linearly only after degradation begins. This allows models to focus on learning the degradation process rather than early-life cycles where little or no meaningful wear is present.

---

### 🌐 Interactive Benchmark Application

To complement the benchmark study, this project includes an interactive web application that provides a centralized platform for exploring the complete turbofan prognostics workflow. Rather than navigating notebooks or source code, users can interactively understand the dataset, methodology, experiments, and benchmark results through an intuitive interface.

**Launch the application:** [Turbofan Prognostics Application](https://turbofan-prognostics.streamlit.app/)

---

### 🤖 Models Evaluated

The benchmark currently includes a diverse collection of Machine Learning and Deep Learning models, all evaluated under a consistent experimental protocol for Remaining Useful Life (RUL) prediction. Model performance is assessed using **R² Score**, **RMSE**, **MAE**, and the **NASA S-Score**. To provide a comprehensive evaluation, results are reported for both **Out-of-Fold (OOF)** predictions obtained through **Group K-Fold cross-validation** and the **held-out test set**, enabling a robust comparison of model generalization across different operating conditions and fault scenarios.


| Machine Learning | Deep Learning |
|:-----------------|:--------------|
| HistGBM | RealMLP |
| XGBoost | TabM |
| LightGBM | ResNet (RTDL) |
| CatBoost | |
| Extra Trees | |

---

### 📊 Running MLflow Experiments

All experiments in this benchmark are tracked using **MLflow**, enabling reproducible experiment management, model versioning, metric comparison, parameter tracking, and artifact visualization.

Launch the MLflow UI: From the project root, start the MLflow tracking server by pointing it to the project's SQLite tracking database:

```bash
mlflow ui --backend-store-uri sqlite:///notebooks/mlflow.db
```

Once the server is running, open your browser and navigate to:

```
http://127.0.0.1:5000
```