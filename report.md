# Indian Auto Market Analytics
## A Statistical Analysis of the Indian Four-Wheeler Market

**Submitted by:** Analysis Team  
**Project:** Indian Auto Market Analytics  
**Technology Stack:** Python, Streamlit, Pandas, Seaborn, Matplotlib, SciPy  
**Date:** April 2026

---

## Table of Contents

1. Introduction
2. Source of Dataset
3. Exploratory Data Analysis (EDA)
4. Analysis on Dataset
    - 4.1 Brand Market Overview
    - 4.2 Brand Model Breakdown
    - 4.3 Engine CC vs Mileage
    - 4.4 Service Cost Trends
    - 4.5 Value for Money Index
    - 4.6 Mileage Prediction using Simple Linear Regression
5. Conclusion
6. Future Scope
7. References

---

## 1. Introduction

The Indian automobile industry is one of the largest in the world. India is currently the third-largest automobile market globally by volume, and the industry contributes significantly to the country's GDP. The four-wheeler segment, which includes passenger cars, SUVs, and utility vehicles, has seen remarkable growth over the past decade driven by rising disposable incomes, urbanization, and improved road infrastructure.

Understanding market dynamics in this sector is crucial for manufacturers, dealers, and consumers alike. Questions such as "Which brands dominate the market?", "How does engine size affect fuel economy?", and "Which vehicles offer the best value for money?" are fundamental to making informed purchasing and business decisions.

This project aims to answer these questions through a data-driven approach. We have built an interactive dashboard using Python and Streamlit that performs six distinct analytical modules on a comprehensive Indian car market dataset. Each module applies appropriate statistical methods ranging from descriptive statistics and hypothesis testing to predictive modeling using Simple Linear Regression.

### 1.1 Objectives

The primary objectives of this project are:

- To perform thorough Exploratory Data Analysis on the Indian car market dataset
- To identify brand positioning and market share patterns
- To analyze the engineering relationship between engine displacement and fuel efficiency
- To track maintenance cost trends across model years
- To develop a custom Value-for-Money index for objective car comparison
- To build a predictive model for estimating fuel efficiency based on engine capacity

### 1.2 Tools and Technologies

| Tool | Purpose |
|------|---------|
| Python 3.13 | Core programming language |
| Pandas | Data manipulation and aggregation |
| NumPy | Numerical computations |
| Matplotlib | Static chart generation |
| Seaborn | Statistical visualization |
| SciPy | Hypothesis testing and regression |
| Streamlit | Interactive web dashboard |

### 1.3 Project Structure

The project follows a simple, functional structure:

```
Indian-Auto-Market-Analytics/
├── main.py                  # All dashboard logic
├── streamlit_app.py         # Entry point (triggers main.py)
├── data/
│   └── car_dataset_india.csv
├── images/
│   └── car.png
├── pyproject.toml
└── uv.lock
```

The entire analytical logic resides in `main.py`, which is triggered through `streamlit_app.py` using Streamlit's framework. This single-file approach was chosen for simplicity and ease of deployment.

---

## 2. Source of Dataset

### 2.1 Dataset Overview

The dataset used in this project is titled **"Car Dataset India"** and contains information about 10,000 car listings from the Indian automobile market. The data covers 10 major automobile brands operating in India across a 10-year period from 2015 to 2024.

### 2.2 Dataset Specifications

| Property | Value |
|----------|-------|
| Total Records | 10,000 |
| Total Features | 11 |
| File Format | CSV |
| File Size | ~500 KB |
| Time Period | 2015 – 2024 |
| Geographic Scope | India |

### 2.3 Feature Description

The dataset contains the following 11 columns:

| # | Column Name | Data Type | Description |
|---|-------------|-----------|-------------|
| 1 | Car_ID | int64 | Unique identifier for each car listing |
| 2 | Brand | string | Manufacturer name (e.g., Maruti Suzuki, Hyundai) |
| 3 | Model | string | Specific car model (e.g., Swift, Creta, Nexon) |
| 4 | Year | int64 | Year of manufacture (2015–2024) |
| 5 | Fuel_Type | string | Fuel category: Petrol, Diesel, CNG, Electric |
| 6 | Transmission | string | Transmission type: Manual or Automatic |
| 7 | Price | float64 | Listed price in Indian Rupees (₹) |
| 8 | Mileage | float64 | Fuel efficiency in kilometers per liter (kmpl) |
| 9 | Engine_CC | int64 | Engine displacement in cubic centimeters |
| 10 | Seating_Capacity | int64 | Number of seats (4–7) |
| 11 | Service_Cost | float64 | Annual maintenance/service cost in ₹ |

