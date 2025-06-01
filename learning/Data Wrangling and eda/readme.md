🔹 Data Wrangling
1. Handling Missing Data
Detecting missing values

Removing vs. imputing (mean/median/mode/ML-based)

Forward/backward fill

Missing indicator variables

2. Handling Outliers
Z-score, IQR methods

Visualization (boxplots, scatter)

Capping/trimming/winsorization

3. Data Types & Conversions
Numeric, categorical, datetime, object types

Type conversion (astype)

Parsing dates, custom formatting

Memory optimization (downcasting)

4. Feature Engineering
Creating new features from existing data

Binning (discretization)

Feature extraction from strings, dates, etc.

5. Feature Scaling
MinMax Scaling

Standard Scaling (Z-score)

Robust Scaling

Normalization (L1, L2)

6. Encoding Categorical Variables
Label Encoding

One-Hot Encoding

Ordinal Encoding

Target/Mean Encoding (carefully with leakage!)

7. Text and String Manipulation
Splitting, replacing, extracting substrings

Regular expressions

Text cleaning (lowercasing, removing punctuation)

🔹 EDA (Exploratory Data Analysis)
1. Descriptive Statistics
Mean, median, mode, std, skew, kurtosis

.describe(), .value_counts(), .info()

2. Aggregations
groupby()

agg() (custom aggregations)

Multi-level groupby

Pivot tables and cross-tabulations

3. Data Visualization
Distribution Analysis
Histogram

KDE plot

Boxplot, Violin plot

ECDF plots

Relationship Analysis
Scatter plots

Pair plots

Heatmaps (correlation matrix)

Joint plots

Categorical Analysis
Count plots

Bar plots

Strip, swarm, and box plots grouped by category

Time Series Plots
Line plots

Rolling averages, trends

4. Correlation & Associations
Pearson/Spearman correlation

Covariance

Heatmaps of correlation matrix

Multicollinearity (VIF)

5. Dimensionality Reduction (Optional but helpful)
PCA (Principal Component Analysis)

t-SNE/UMAP for visualization

🔹 Advanced Data Handling (Optional/Bonus)
Merging & joining datasets (merge, concat, join)

Reshaping data (melt, pivot)

Window functions (rolling, expanding)

Time series indexing and resampling

Handling duplicate rows

Data sampling (random sampling, stratified sampling)