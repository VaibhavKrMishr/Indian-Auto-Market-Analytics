import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

IMG = "/home/vaibhav/Desktop/Projects/Indian-Auto-Market-Analytics/images"
OUT = "/home/vaibhav/Desktop/Projects/Indian-Auto-Market-Analytics/Indian_Auto_Market_Report.docx"

doc = Document()
style = doc.styles['Normal']
style.font.name = 'Calibri'
style.font.size = Pt(11)

def heading(txt, lvl=1):
    doc.add_heading(txt, level=lvl)

def para(txt, bold=False):
    p = doc.add_paragraph()
    r = p.add_run(txt)
    r.bold = bold

def img(name, w=5.5):
    path = os.path.join(IMG, name)
    if os.path.exists(path):
        doc.add_picture(path, width=Inches(w))
        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER

def table(headers, rows):
    t = doc.add_table(rows=1+len(rows), cols=len(headers))
    t.style = 'Light Grid Accent 1'
    for i, h in enumerate(headers):
        t.rows[0].cells[i].text = h
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            t.rows[ri+1].cells[ci].text = str(val)

# ========== TITLE PAGE ==========
for _ in range(6):
    doc.add_paragraph()
t = doc.add_paragraph()
t.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = t.add_run("Indian Auto Market Analytics")
r.bold = True
r.font.size = Pt(28)
r.font.color.rgb = RGBColor(0, 51, 102)

s = doc.add_paragraph()
s.alignment = WD_ALIGN_PARAGRAPH.CENTER
r2 = s.add_run("A Statistical Analysis of the Indian Four-Wheeler Market")
r2.font.size = Pt(16)
r2.font.color.rgb = RGBColor(100, 100, 100)

for _ in range(4):
    doc.add_paragraph()
info = doc.add_paragraph()
info.alignment = WD_ALIGN_PARAGRAPH.CENTER
info.add_run("Technology: ").bold = True
info.add_run("Python, Streamlit, Pandas, Seaborn, Matplotlib, SciPy")
d = doc.add_paragraph()
d.alignment = WD_ALIGN_PARAGRAPH.CENTER
d.add_run("Date: April 2026")
doc.add_page_break()

# ========== TOC ==========
heading("Table of Contents")
for item in ["1. Introduction","2. Source of Dataset","3. Exploratory Data Analysis (EDA)","4. Analysis on Dataset","   4.1 Brand Market Overview","   4.2 Brand Model Breakdown","   4.3 Engine CC vs Mileage","   4.4 Service Cost Trends","   4.5 Value for Money Index","   4.6 Mileage Prediction (SLR)","5. Conclusion","6. Future Scope","7. References"]:
    doc.add_paragraph(item)
doc.add_page_break()

# ========== 1. INTRODUCTION ==========
heading("1. Introduction")
para("The Indian automobile industry is one of the largest in the world. India is currently the third-largest automobile market globally by volume. The four-wheeler segment has seen remarkable growth over the past decade driven by rising disposable incomes, urbanization, and improved road infrastructure.")
para("This project aims to analyze the Indian car market through a data-driven approach. We built an interactive dashboard using Python and Streamlit that performs six distinct analytical modules on a comprehensive dataset of 10,000 car listings.")

heading("1.1 Objectives", 2)
for obj in ["Perform thorough EDA on the Indian car market dataset","Identify brand positioning and market share patterns","Analyze the relationship between engine displacement and fuel efficiency","Track maintenance cost trends across model years","Develop a custom Value-for-Money index","Build a predictive model using Simple Linear Regression"]:
    doc.add_paragraph(obj, style='List Bullet')

heading("1.2 Tools and Technologies", 2)
table(["Tool","Purpose"],[["Python 3.13","Core language"],["Pandas","Data manipulation"],["NumPy","Numerical computations"],["Matplotlib","Charts"],["Seaborn","Statistical visualization"],["SciPy","Hypothesis testing & regression"],["Streamlit","Interactive dashboard"]])

heading("1.3 Project Structure", 2)
for line in ["Indian-Auto-Market-Analytics/","├── main.py","├── streamlit_app.py","├── data/car_dataset_india.csv","├── images/","├── pyproject.toml","└── uv.lock"]:
    p = doc.add_paragraph(line)
    p.runs[0].font.name = 'Consolas'
    p.runs[0].font.size = Pt(9)
doc.add_page_break()