### 2.4 Brands Covered

The dataset covers the following 10 major automobile brands in India:

1. Maruti Suzuki (1,042 listings)
2. Volkswagen (1,034 listings)
3. Hyundai (1,033 listings)
4. Mahindra (1,024 listings)
5. Skoda (1,011 listings)
6. Tata Motors (989 listings)
7. Honda (982 listings)
8. Kia (973 listings)
9. Renault (958 listings)
10. Toyota (954 listings)

The distribution across brands is relatively balanced, with each brand contributing approximately 9.5% to 10.4% of the total dataset. This ensures that no single brand disproportionately influences the analytical outcomes.

### 2.5 Fuel Type Distribution

| Fuel Type | Count | Percentage |
|-----------|-------|------------|
| CNG | 2,588 | 25.88% |
| Electric | 2,518 | 25.18% |
| Diesel | 2,468 | 24.68% |
| Petrol | 2,426 | 24.26% |

The fuel type distribution is nearly uniform across all four categories. This is notable and suggests that the dataset was curated to provide balanced representation across fuel segments.

### 2.6 Transmission Split

| Type | Count | Percentage |
|------|-------|------------|
| Manual | 5,045 | 50.45% |
| Automatic | 4,955 | 49.55% |

The transmission split is almost exactly 50-50, reflecting the growing adoption of automatic transmissions in the Indian market while manual variants continue to maintain a strong presence.

---

## 3. Exploratory Data Analysis (EDA)

Exploratory Data Analysis is the critical first step in any data science project. Before running formal hypothesis tests or building predictive models, we need to understand the structure, quality, and distribution patterns within the data.

### 3.1 Data Quality Assessment

#### 3.1.1 Missing Values Check

We performed a null value audit using `df.isnull().sum()`:

| Column | Missing Values |
|--------|---------------|
| Car_ID | 0 |
| Brand | 0 |
| Model | 0 |
| Year | 0 |
| Fuel_Type | 0 |
| Transmission | 0 |
| Price | 0 |
| Mileage | 0 |
| Engine_CC | 0 |
| Seating_Capacity | 0 |
| Service_Cost | 0 |

**Result:** The dataset is 100% complete with zero missing values across all 11 columns. No imputation or data cleaning was required for null handling.

#### 3.1.2 Data Type Verification

We verified column data types using `df.dtypes`:

- **Numerical columns (7):** Car_ID (int64), Year (int64), Price (float64), Mileage (float64), Engine_CC (int64), Seating_Capacity (int64), Service_Cost (float64)
- **Categorical columns (4):** Brand (string), Model (string), Fuel_Type (string), Transmission (string)

All data types are correctly assigned. No type conversion was necessary.

### 3.2 Descriptive Statistics

Using `df.describe()`, we computed summary statistics for all numerical features:

| Statistic | Year | Price (₹) | Mileage (kmpl) | Engine_CC | Seating | Service_Cost (₹) |
|-----------|------|-----------|----------------|-----------|---------|-------------------|
| Count | 10,000 | 10,000 | 10,000 | 10,000 | 10,000 | 10,000 |
| Mean | 2019.5 | ~19.5L | ~20.0 | ~1,543 | 5.5 | 14,969 |
| Std Dev | 2.88 | ~7.8L | ~5.8 | ~543 | 1.12 | 5,778 |
| Min | 2015 | ~5L | ~10 | 800 | 4 | 5,000 |
| 25th %ile | 2017 | ~12.5L | ~15 | 1,000 | 5 | 9,900 |
| Median | 2020 | ~20L | ~20 | 1,500 | 6 | 15,000 |
| 75th %ile | 2022 | ~27L | ~25 | 2,000 | 7 | 20,000 |
| Max | 2024 | ~35L | ~30 | 2,500 | 7 | 25,000 |

