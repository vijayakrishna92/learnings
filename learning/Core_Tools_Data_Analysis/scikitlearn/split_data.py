'''
A Python library that provides tools to:

Preprocess data

Build machine learning models

Evaluate models

Use them for prediction                                           |

'''

import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('data/data.csv')
#print(df.head)
x = df['Age']        # Features (input)
y = df['income']       # Target (output)
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print('xtrain',X_train,'xtest',X_test,'ytrain',y_train,'yest',y_test)