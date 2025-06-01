#MICE is a sophisticated technique that models each feature with missing values as a function of other features and iteratively imputes them.
#MICE works best when your dataset has multiple correlated features.
#You can use IterativeImputer from sklearn.impute which is an implementation of MICE. For categorical variables, you often need to encode them numerically before applying MICE.

import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer  # noqa
from sklearn.impute import IterativeImputer

# Sample DataFrame with missing values
df = pd.DataFrame({
    'Age': [25, np.nan, 22, 28],
    'Income': [50000, 54000, np.nan, 58000],
    'Gender': ['F', 'M', 'F', None]
})

# Convert categorical to numeric first (for example purposes, label encoding)
df['Gender_enc'] = df['Gender'].map({'F': 0, 'M': 1})

# Select only numeric columns for imputation
num_cols = ['Age', 'Income', 'Gender_enc']

# Create imputer object
imputer = IterativeImputer(random_state=0)

# Fit and transform the numeric data
df_imputed = imputer.fit_transform(df[num_cols])

# Convert back to DataFrame
df_imputed = pd.DataFrame(df_imputed, columns=num_cols)

print(df_imputed)