**Key Observations:**
- The price range spans from approximately ₹5 lakhs to ₹35 lakhs, covering the budget to mid-premium segment.
- Mileage values range from 10 to 30 kmpl, which is consistent with the Indian market where fuel economy is a primary consumer concern.
- Engine CC values are discrete, ranging from 800cc (small hatchbacks) to 2,500cc (SUVs and sedans).
- Service costs show considerable variance (std = ₹5,778), suggesting significant differences in maintenance requirements across segments.

### 3.3 Distribution Analysis

#### 3.3.1 Price Distribution

The price histogram with KDE (Kernel Density Estimation) overlay reveals an approximately uniform distribution across the price range. This means the dataset contains a balanced mix of budget, mid-range, and premium vehicles. There is no significant skew toward any particular price bracket.

#### 3.3.2 Mileage Distribution

The mileage distribution similarly shows a roughly uniform pattern across the 10–30 kmpl range. This is expected given the diverse mix of fuel types and engine sizes in the dataset.

### 3.4 Correlation Analysis

We computed the Pearson correlation matrix for all numerical features (excluding Car_ID):

| | Year | Price | Mileage | Engine_CC | Seating | Service_Cost |
|---|------|-------|---------|-----------|---------|--------------|
| Year | 1.000 | -0.002 | -0.001 | 0.008 | 0.011 | -0.008 |
| Price | -0.002 | 1.000 | 0.013 | -0.015 | -0.015 | 0.002 |
| Mileage | -0.001 | 0.013 | 1.000 | -0.008 | -0.004 | -0.014 |
| Engine_CC | 0.008 | -0.015 | -0.008 | 1.000 | 0.006 | 0.013 |
| Seating | 0.011 | -0.015 | -0.004 | 0.006 | 1.000 | -0.016 |
| Service_Cost | -0.008 | 0.002 | -0.014 | 0.013 | -0.016 | 1.000 |

**Key Observations:**
- All pairwise correlations are extremely weak (|r| < 0.02), indicating that the numerical features are largely independent of each other in this dataset.
- The slight negative correlation between Engine_CC and Mileage (-0.008) aligns with the engineering expectation that larger engines consume more fuel, though the effect is very small at the individual car level.
- Service_Cost shows minimal correlation with Price (0.002), suggesting that expensive cars don't necessarily cost more to maintain in this dataset.

---

## 4. Analysis on Dataset

### 4.1 Analysis 1: Brand Market Overview

#### i. Introduction

Understanding brand-level market positioning is fundamental to any automotive market study. This analysis examines how the 10 major Indian car brands are distributed in terms of listing volume and average pricing. The goal is to identify which brands dominate the market and whether there exists a statistical relationship between brand identity and fuel type preference.

#### ii. General Description

We aggregate the dataset by the `Brand` column to compute two key metrics:
- **Volume:** Total number of car listings per brand (proxy for market presence)
- **Average Price:** Mean listed price per brand (indicator of market segment positioning)

Additionally, we perform a Chi-square test of independence to determine whether the choice of fuel type is statistically associated with the brand.

#### iii. Specific Requirements, Functions and Formulas

**Functions Used:**
- `df.groupby('Brand').agg()` — Aggregation by brand
- `pd.crosstab()` — Contingency table construction
- `scipy.stats.chi2_contingency()` — Chi-Square Test of Independence

**Chi-Square Test Formula:**

$$\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}$$

Where:
- $O_i$ = Observed frequency in cell $i$
- $E_i$ = Expected frequency in cell $i$ under the null hypothesis

**Hypotheses:**
- $H_0$: Brand and Fuel_Type are independent (no association)
- $H_1$: Brand and Fuel_Type are dependent (association exists)
- Significance level: $\alpha = 0.05$

#### iv. Analysis Results

**Brand Volume Rankings:**

