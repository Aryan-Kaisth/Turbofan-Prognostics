## Dataset Overview

<p align="left">
  <img src="https://farm3.staticflickr.com/2460/3686365971_12107421e7_o_d.jpg" width="40%">
</p>

The **NASA C-MAPSS (Commercial Modular Aero-Propulsion System Simulation)** dataset is a benchmark dataset for Remaining Useful Life (RUL) prediction and predictive maintenance research. It contains multivariate time-series data collected from simulated turbofan aircraft engines operating under different environmental conditions and fault scenarios.

Each engine is represented as an independent trajectory, where every row corresponds to a single operational cycle. An engine begins in a healthy state and gradually degrades over time until failure. The dataset includes three operational settings and twenty-one sensor measurements recorded at every cycle.

The benchmark is divided into four independent subsets, each with different operating conditions and degradation modes.

| Dataset   | Train Engines | Test Engines | Operating Conditions | Fault Modes                                      |
| :-------- | ------------: | -----------: | -------------------- | ------------------------------------------------ |
| **FD001** |           100 |          100 | One (Sea Level)      | High-Pressure Compressor (HPC) Degradation       |
| **FD002** |           260 |          259 | Six                  | High-Pressure Compressor (HPC) Degradation       |
| **FD003** |           100 |          100 | One (Sea Level)      | High-Pressure Compressor (HPC) & Fan Degradation |
| **FD004** |           248 |          249 | Six                  | High-Pressure Compressor (HPC) & Fan Degradation |

### Training Data

The training set contains complete engine trajectories from the initial operating cycle until system failure. Since the failure cycle is known, the Remaining Useful Life (RUL) for every cycle can be derived directly from the final cycle of each engine.

### Test Data

The test set contains partial engine trajectories that terminate before failure. The objective is to estimate the Remaining Useful Life (RUL) at the final observed cycle of each engine. A separate file containing the ground-truth RUL values is provided for evaluation.

### Data Structure

Each observation consists of **26 columns**, where every row represents a single operational cycle of an engine.

| Columns  | Description              |
| -------- | ------------------------ |
| **1**    | Unit Number (Engine ID)  |
| **2**    | Time Cycles              |
| **3–5**  | Operational Settings (3) |
| **6–26** | Sensor Measurements (21) |

Each engine trajectory therefore forms a multivariate time series describing the engine's degradation process throughout its operational lifetime.