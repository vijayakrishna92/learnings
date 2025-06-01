# Propagate previous or next value to fill missing data (used often in time series).

import pandas as pd
import numpy as np


# Sample DataFrame with missing values
df = pd.DataFrame({
    'Age': [25, np.nan, 22, 28],
    'Income': [50000, 54000, np.nan, 58000],
    'Gender': ['F', 'M', 'F', None]
})

# Forward fill (fill with previous value)
df['Gender_ffill'] = df['Gender'].ffill()
print(df['Gender_ffill'])

# Backward fill (fill with next value)

df['Gender_bfill'] = df['Gender'].bfill()
print(df['Gender_bfill'])