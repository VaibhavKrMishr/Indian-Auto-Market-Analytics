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

    st.sidebar.image("images/car.png")
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

    if page == "Home":
        st.title("Indian Car Market - Quick Look")
        st.write("We have **" + str(len(df)) + "** cars from **" + str(df['Brand'].nunique()) + "** brands.")

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

        st.subheader("Correlation heatmap")
        fig, ax = plt.subplots()
        nums = df.select_dtypes('number').drop(columns=['Car_ID'])
        sns.heatmap(nums.corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

    elif page == "1. Brand Overview":
        st.header("Brand-wise numbers")
        st.write("Seeing which brands appear more and how their pricing looks.")

        brand_df = df.groupby('Brand').agg(avg_price=('Price','mean'), count=('Car_ID','count')).reset_index()
        brand_df = brand_df.sort_values('count', ascending=False)
        st.dataframe(brand_df)

        fig = plt.figure(figsize=(10, 5))
        sns.barplot(data=brand_df, x='Brand', y='count')
        plt.xticks(rotation=45)
        plt.title("How many listings per brand")
        st.pyplot(fig)

    elif page == "2. Model Breakdown":
        st.header("Models inside a brand")

        brand = st.selectbox("Pick a brand", sorted(df['Brand'].unique()))
        temp = df[df['Brand'] == brand]
        mc = temp['Model'].value_counts()

        col1, col2 = st.columns(2)
        with col1:
            st.write("**" + brand + "** has " + str(len(mc)) + " models:")
            st.dataframe(mc)
        with col2:
            fig, ax = plt.subplots()
            ax.pie(mc, labels=mc.index, autopct='%1.1f%%')
            plt.title(brand + " model share")
            st.pyplot(fig)

    elif page == "3. CC vs Mileage":
        st.header("Does engine size affect mileage?")
        # electric cars dont have CC so removing them
        ice = df[df['Fuel_Type'] != 'Electric']
        st.write("Working with " + str(len(ice)) + " non-electric cars.")

        grouped = ice.groupby(['Engine_CC','Fuel_Type'], observed=False)['Mileage'].mean().reset_index()
        fig = plt.figure(figsize=(10, 6))
        sns.lineplot(data=grouped, x='Engine_CC', y='Mileage', hue='Fuel_Type', marker='o')
        plt.title("Avg mileage by engine CC")
        st.pyplot(fig)

    elif page == "4. Service Costs":
        st.header("Service cost over the years")
        fig = plt.figure(figsize=(10, 5))
        sns.lineplot(data=df, x='Year', y='Service_Cost', estimator='mean')
        plt.title("Average service cost by year")
        st.pyplot(fig)



        st.subheader("Service cost trend by brand")
        fig = plt.figure(figsize=(12,6))
        sns.lineplot(data=df, x='Year', y='Service_Cost', hue='Brand', estimator='mean')
        plt.title("Year-wise service cost per brand")
        plt.legend(bbox_to_anchor=(1.05,1), loc='upper left', fontsize=8)
        plt.tight_layout()
        st.pyplot(fig)

    elif page == "5. Value for Money":
        st.header("Value for Money ranking")
        st.write("I made a simple formula: (Mileage / Price in lakhs) * (CC / 1000)")
        st.write("Higher score = better deal for what you pay.")

        vdf = df.copy()
        vdf['vfm'] = (vdf['Mileage'] / (vdf['Price']/100000)) * (vdf['Engine_CC']/1000)

        top = vdf.nlargest(10,'vfm')[['Brand','Model','Price','Mileage','Engine_CC','vfm']]
        st.dataframe(top)

        st.subheader("Top 10 VFM Cars")
        fig, ax = plt.subplots(figsize=(10,5))
        names = top['Brand'] + ' ' + top['Model']
        ax.barh(names, top['vfm'], color=sns.color_palette("viridis", len(top)))
        ax.set_xlabel("VFM Score")
        ax.invert_yaxis()
        plt.tight_layout()
        st.pyplot(fig)

        st.subheader("Average VFM by Brand")
        bv = vdf.groupby('Brand')['vfm'].mean().sort_values(ascending=False)
        fig = plt.figure(figsize=(10,4))
        bv.plot(kind='bar', color='teal')
        plt.ylabel("Avg VFM Score")
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig)

    elif page == "6. Mileage Prediction (SLR)":
        st.header("Simple Linear Regression - CC vs Mileage")

        # same filter, no electric
        ice_df = df[df['Fuel_Type'] != 'Electric']
        g = ice_df.groupby('Engine_CC')['Mileage'].mean().reset_index()

        slope, intercept, r_val, p_val, std_err = stats.linregress(g['Engine_CC'], g['Mileage'])


        st.subheader("Try it yourself")
        cc_input = st.number_input("Enter a CC value", 800, 5000, 1200)
        result = intercept + slope * cc_input
        st.write("Predicted mileage for " + str(cc_input) + "cc: **" + str(round(result, 2)) + " kmpl**")

        fig = plt.figure(figsize=(10, 6))
        sns.regplot(x=g['Engine_CC'], y=g['Mileage'], ci=95, marker='o', scatter_kws={'s':80,'zorder':5})
        plt.title("CC vs Average Mileage (with 95% confidence band)")
        plt.xlabel("Engine CC")
        plt.ylabel("Avg Mileage (kmpl)")
        plt.grid(True, alpha=0.3)
        st.pyplot(fig)


if __name__ == "__main__":
    main()
