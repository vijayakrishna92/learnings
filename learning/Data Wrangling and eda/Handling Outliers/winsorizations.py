# Trimming: Remove outliers completely

# Capping/Winsorization: Replace outliers with threshold values
import pandas as pd
import numpy as np

# Sample data
df = pd.DataFrame({
    'Income': [45000, 47000, 48000, 100000, 1000000]  # Last value is an outlier
})
Q1 = df['Income'].quantile(0.25)
Q3 = df['Income'].quantile(0.75)
IQR = Q3 - Q1

# Define bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Winsorize (cap values outside bounds)
df['Income_capped'] = np.where(df['Income'] > upper_bound, upper_bound,
                               np.where(df['Income'] < lower_bound, lower_bound, df['Income']))

print("Winsorized Income:")
print(df[['Income', 'Income_capped']])

# 1000000 should be trimmed or Winsorization with threshold, above one is Winsorization