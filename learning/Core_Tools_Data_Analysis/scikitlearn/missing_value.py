import pandas as pd
from sklearn.impute import SimpleImputer

df = pd.read_csv('data/data.csv')

# Fill missing ages with the mean
imputer = SimpleImputer(strategy='mean')
df[['Age']] = imputer.fit_transform(df[['Age']])
print(df[['Age']])