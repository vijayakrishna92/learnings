import pandas as pd
from sklearn.preprocessing import MinMaxScaler
# Alternative to StandardScaler, scales between 0 and 1.
df = pd.read_csv('data/data.csv')

scaler = MinMaxScaler()
df[['Age', 'income']] = scaler.fit_transform(df[['Age', 'income']])
print(df[['Age', 'income']])