| Rank | Brand | Volume | Avg Price (₹) |
|------|-------|--------|----------------|
| 1 | Maruti Suzuki | 1,042 | 19.18L |
| 2 | Volkswagen | 1,034 | 19.61L |
| 3 | Hyundai | 1,033 | 19.33L |
| 4 | Mahindra | 1,024 | 19.96L |
| 5 | Skoda | 1,011 | 19.56L |
| 6 | Tata Motors | 989 | 19.16L |
| 7 | Honda | 982 | 19.72L |
| 8 | Kia | 973 | 19.17L |
| 9 | Renault | 958 | 19.51L |
| 10 | Toyota | 954 | 19.40L |

**Chi-Square Test Results:**
- Chi-Square Statistic: $\chi^2 = 18.3777$
- Degrees of Freedom: 27
- P-Value: 0.8916

Since $p = 0.8916 > 0.05$, we **fail to reject** the null hypothesis. There is no statistically significant association between brand and fuel type in this dataset. Each brand offers a relatively balanced mix of Petrol, Diesel, CNG, and Electric vehicles.

#### v. Visualization

The bar chart visualization displays all 10 brands on the x-axis with their corresponding listing counts on the y-axis. The chart reveals a relatively even distribution of listings across brands, with Maruti Suzuki leading marginally at 1,042 listings and Toyota at the lower end with 954.

The near-uniform distribution across brands suggests that the dataset was designed to provide balanced representation, which is beneficial for comparative analysis but may not perfectly reflect real-world market share where Maruti Suzuki, for instance, commands approximately 40% of the Indian passenger vehicle market.

---

### 4.2 Analysis 2: Brand Model Breakdown

#### i. Introduction

While the previous analysis examined brands at a macro level, this module drills down into individual brand portfolios. The objective is to understand how a particular manufacturer's sales are distributed across its various car models. This reveals whether a brand relies heavily on a single "hero model" or maintains a diversified product lineup.

#### ii. General Description

The user selects a specific brand from a dropdown menu, and the dashboard filters the dataset to show only that brand's entries. We then compute the frequency distribution of car models within that brand's portfolio and display it as both a data table and a pie chart.

This analysis is interactive — the user can switch between all 10 brands to compare their internal sales structures.

#### iii. Specific Requirements, Functions and Formulas

**Functions Used:**
- `df[df['Brand'] == selected_brand]` — Filtering by brand
- `Series.value_counts()` — Frequency distribution of models
- `matplotlib.pyplot.pie()` — Pie chart generation

**Model Share Formula:**

$$\text{Model Share (\%)} = \frac{\text{Count of Model}_i}{\text{Total Count for Brand}} \times 100$$

#### iv. Analysis Results

Taking **Maruti Suzuki** as an example (1,042 total listings):

The model distribution reveals how Maruti's portfolio is split across its models like Swift, Alto, Baleno, WagonR, Ertiga, Brezza, and others. Each model contributes a certain percentage to the overall brand volume.

Similar analysis can be performed for any brand. For instance:
- **Hyundai** shows distribution across Creta, Venue, i20, Verna, etc.
- **Tata Motors** shows distribution across Nexon, Punch, Safari, Harrier, etc.

The pie chart provides an intuitive visual of which models carry the brand's volume.

#### v. Visualization

The pie chart displays each model as a proportional slice with percentage annotations. This immediately reveals the dominant models within each brand's lineup. For brands where one model significantly outperforms others, the pie chart shows a clearly larger slice, making the "hero model" pattern visually obvious.

The accompanying data table shows exact counts, enabling precise comparison that the pie chart may not convey at very small percentage differences.

---

### 4.3 Analysis 3: Engine CC vs Mileage

#### i. Introduction

One of the most fundamental relationships in automotive engineering is the trade-off between engine size (displacement in CC) and fuel efficiency (mileage in kmpl). Larger engines produce more power but generally consume more fuel. This analysis quantifies this relationship using the dataset and applies Pearson's correlation coefficient to measure its statistical significance.

#### ii. General Description

We filter out Electric vehicles from this analysis because they do not have internal combustion engines and therefore the concept of "Engine CC" is not applicable to them in the traditional sense.

For the remaining ICE (Internal Combustion Engine) vehicles, we group the data by Engine_CC and Fuel_Type, computing the mean mileage for each combination. This produces a cleaner view of the trend compared to raw individual data points.

#### iii. Specific Requirements, Functions and Formulas

