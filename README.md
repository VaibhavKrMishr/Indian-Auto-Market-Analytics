# Indian Auto Market Analytics 🚗📊

An interactive Business Intelligence dashboard for the Indian four-wheeler market. Built using **Python**, **Streamlit**, and **Statistical Modeling** techniques.

## 📌 Project Overview

This project provides a data-driven look into the Indian automobile industry. I analyzed a dataset of **10,000+ car listings** to identify market trends, engineering trade-offs, and consumer value propositions.

### 🔍 Key Analytical Modules

1. **Exploratory Data Analysis (EDA)**: A deep dive into data health, distribution of price/mileage, and feature correlations.
2. **Brand & Model Dynamics**: Market share analysis and portfolio breakdown for 10 major manufacturers.
3. **Engine CC vs Mileage**: Quantifying the relationship between engine displacement and fuel efficiency across different fuel types.
4. **Maintenance Cost Tracking**: Analyzing service cost trends from 2015 to 2024 to identify which brands are most expensive to maintain.
5. **Value for Money (VFM) Index**: A custom mathematical index I developed to rank cars by balancing performance, economy, and price.
6. **Predictive Modeling (SLR)**: A Simple Linear Regression tool to estimate mileage based on engine size.

## 🛠️ Tech Stack

- **Frontend**: Streamlit (Interactive Dashboard)
- **Data Engineering**: Pandas, NumPy
- **Visualizations**: Seaborn, Matplotlib
- **Statistical Analysis**: SciPy (Linear Regression, Pearson Correlation, Chi-Square)

## 📊 Dataset

I used the **Indian Car Market Dataset** from Kaggle.
- **Link**: [Kaggle Dataset](https://www.kaggle.com/datasets/ak0212/indian-car-market-dataset)
- **Scope**: 10,000 entries across 10 top brands (Maruti, Hyundai, Tata, Honda, etc.)

*Special thanks to Akshay Kumar for providing the dataset.*

## 🚀 How to Run

### The Modern Way (Recommended)
If you have [uv](https://github.com/astral-sh/uv) installed:
```bash
uv sync
uv run streamlit run streamlit_app.py
```

### Standard Pip Fallback
```bash
pip install streamlit pandas numpy matplotlib seaborn scipy
streamlit run streamlit_app.py
```

## 📂 Repository Structure

- `main.py`: The core logic for all 6 analytical modules and the UI.
- `streamlit_app.py`: Minimal entry point to trigger the dashboard.
- `images/`: Original screenshots captured from the live dashboard.
- `data/`: The car market dataset (CSV).

---
*Created as part of my Data Science portfolio by Vaibhav Mishra.*