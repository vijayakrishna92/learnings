# pandas dataframe
import pandas as pd


df = pd.read_csv('data/data.csv') # Read a CSV file into a pandas dataframe
df['active'] = True
print(df)

#save to new csv
df.to_csv('data/output.csv', index= False)