# ========== 2. SOURCE ==========
heading("2. Source of Dataset")
heading("2.1 Dataset Overview", 2)
para("The dataset contains 10,000 car listings from the Indian automobile market, covering 10 major brands across a 10-year period (2015-2024).")

heading("2.2 Specifications", 2)
table(["Property","Value"],[["Total Records","10,000"],["Total Features","11"],["File Format","CSV"],["Time Period","2015 - 2024"],["Geographic Scope","India"]])

heading("2.3 Feature Description", 2)
table(["#","Column","Type","Description"],[["1","Car_ID","int64","Unique ID"],["2","Brand","string","Manufacturer"],["3","Model","string","Car model"],["4","Year","int64","Year of manufacture"],["5","Fuel_Type","string","Petrol/Diesel/CNG/Electric"],["6","Transmission","string","Manual/Automatic"],["7","Price","float64","Price in INR"],["8","Mileage","float64","kmpl"],["9","Engine_CC","int64","Engine displacement"],["10","Seating_Capacity","int64","Seats (4-7)"],["11","Service_Cost","float64","Annual service cost"]])

heading("2.4 Brands Covered", 2)
table(["#","Brand","Listings"],[["1","Maruti Suzuki","1,042"],["2","Volkswagen","1,034"],["3","Hyundai","1,033"],["4","Mahindra","1,024"],["5","Skoda","1,011"],["6","Tata Motors","989"],["7","Honda","982"],["8","Kia","973"],["9","Renault","958"],["10","Toyota","954"]])

heading("2.5 Fuel Type Distribution", 2)
table(["Fuel Type","Count","Percentage"],[["CNG","2,588","25.88%"],["Electric","2,518","25.18%"],["Diesel","2,468","24.68%"],["Petrol","2,426","24.26%"]])
doc.add_page_break()

# ========== 3. EDA ==========
heading("3. Exploratory Data Analysis (EDA)")
para("Before running statistical tests, we need to understand the data quality and distribution patterns.")

heading("3.1 Data Quality - Null Check", 2)
para("We checked for missing values using df.isnull().sum(). The dataset has zero null values across all 11 columns.")
img("EDA_Null.png")
para("Figure 3.1: Null value check output")

heading("3.2 Data Types", 2)
para("All column types are correctly assigned — 7 numerical and 4 categorical.")
img("EDA_Info.png")
para("Figure 3.2: Column data types")

heading("3.3 Sample Data - head(10)", 2)
img("HEad_10.png")
para("Figure 3.3: First 10 rows of the dataset")

heading("3.4 Descriptive Statistics", 2)
para("Using df.describe() to get summary statistics for all numerical columns.")
img("Describe.png")
para("Figure 3.4: describe() output")

heading("3.5 Distributions", 2)
para("Price and mileage histograms with KDE overlay show roughly uniform distributions.")
img("EDA_pics.png")
para("Figure 3.5: Price and Mileage distribution plots")

heading("3.6 Correlation Matrix", 2)
para("All pairwise correlations are extremely weak (|r| < 0.02), showing features are largely independent.")
img("EDA_Corr_heatmap.png")
para("Figure 3.6: Correlation heatmap")
doc.add_page_break()

# ========== 4. ANALYSES ==========
heading("4. Analysis on Dataset")

# 4.1
heading("4.1 Analysis 1: Brand Market Overview", 2)
heading("i. Introduction", 3)
para("This analysis examines how brands are distributed in terms of listing volume and average pricing.")
heading("ii. General Description", 3)
para("We aggregate the dataset by Brand to compute volume and average price per brand.")
heading("iii. Requirements and Functions", 3)
para("Functions: df.groupby('Brand').agg(), seaborn.barplot()")
heading("iv. Analysis Results", 3)
table(["Brand","Volume","Avg Price"],[["Maruti Suzuki","1,042","₹19.18L"],["Volkswagen","1,034","₹19.61L"],["Hyundai","1,033","₹19.33L"],["Mahindra","1,024","₹19.96L"],["Skoda","1,011","₹19.56L"],["Tata Motors","989","₹19.16L"],["Honda","982","₹19.72L"],["Kia","973","₹19.17L"],["Renault","958","₹19.51L"],["Toyota","954","₹19.40L"]])
heading("v. Visualization", 3)
img("Brand_sales_A1.png")
para("Figure 4.1: Brand volume distribution")
doc.add_page_break()

