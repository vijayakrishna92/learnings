# Z-score measures how far a data point is from the mean in terms of standard deviation. Points with |z| > 3 are often considered outliers.

import pandas as pd

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