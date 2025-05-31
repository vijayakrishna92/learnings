
import pandas as pd
from sklearn.preprocessing import StandardScaler
#Used to standardize features (mean = 0, std = 1).
df = pd.read_csv('data/data.csv')

scaler = StandardScaler()
df[['Age', 'income']] = scaler.fit_transform(df[['Age', 'income']])
print(df[['Age', 'income']])