# 4.2
heading("4.2 Analysis 2: Brand Model Breakdown", 2)
heading("i. Introduction", 3)
para("This module drills into individual brand portfolios to see how sales are split across models.")
heading("ii. General Description", 3)
para("User selects a brand, and we display a pie chart showing the model-wise percentage split.")
heading("iii. Requirements and Functions", 3)
para("Functions: df[df['Brand']==selected], Series.value_counts(), matplotlib.pyplot.pie()")
para("Model Share (%) = (Count of Model / Total Brand Count) × 100")
heading("iv. Analysis Results & Visualization", 3)
para("Screenshots from all 10 brands:")

brand_imgs = [
    ("A2_Honda.png","Honda"), ("A2_Hyundia.png","Hyundai"), ("A2_Kia.png","Kia"),
    ("A2_Mahindra.png","Mahindra"), ("A2_Maruti.png","Maruti Suzuki"), ("A2_Skoda.png","Skoda"),
    ("A2_Tata.png","Tata Motors"), ("A2_Toyota.png","Toyota"), ("A2_VW.png","Volkswagen"),
    ("Renault.png","Renault")
]
for fname, bname in brand_imgs:
    para("Figure: " + bname + " Model Split", bold=True)
    img(fname)
doc.add_page_break()

# 4.3
heading("4.3 Analysis 3: Engine CC vs Mileage", 2)
heading("i. Introduction", 3)
para("Analyzing the trade-off between engine size (CC) and fuel efficiency (kmpl). Electric vehicles are excluded since they don't have traditional engine displacement.")
heading("ii. General Description", 3)
para("We group by Engine_CC and Fuel_Type, computing mean mileage for each combination, then plot a multi-line chart.")
heading("iii. Requirements and Functions", 3)
para("Functions: df.groupby(), seaborn.lineplot()")
para("Pearson Correlation: r = Σ(xi-x̄)(yi-ȳ) / √[Σ(xi-x̄)² × Σ(yi-ȳ)²]")
heading("iv. Analysis Results", 3)
para("Sample size: 7,482 non-electric cars. The grouped averages show very little variation (~19.8 to 20.3 kmpl).")
heading("v. Visualization", 3)
img("A3_CC_vs_Mileage.png")
para("Figure 4.3: Average mileage by engine CC, grouped by fuel type")
doc.add_page_break()

# 4.4
heading("4.4 Analysis 4: Service Cost Trends", 2)
heading("i. Introduction", 3)
para("Tracking how service costs evolve across model years and across brands.")
heading("ii. General Description", 3)
para("We compute mean service cost per year and per brand, then visualize both as line charts.")
heading("iii. Requirements and Functions", 3)
para("Functions: seaborn.lineplot(estimator='mean'), seaborn.lineplot(hue='Brand')")
heading("iv. Analysis Results", 3)
table(["Year","Avg Service Cost"],[["2015","₹14,971"],["2016","₹14,910"],["2017","₹14,949"],["2018","₹15,080"],["2019","₹15,160"],["2020","₹14,810"],["2021","₹15,293"],["2022","₹14,960"],["2023","₹14,944"],["2024","₹14,627"]])
para("Costs remain stable across the decade, fluctuating between ₹14,627 and ₹15,293.")
heading("v. Visualization", 3)
img("A4_Service_by_year.png")
para("Figure 4.4a: Average service cost by year")
img("A4_Service_By_Brand_trend.png")
para("Figure 4.4b: Year-wise service cost trend by brand")
doc.add_page_break()

# 4.5
heading("4.5 Analysis 5: Value for Money Index", 2)
heading("i. Introduction", 3)
para("We created a custom VFM index to quantify which cars deliver the best performance-to-price ratio.")
heading("ii. General Description", 3)
para("A VFM score is computed for every car, then the top 10 are ranked, and brand-wise averages are compared.")
heading("iii. Requirements and Functions", 3)
para("VFM Formula: (Mileage / Price in Lakhs) × (Engine_CC / 1000)")
para("Higher score = better value for the buyer.")
heading("iv. Analysis Results", 3)
table(["Rank","Brand","Model","VFM Score"],[["1","Kia","EV6","16.50"],["2","Renault","Kiger","15.85"],["3","Toyota","Camry","15.76"],["4","Honda","Jazz","15.31"],["5","Hyundai","i20","15.06"]])
heading("v. Visualization", 3)
img("A5_Table.png")
para("Figure 4.5a: Top 10 VFM cars data table")
img("A5_Top_10_cars.png")
para("Figure 4.5b: Top 10 VFM cars horizontal bar chart")
img("A5_VFM_by_brand.png")
para("Figure 4.5c: Average VFM score by brand")
doc.add_page_break()

