import pandas as pd
from sklearn.preprocessing import LabelEncoder
#If you have labels like ['Low', 'Medium', 'High'], convert them to numbers.
df = pd.read_csv('data/data.csv')

encoder = LabelEncoder()
df['name_encoded'] = encoder.fit_transform(df['Name'])
print(df[['name_encoded']])