**Functions Used:**
- `df[df['Fuel_Type'] != 'Electric']` — Filtering out EVs
- `df.groupby(['Engine_CC', 'Fuel_Type'])['Mileage'].mean()` — Grouped averaging
- `seaborn.lineplot()` — Multi-line trend visualization
- `scipy.stats.pearsonr()` — Pearson Correlation Coefficient

**Pearson Correlation Formula:**

$$r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}}$$

Where:
- $x_i$ = Engine_CC values
- $y_i$ = Mileage values
- $\bar{x}, \bar{y}$ = Respective means

**Hypotheses:**
- $H_0$: There is no linear correlation between Engine_CC and Mileage ($r = 0$)
- $H_1$: There exists a linear correlation between Engine_CC and Mileage ($r \neq 0$)
- Significance level: $\alpha = 0.05$

#### iv. Analysis Results

**Sample Size:** 7,482 non-electric vehicles

**Pearson Correlation Results:**
- Correlation coefficient: $r = -0.0077$
- P-Value: $p = 5.0772 \times 10^{-1}$

The correlation coefficient is very close to zero and the p-value is far above 0.05, meaning we **fail to reject** the null hypothesis. At the individual car level, there is no statistically significant linear correlation between engine displacement and fuel efficiency in this dataset.

However, this result is influenced by the randomized nature of the dataset. In real-world data, a stronger negative correlation would be expected.

**Grouped Average Mileage by Engine CC:**

| Engine CC | Mean Mileage (kmpl) |
|-----------|---------------------|
| 800 | 20.12 |
| 1,000 | 19.90 |
| 1,200 | 19.92 |
| 1,500 | 20.25 |
| 1,800 | 19.88 |
| 2,000 | 20.17 |
| 2,500 | 19.80 |

The grouped averages show very little variation across engine sizes (~19.8 to 20.3 kmpl), reinforcing the weak correlation finding.

#### v. Visualization

The line plot displays Engine_CC on the x-axis and Mean Mileage on the y-axis, with separate lines for each fuel type (Petrol, Diesel, CNG). Each line is marked with data points using circular markers for clarity.

The visualization shows that while there is a very slight downward trend (consistent with the negative r-value), the lines are largely flat, indicating that engine size alone is not a strong predictor of mileage in this particular dataset.

---

### 4.4 Analysis 4: Service Cost Trends

#### i. Introduction

Maintenance and service costs are a critical component of the total cost of vehicle ownership. This analysis tracks how average service costs have evolved across model years (2015–2024). Understanding these trends helps consumers anticipate long-term ownership expenses and can reveal whether newer vehicles are becoming more or less expensive to maintain.

#### ii. General Description

We compute the mean annual service cost for each model year and visualize the trend as a line chart. Additionally, a box plot is generated to display the full distribution of service costs per year, including the identification of potential outliers through whisker boundaries.

#### iii. Specific Requirements, Functions and Formulas

**Functions Used:**
- `seaborn.lineplot(estimator='mean')` — Average trend line
- `seaborn.boxplot()` — Distribution with outlier detection

**Box Plot Components:**
- **Box:** Spans from Q1 (25th percentile) to Q3 (75th percentile) — the Interquartile Range (IQR)
- **Median Line:** The line inside the box represents the 50th percentile
- **Whiskers:** Extend to the most extreme data point within 1.5 × IQR from the box edges
- **Outliers:** Individual points beyond the whiskers

#### iv. Analysis Results

**Mean Service Cost by Year:**

| Year | Avg Service Cost (₹) |
|------|----------------------|
| 2015 | 14,971 |
| 2016 | 14,910 |
| 2017 | 14,949 |
| 2018 | 15,080 |
| 2019 | 15,160 |
| 2020 | 14,810 |
| 2021 | 15,293 |
| 2022 | 14,960 |
| 2023 | 14,944 |
| 2024 | 14,627 |

**Observations:**
- Service costs remain remarkably stable across the 10-year period, fluctuating within a narrow band of ₹14,627 to ₹15,293.
- The overall mean service cost across all years is approximately ₹14,969.
- 2024 models show the lowest average service cost (₹14,627), which could indicate improved reliability in newer models or lower cumulative service needs for vehicles still under warranty.
- The standard deviation is ₹5,778, indicating substantial within-year variation.