# 4.6
heading("4.6 Analysis 6: Mileage Prediction (SLR)", 2)
heading("i. Introduction", 3)
para("Simple Linear Regression is used to predict average mileage from engine CC using grouped averages.")
heading("ii. General Description", 3)
para("We filter out electric vehicles, group by Engine_CC, compute mean mileage per CC group (7 data points), and fit a regression line.")
heading("iii. Requirements and Functions", 3)
para("SLR Model: ŷ = β₀ + β₁x")
para("Where: ŷ = Predicted Mileage, x = Engine_CC")
para("β₁ (slope) = Σ(xi-x̄)(yi-ȳ) / Σ(xi-x̄)²")
para("β₀ (intercept) = ȳ - β₁x̄")
para("Function: scipy.stats.linregress()")
heading("iv. Analysis Results", 3)
table(["Parameter","Value"],[["Slope (β₁)","-0.000078"],["Intercept (β₀)","20.1260"],["Correlation (r)","-0.2721"],["R²","0.0740"],["P-Value","0.5550"]])
para("Equation: Mileage = -0.000078 × CC + 20.126")
para("The negative slope confirms bigger engines give less mileage, which is the expected engineering relationship.")
heading("v. Visualization", 3)
img("SLR.png")
para("Figure 4.6: Regression plot - CC vs average mileage with 95% confidence band and interactive predictor")
doc.add_page_break()

# ========== 5. CONCLUSION ==========
heading("5. Conclusion")
for i, f in enumerate([
    "The market is well-distributed across 10 major brands, with Maruti Suzuki leading in volume.",
    "Individual brand analysis reveals varying model concentration levels across manufacturers.",
    "The Pearson correlation between Engine_CC and Mileage is weak (r = -0.0077) but directionally correct.",
    "Service costs remained stable across 2015-2024, between ₹14,627 and ₹15,293 annually.",
    "The VFM index identified the best value cars, with Kia EV6, Renault Kiger, and Toyota Camry topping the list.",
    "The SLR model showed the correct negative trend but limited predictive power (R² = 0.074) due to the nature of the dataset."
], 1):
    doc.add_paragraph(str(i) + ". " + f)

heading("5.1 Limitations", 2)
for l in ["The dataset is synthetic, resulting in near-uniform distributions.","SLR uses only 7 grouped data points.","External factors (brand reputation, safety ratings) are not captured.","The VFM formula weights components equally."]:
    doc.add_paragraph(l, style='List Bullet')
doc.add_page_break()

# ========== 6. FUTURE SCOPE ==========
heading("6. Future Scope")
heading("6.1 Data Enhancement", 2)
for x in ["Use real scraped data from CarDekho or Cars24.","Add safety ratings, boot space, warranty period.","Monthly sales data for seasonal analysis."]:
    doc.add_paragraph(x, style='List Bullet')
heading("6.2 Advanced Analytics", 2)
for x in ["Multiple Linear Regression with multiple predictors.","Classification models for value categorization.","K-Means clustering for market segmentation."]:
    doc.add_paragraph(x, style='List Bullet')
heading("6.3 Deployment", 2)
for x in ["Cloud deployment via Streamlit Community Cloud.","Mobile-responsive layout.","REST API for the prediction model."]:
    doc.add_paragraph(x, style='List Bullet')
doc.add_page_break()

# ========== 7. REFERENCES ==========
heading("7. References")
refs = [
    "Society of Indian Automobile Manufacturers (SIAM). https://www.siam.in",
    "McKinney, W. (2017). Python for Data Analysis. O'Reilly Media.",
    "Streamlit Documentation. https://docs.streamlit.io",
    "SciPy Documentation. https://docs.scipy.org/doc/scipy/reference/stats.html",
    "Waskom, M. (2021). Seaborn: Statistical Data Visualization. JOSS, 6(60).",
    "Montgomery, D.C. et al. (2012). Introduction to Linear Regression Analysis. Wiley.",
    "NumPy Documentation. https://numpy.org/doc",
    "Pandas Documentation. https://pandas.pydata.org/docs",
    "VanderPlas, J. (2016). Python Data Science Handbook. O'Reilly Media.",
    "Seabold, S. & Perktold, J. (2010). Statsmodels. 9th Python in Science Conference."
]
for i, ref in enumerate(refs, 1):
    doc.add_paragraph("[" + str(i) + "] " + ref)

doc.save(OUT)
print("Done! Saved to: " + OUT)
