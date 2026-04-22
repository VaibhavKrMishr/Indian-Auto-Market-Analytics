# Indian Auto Market Analytics 🚗📊

This is my academic project for analyzing the Indian car market. I built an interactive dashboard using Python and Streamlit to explore a dataset of 10,000+ car listings.

## Project Description

I wanted to see how different factors like engine size (CC) affect mileage and which brands offer the best value for money in India. The dashboard has 6 main parts ranging from simple brand breakdowns to a linear regression model for predicting fuel efficiency.

## Key Features

- **EDA Home Page**: Data health check, basic distributions, and correlation heatmap.
- **Brand & Model Analysis**: Breakdown of sales volume and model variety.
- **Engine CC vs Mileage**: Visualizing the engineering trade-off.
- **Service Costs**: Tracking maintenance trends from 2015 to 2024.
- **Value for Money**: A custom ranking index I built to find the best deals.
- **Mileage Prediction**: Simple Linear Regression tool to estimate kmpl from engine size.

## Dataset Info

I used the **Indian Car Market Dataset** from Kaggle.
- **Link**: [Kaggle Dataset](https://www.kaggle.com/datasets/ak0212/indian-car-market-dataset)
- **Size**: 10,000 entries
- **Details**: Covers 10 brands, 4 fuel types, and 10 years of data.

*Special thanks to Akshay Kumar for providing the dataset.*

## How to Run

1. Install requirements:
   ```bash
   pip install streamlit pandas numpy matplotlib seaborn scipy
   ```
2. Run the app:
   ```bash
   streamlit run streamlit_app.py
   ```

## Files in this Repo

- `main.py`: Core dashboard logic (Python/Streamlit).
- `streamlit_app.py`: Entry point script.
- `generate_report.py`: Script to generate the full academic report (`.docx`).
- `report.md`: Technical documentation of the analysis.
- `images/`: Original screenshots captured from the dashboard.

---
*Created as part of my Data Science portfolio.*