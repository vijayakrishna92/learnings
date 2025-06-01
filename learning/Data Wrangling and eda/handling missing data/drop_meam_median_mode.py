# Removing: Drop rows/columns with missing values.
# Imputing: Fill in missing values with statistical measures (mean, median, mode) or ML models.

import pandas as pd
import numpy as np
# Sample DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', None, 'David'],
    'Age': [25, np.nan, 22, 28],
    'Gender': ['F', 'M', 'F', None]
})

print("Original DataFrame:")
print(df)
print("\n---")

# Drop rows with any missing values
df_dropped = df.dropna()
print("After dropping rows with missing values:")
print(df_dropped)
print("\n---")

# Fill missing numerical value with mean
df['Age_filled_mean'] = df['Age'].fillna(df['Age'].mean())
print("Fill missing 'Age' with mean:")
print(df[['Age', 'Age_filled_mean']])
print("\n---")

# Fill missing categorical value with mode
df['Gender_filled_mode'] = df['Gender'].fillna(df['Gender'].mode()[0])
print("Fill missing 'Gender' with mode:")
print(df[['Gender', 'Gender_filled_mode']])
print("\n---")

# Fill missing numerical value with median
df['Age_filled_median'] = df['Age'].fillna(df['Age'].median())
print("Fill missing 'Age' with median:")
print(df[['Age', 'Age_filled_median']])