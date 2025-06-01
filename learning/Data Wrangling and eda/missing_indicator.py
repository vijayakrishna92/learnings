# Add a new binary column to indicate if a value was missing (useful in ML models).

import pandas as pd
import numpy as np


# Sample DataFrame with missing values
df = pd.DataFrame({
    'Age': [25, np.nan, 22, 28],
    'Income': [50000, 54000, np.nan, 58000],
    'Gender': ['F', 'M', 'F', None]
})

# Create missing indicator for 'Age'
df['Age_missing'] = df['Age'].isnull().astype(int)
print(df['Age_missing'])

# Can be useful before filling
df['Age_filled'] = df['Age'].fillna(df['Age'].median())
print(df['Age_filled'])