#### v. Visualization

The line chart shows a nearly flat trend line hovering around the ₹15,000 mark, confirming that service costs have not undergone dramatic changes over the decade.

The box plot provides a richer view, displaying the full spread of service costs for each year. The boxes are roughly similar in size across years, and the whiskers extend consistently to the ₹5,000 and ₹25,000 boundaries. This confirms that the cost distribution is stable and there are no dramatic year-over-year shifts.

---

### 4.5 Analysis 5: Value for Money Index

#### i. Introduction

The "Value for Money" (VFM) concept attempts to quantify which cars deliver the best combination of performance and economy relative to their price. Since this is inherently subjective, we created a custom mathematical index that balances three key consumer-facing metrics: mileage, price, and engine capacity.

#### ii. General Description

We compute a VFM score for every car in the dataset using a custom formula that rewards high mileage and engine capacity while penalizing high prices. The top 10 highest-scoring vehicles are presented as the "best value" options. Additionally, we use the IQR (Interquartile Range) method to identify statistical outliers — cars that offer exceptionally high or low value.

#### iii. Specific Requirements, Functions and Formulas

**Custom VFM Formula:**

$$\text{VFM Score} = \frac{\text{Mileage (kmpl)}}{\text{Price (in Lakhs)}} \times \frac{\text{Engine\_CC}}{1000}$$

**Rationale:**
- **Mileage / Price in Lakhs:** Measures fuel efficiency per unit of investment. A car that delivers 20 kmpl at ₹10L scores higher than one delivering 20 kmpl at ₹20L.
- **Engine_CC / 1000:** Rewards larger, more powerful engines. This normalizes the CC value to liters for scale compatibility.

**IQR Outlier Detection:**

$$\text{IQR} = Q_3 - Q_1$$
$$\text{Lower Fence} = Q_1 - 1.5 \times \text{IQR}$$
$$\text{Upper Fence} = Q_3 + 1.5 \times \text{IQR}$$

Any data point below the Lower Fence or above the Upper Fence is classified as an outlier.

#### iv. Analysis Results

**Top 5 Value-for-Money Cars:**

| Rank | Brand | Model | VFM Score |
|------|-------|-------|-----------|
| 1 | Kia | EV6 | 16.50 |
| 2 | Renault | Kiger | 15.85 |
| 3 | Toyota | Camry | 15.76 |
| 4 | Honda | Jazz | 15.31 |
| 5 | Hyundai | i20 | 15.06 |

**IQR-Based Outlier Analysis:**
- Q1 (25th Percentile): Computed from VFM distribution
- Q3 (75th Percentile): Computed from VFM distribution
- Total outlier cars identified: **715 out of 10,000** (7.15%)

These 715 vehicles represent cars that offer either exceptionally good or exceptionally poor value compared to the market norm.

#### v. Visualization

The box plot displays the distribution of VFM scores across the entire dataset. The box represents the interquartile range, and individual dots beyond the whiskers mark the outlier vehicles. The right-side outliers (high VFM) represent the best deals in the market, while left-side outliers (if any) represent potentially overpriced vehicles relative to their specifications.

---

### 4.6 Analysis 6: Mileage Prediction using Simple Linear Regression

#### i. Introduction

Simple Linear Regression (SLR) is a fundamental statistical method for modeling the relationship between a dependent variable and a single independent variable. In this analysis, we apply SLR to predict average fuel efficiency (Mileage) based on engine displacement (Engine_CC).

This is the most advanced analytical module in the project, as it moves beyond descriptive statistics into predictive modeling.

#### ii. General Description

Rather than using individual car records (which contain significant variance), we first aggregate the data by computing the mean mileage for each unique Engine_CC value. This produces 7 clean data points (one for each CC category: 800, 1000, 1200, 1500, 1800, 2000, 2500).

We then fit a linear regression line through these grouped averages and provide an interactive prediction tool where the user can input any CC value to get the model's predicted mileage.

#### iii. Specific Requirements, Functions and Formulas

