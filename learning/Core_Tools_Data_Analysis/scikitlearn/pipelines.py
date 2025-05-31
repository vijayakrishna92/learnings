import pandas as pd
from sklearn.pipeline import Pipeline # Used to organize preprocessing steps cleanly.
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

# Load your data
df = pd.read_csv('data/data.csv')

pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

df[['Age', 'income']] = pipeline.fit_transform(df[['Age', 'income']])

# Show result
print(df[['Age', 'income']])