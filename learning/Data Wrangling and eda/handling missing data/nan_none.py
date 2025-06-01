import pandas as pd
import numpy as np
# Identify which values are missing (NaN, None) in your dataset.
# Sample DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', None, 'David'],
    'Age': [25, np.nan, 22, 28],
    'Gender': ['F', 'M', 'F', None]
})

# Detect missing values
print(df.isnull())

# Count total missing values per column
print(df.isnull().sum())