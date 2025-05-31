import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

# Load your data
df = pd.read_csv('data/data.csv')

preprocessor = ColumnTransformer(transformers=[
    ('num', StandardScaler(), ['Age', 'income']),
    ('cat', OneHotEncoder(), ['Name'])
])

# Apply the transformation and print the result
df_transformed = preprocessor.fit_transform(df)
print(df_transformed)