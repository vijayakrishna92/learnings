 
1. NumPy – Numerical operations
Arrays and matrix operations

Broadcasting

Indexing and slicing

Vectorized computations

2. pandas – Data analysis powerhouse
DataFrames and Series

Reading/writing data (CSV, Excel, JSON)

Cleaning data (missing values, renaming, filtering)

GroupBy, merge/join, pivot tables

3. Data Visualization
matplotlib – core plotting

seaborn – statistical plots (histogram, boxplot, heatmap)

(Optional) plotly – interactive visualizations

4. SQL Basics
SELECT, WHERE, JOIN, GROUP BY, ORDER BY

Aggregations and subqueries


🔍 Exploratory Data Analysis (EDA) Checklist
🟢 1. Understand the Data
Read the dataset: Use pandas.read_csv() or similar

df.head(), df.tail(), df.info(), df.describe()

Check data types of each column

Identify target variable (if any)

🟡 2. Univariate Analysis (One feature at a time)
Categorical variables:

Value counts: df['col'].value_counts()

Plots: bar plots, pie charts

Numerical variables:

Summary stats: mean, median, std

Plots: histograms, boxplots, density plots

🟠 3. Bivariate / Multivariate Analysis
Relationship between two or more features

Numerical vs numerical:

Scatter plots, correlation matrix

Categorical vs numerical:

Box plots, violin plots

Categorical vs categorical:

Crosstabs, stacked bar plots

🔵 4. Missing Values
Identify missing data: df.isnull().sum()

Options:

Drop rows/columns

Impute with mean/median/mode

Flag missingness as a feature

🟣 5. Outlier Detection
Use boxplots, IQR, or z-score methods

Decide whether to remove, cap, or keep them

⚫ 6. Feature Engineering (early ideas)
Creating new columns

Date features (year, month, weekday)

Binning continuous variables

Encoding categorical variables (label/one-hot)

🟤 7. Data Distribution & Correlation
Histograms, KDE plots for distribution

Heatmaps for correlation (df.corr() + sns.heatmap())