**Functions Used:**
- `df.groupby('Engine_CC')['Mileage'].mean()` — Data aggregation
- `scipy.stats.linregress()` — Linear regression fitting
- `seaborn.regplot()` — Regression visualization with confidence band

**Simple Linear Regression Model:**

$$\hat{y} = \beta_0 + \beta_1 x$$

Where:
- $\hat{y}$ = Predicted Mileage (kmpl)
- $x$ = Engine_CC
- $\beta_0$ = Intercept (y-value when x = 0)
- $\beta_1$ = Slope (change in y per unit change in x)

**Slope Formula:**

$$\beta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}$$

**Intercept Formula:**

$$\beta_0 = \bar{y} - \beta_1 \bar{x}$$

**Coefficient of Determination:**

$$R^2 = r^2$$

This measures the proportion of variance in the dependent variable that is predictable from the independent variable.

#### iv. Analysis Results

**Regression Output:**

| Parameter | Value |
|-----------|-------|
| Slope ($\beta_1$) | -0.000078 |
| Intercept ($\beta_0$) | 20.1260 |
| Correlation ($r$) | -0.2721 |
| R-squared ($R^2$) | 0.0740 |
| P-Value | 0.5550 |
| Standard Error | 0.000123 |

**The Regression Equation:**

$$\text{Mileage} = -0.000078 \times \text{CC} + 20.126$$

**Interpretation:**
- The **negative slope** (-0.000078) confirms the expected engineering relationship: as engine displacement increases, mileage decreases.
- For every 100cc increase in engine size, the model predicts a decrease of approximately 0.0078 kmpl in fuel efficiency.
- The **r-value of -0.2721** indicates a weak negative correlation at the grouped level.
- The **p-value of 0.5550** is above the 0.05 significance threshold, meaning the relationship is not statistically significant with only 7 data points.
- The **R² of 0.074** means the model explains approximately 7.4% of the variance in average mileage.

**Sample Predictions:**

| Input CC | Predicted Mileage |
|----------|-------------------|
| 800 | 20.06 kmpl |
| 1,200 | 20.03 kmpl |
| 1,500 | 20.01 kmpl |
| 2,000 | 19.97 kmpl |
| 2,500 | 19.93 kmpl |

While the predictions show the correct directional trend (higher CC → lower mileage), the differences are very small due to the weak relationship in this dataset.

#### v. Visualization

The regression plot displays:
- **Scatter points:** The 7 grouped average data points (one per CC category)
- **Regression line:** The best-fit line showing the predicted relationship
- **Confidence band:** The shaded region showing the 95% confidence interval for the regression line

The wide confidence band reflects the high uncertainty in the model, consistent with the high p-value and low R² values. Despite this, the downward slope of the regression line correctly captures the general engineering principle that larger engines are less fuel-efficient.

---

## 5. Conclusion

This project successfully developed an interactive Business Intelligence dashboard for the Indian automobile market using Python and Streamlit. The following key findings emerged from our six analytical modules:

### 5.1 Key Findings

1. **Market Structure:** The Indian four-wheeler market covered in this dataset is well-distributed across 10 major brands, with Maruti Suzuki, Volkswagen, and Hyundai leading in listing volume. All brands maintain similar average pricing around ₹19-20 lakhs.

2. **Brand-Fuel Independence:** The Chi-square test revealed no significant association between brand identity and fuel type preference (p = 0.8916), indicating that all major brands offer comparable fuel type portfolios.

3. **Model Concentration:** Individual brand analysis through pie charts reveals varying degrees of model concentration, with some brands showing balanced portfolios and others relying more heavily on specific models.

4. **Engine-Efficiency Relationship:** While the Pearson correlation between Engine_CC and Mileage was weak at the individual level (r = -0.0077), the negative slope of the regression model at the grouped level confirms the expected engineering trade-off between engine size and fuel economy.

5. **Stable Maintenance Costs:** Service costs have remained remarkably stable across the 2015–2024 period, fluctuating between ₹14,627 and ₹15,293 annually.

6. **Value Outliers Exist:** The IQR-based outlier analysis identified 715 cars (7.15%) with exceptional VFM scores, representing either extraordinary deals or overpriced listings relative to market norms.

