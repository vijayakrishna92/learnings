# IQR = Q3 - Q1. Outliers lie below Q1 - 1.5×IQR or above Q3 + 1.5×IQR.

import pandas as pd
import numpy as np
from scipy.stats import zscore

# Sample data
df = pd.DataFrame({
    'Income': [45000, 47000, 48000, 100000, 1000000]  # Last value is an outlier
})

# Reuse the same Income column
Q1 = df['Income'].quantile(0.25)
Q3 = df['Income'].quantile(0.75)
IQR = Q3 - Q1
# Define bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter
df_iqr_filtered = df[(df['Income'] >= lower_bound) & (df['Income'] <= upper_bound)]

print("IQR filtered data:")
print(df_iqr_filtered)