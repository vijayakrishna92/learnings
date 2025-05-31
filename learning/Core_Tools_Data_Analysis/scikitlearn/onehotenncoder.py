import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Load your data
df = pd.read_csv('data/data.csv')

# Initialize OneHotEncoder (disable sparse output for easy DataFrame conversion)
encoder = OneHotEncoder(sparse_output=False)  # use sparse=False if you have an older sklearn version

# Fit and transform the 'Name' column
encoded = encoder.fit_transform(df[['Name']])

# Convert to dataframe
encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(['Name']))

# Show result
print(encoded_df)