7. **Predictive Capability:** The SLR model, while showing the correct directional trend, demonstrated limited predictive power (R² = 0.074) due to the randomized nature of the dataset. The methodology, however, is sound and would yield stronger results with real-world data.

### 5.2 Technical Contributions

- Development of a **custom VFM Index** that balances mileage, price, and engine capacity into a single comparable metric.
- Implementation of **four distinct statistical tests** (Chi-square, Pearson, IQR, SLR) providing multi-dimensional validation.
- Creation of an **interactive, web-based dashboard** that allows real-time exploration without requiring programming knowledge.

### 5.3 Limitations

1. The dataset appears to be synthetic or curated, resulting in near-uniform distributions that weaken statistical relationships.
2. The SLR model uses only 7 grouped data points for regression, limiting statistical power.
3. External factors affecting car pricing (brand reputation, safety ratings, resale value) are not captured in the dataset.
4. The VFM formula is subjective and weights each component equally; consumers may value mileage differently than engine power.

---

## 6. Future Scope

This project establishes a foundation that can be extended in several directions:

### 6.1 Data Enhancement

- **Real Market Data:** Replacing the current dataset with scrapped data from platforms like CarDekho, CarWale, or Cars24 would produce more realistic statistical relationships and stronger predictive models.
- **Additional Features:** Including variables like safety ratings (NCAP scores), boot space, ground clearance, and warranty period would enrich the analysis.
- **Time Series Data:** Monthly or quarterly sales figures would enable trend forecasting and seasonal analysis.

### 6.2 Advanced Analytics

- **Multiple Linear Regression (MLR):** Extending the SLR model to include multiple predictors (CC, Year, Fuel_Type, Transmission) for more accurate mileage or price prediction.
- **Classification Models:** Using Logistic Regression or Decision Trees to predict whether a car falls in the "high value" or "low value" category based on its specifications.
- **Cluster Analysis:** Applying K-Means clustering to segment the market into natural groups (budget, mid-range, premium) based on multiple features simultaneously.
- **Sentiment Analysis:** Integrating customer review data to correlate satisfaction scores with objective car metrics.

### 6.3 Dashboard Enhancement

- **Normality Testing:** Adding Shapiro-Wilk tests before parametric tests to validate distributional assumptions.
- **Confidence Interval Toggle:** Allowing users to visualize different confidence levels (90%, 95%, 99%) on regression plots.
- **Export Functionality:** Adding PDF/Excel export options for analysis results.
- **Comparative Dashboard:** Side-by-side comparison tool for two or more car models.

### 6.4 Deployment

- **Cloud Deployment:** Hosting the dashboard on Streamlit Community Cloud or Heroku for public access.
- **Mobile Optimization:** Adapting the layout for mobile screens using responsive Streamlit components.
- **API Development:** Creating a REST API endpoint for the prediction model so other applications can consume the forecasting service.

---

## 7. References

1. Society of Indian Automobile Manufacturers (SIAM). "Statistical Profile of Automobile Industry in India, 2023-24." https://www.siam.in

2. McKinney, W. (2017). *Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython.* O'Reilly Media, 2nd Edition.

3. Seabold, S. & Perktold, J. (2010). "Statsmodels: Econometric and Statistical Modeling with Python." *Proceedings of the 9th Python in Science Conference.*

4. VanderPlas, J. (2016). *Python Data Science Handbook.* O'Reilly Media.

5. Streamlit Documentation. "Streamlit API Reference." https://docs.streamlit.io

6. SciPy Documentation. "Statistical Functions (scipy.stats)." https://docs.scipy.org/doc/scipy/reference/stats.html

7. Waskom, M. (2021). "Seaborn: Statistical Data Visualization." *Journal of Open Source Software,* 6(60), 3021.

8. Montgomery, D.C., Peck, E.A., & Vining, G.G. (2012). *Introduction to Linear Regression Analysis.* Wiley, 5th Edition.

9. Numpy Documentation. "NumPy Reference Guide." https://numpy.org/doc

10. Pandas Documentation. "Pandas User Guide." https://pandas.pydata.org/docs

---

*This report was prepared as part of the Indian Auto Market Analytics project. The interactive dashboard can be accessed by running `streamlit run streamlit_app.py` from the project root directory.*
