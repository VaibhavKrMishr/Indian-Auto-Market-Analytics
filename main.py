import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

st.set_page_config(page_title="Car Market Analysis", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv('data/car_dataset_india.csv')

def main():
    df = load_data()

    st.sidebar.title("Car Market Analysis")
    st.sidebar.write("Indian 4-Wheeler Dataset")

    page = st.sidebar.radio("Select Page", [
        "Home",
        "1. Brand Overview",
        "2. Model Breakdown",
        "3. CC vs Mileage",
        "4. Service Costs",
        "5. Value for Money",
        "6. Mileage Prediction (SLR)"
    ])

    # ---- HOME PAGE ----
    if page == "Home":
        st.title("Indian Car Market - Quick Look")
        st.write(f"We have **{len(df)}** cars from **{df['Brand'].nunique()}** brands in this dataset.")

        with st.expander("Data health check"):
            st.write("Null values per column:")
            st.write(df.isnull().sum())
            st.write("Column types:")
            st.write(df.dtypes)

        st.subheader("First 10 rows")
        st.dataframe(df.head(10))

        st.subheader("describe() output")
        st.dataframe(df.describe())

        st.subheader("Some distributions")
        col1, col2 = st.columns(2)
        with col1:
            fig = plt.figure()
            sns.histplot(df['Price'], kde=True)
            plt.title("Price spread")
            st.pyplot(fig)
        with col2:
            fig = plt.figure()
            sns.histplot(df['Mileage'], kde=True, color='green')
            plt.title("Mileage spread")
            st.pyplot(fig)

        # wanted to see how the numerical columns correlate with each other
        st.subheader("Correlation heatmap")
        fig, ax = plt.subplots()
        num_cols = df.select_dtypes('number').drop(columns=['Car_ID'])
        sns.heatmap(num_cols.corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

    # ---- BRAND OVERVIEW ----
    elif page == "1. Brand Overview":
        st.header("Brand-wise numbers")
        st.write("Seeing which brands appear more and how their pricing looks.")

        brand_df = df.groupby('Brand').agg(
            avg_price=('Price', 'mean'),
            count=('Car_ID', 'count')
        ).reset_index()
        brand_df = brand_df.sort_values('count', ascending=False)

        st.dataframe(brand_df)

        fig = plt.figure(figsize=(10, 5))
        sns.barplot(data=brand_df, x='Brand', y='count')
        plt.xticks(rotation=45)
        plt.title("How many listings per brand")
        st.pyplot(fig)

        # chi square test - checking if theres a link between brand and fuel type
        ct = pd.crosstab(df['Brand'], df['Fuel_Type'])
        chi2, pval, dof, expected = stats.chi2_contingency(ct)
        st.write(f"Chi-square p-value: {pval:.4f}")
        if pval < 0.05:
            st.write("Looks like brands do tend to prefer certain fuel types, which makes sense.")
        else:
            st.write("No strong pattern between brand and fuel.")

    elif page == "2. Model Breakdown":
        st.header("Models inside a brand")

        brand = st.selectbox("Pick a brand", sorted(df['Brand'].unique()))
        temp = df[df['Brand'] == brand]
        mc = temp['Model'].value_counts()

        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**{brand}** has {len(mc)} models:")
            st.dataframe(mc)
        with col2:
            fig, ax = plt.subplots()
            ax.pie(mc, labels=mc.index, autopct='%1.1f%%')
            plt.title(f"{brand} model share")
            st.pyplot(fig)



    elif page == "3. CC vs Mileage":
        st.header("Does engine size affect mileage?")

        # electric cars dont have CC so removing them
        ice = df[df['Fuel_Type'] != 'Electric']
        st.write(f"Working with {len(ice)} non-electric cars.")

        grouped = ice.groupby(['Engine_CC','Fuel_Type'], observed=False)['Mileage'].mean().reset_index()

        fig = plt.figure(figsize=(10, 6))
        sns.lineplot(data=grouped, x='Engine_CC', y='Mileage', hue='Fuel_Type', marker='o')
        plt.title("Avg mileage by engine CC")
        st.pyplot(fig)

        r_val, p_val = stats.pearsonr(ice['Engine_CC'], ice['Mileage'])
        st.write(f"Pearson correlation: r = {r_val:.4f}, p = {p_val:.4e}")
        st.write("bigger engine usually means less mileage so this makes sense")

    elif page == "4. Service Costs":
        st.header("Service cost over the years")

        fig = plt.figure(figsize=(10, 5))
        sns.lineplot(data=df, x='Year', y='Service_Cost', estimator='mean')
        plt.title("Average service cost by year")
        st.pyplot(fig)



        st.write("Boxplot to spot any weird outliers:")
        fig = plt.figure()
        sns.boxplot(data=df, x='Year', y='Service_Cost')
        plt.xticks(rotation=45)
        st.pyplot(fig)

    elif page == "5. Value for Money":
        st.header("Value for Money ranking")
        st.write("I made a simple formula: (Mileage / Price in lakhs) * (CC / 1000)")
        st.write("Higher score = better deal for what you pay.")

        vdf = df.copy()
        vdf['vfm'] = (vdf['Mileage'] / (vdf['Price']/100000)) * (vdf['Engine_CC']/1000)

        st.write("Top 10:")
        st.dataframe(vdf.nlargest(10, 'vfm')[['Brand','Model','Price','Mileage','Engine_CC','vfm']])

        fig = plt.figure()
        sns.boxplot(x=vdf['vfm'])
        plt.title("VFM score distribution")
        st.pyplot(fig)

        # checking for outliers using IQR method
        q1 = vdf['vfm'].quantile(0.25)
        q3 = vdf['vfm'].quantile(0.75)
        iqr_val = q3 - q1
        lower = q1 - 1.5 * iqr_val
        upper = q3 + 1.5 * iqr_val
        outliers = vdf[(vdf['vfm'] < lower) | (vdf['vfm'] > upper)]
        st.write(f"Found {len(outliers)} outlier cars by IQR method.")
        if not outliers.empty:
            st.dataframe(outliers[['Brand','Model','vfm']])

    elif page == "6. Mileage Prediction (SLR)":
        st.header("Simple Linear Regression - CC vs Mileage")
        st.write("Trying to see if we can predict mileage from engine cc.")
        st.write("Using grouped averages so the trend is cleaner.")

        # same filter as before, no electric
        ice_df = df[df['Fuel_Type'] != 'Electric']
        g = ice_df.groupby('Engine_CC')['Mileage'].mean().reset_index()

        slope, intercept, r_val, p_val, std_err = stats.linregress(g['Engine_CC'], g['Mileage'])

        st.write(f"Equation: mileage = {slope:.5f} × CC + {intercept:.2f}")
        st.write(f"r value = {r_val:.4f}, p value = {p_val:.4f}")

        # negative slope means bigger cc = worse mileage
        fig = plt.figure(figsize=(9, 5))
        sns.regplot(x=g['Engine_CC'], y=g['Mileage'])
        plt.title("Regression: CC vs avg mileage")
        plt.xlabel("Engine CC")
        plt.ylabel("Avg Mileage (kmpl)")
        st.pyplot(fig)

        st.subheader("Try it yourself")
        cc_input = st.number_input("Enter a CC value", 800, 5000, 1200)
        result = intercept + slope * cc_input
        st.write(f"Predicted mileage for {cc_input}cc: **{result:.2f} kmpl**")

if __name__ == "__main__":
    main()
