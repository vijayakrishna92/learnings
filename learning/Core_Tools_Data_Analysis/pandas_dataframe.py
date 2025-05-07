# pandas dataframe
import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5]})
print("data frame", df) # Print the pandas dataframe
print("shape", df.shape) # Print the shape of the pandas dataframe
print("data type", df.dtypes) # Print the data types of the pandas dataframe
print("number of dimension", df.ndim) # Print the number of dimensions of the pandas dataframe
print("column A ", df['A']) # Print the column 'A' of the pandas dataframe
print('first row', df.iloc[0]) # Print the first row of the pandas dataframe
print('first row first column', df.iloc[0, 0]) # Print the element at row 0, column 0 of the pandas dataframe

df = pd.read_csv('data/data.csv') # Read a CSV file into a pandas dataframe
print(df) # Print the pandas dataframe
print(df.head()) # Print the first 5 rows of the pandas dataframe
print(df.tail()) # Print the last 5 rows of the pandas dataframe
print(df.shape) # Print the shape of the pandas dataframe
print(df.dtypes) # Print the data types of the pandas dataframe
print(df.ndim) # Print the number of dimensions of the pandas dataframe
print(df.columns) # Print the columns of the pandas dataframe
print(df['Name']) # Print the column 'Name' of the pandas dataframe
print(df.info) # Print the info of the pandas dataframe
print(df.describe()) # Print the description of the pandas dataframe
print(df.value_counts()) # Print the value counts of the pandas dataframe
print(df.nunique()) # Print the number of unique values in each column of the pandas dataframe
print(df.iloc[:,-1]) # Print the last columns of the pandas dataframe
print(df.iloc[0, -1]) # Print the element at row 0, column -1 of the pandas dataframe