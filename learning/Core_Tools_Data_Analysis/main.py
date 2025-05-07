# pandas dataframe
import pandas as pd


df = pd.read_csv('data/data.csv') # Read a CSV file into a pandas dataframe

'''
✅ 4. Data Cleaning
Handling missing values: .isnull(), .fillna(), .dropna()

Renaming columns: .rename()

Changing data types: .astype()

Removing duplicates: .drop_duplicates()

Replacing values: .replace()

✅ 5. Working with Columns
Creating new columns:

python
Copy
Edit
df['bmi'] = df['weight'] / (df['height']/100)**2
Apply functions: .apply(), .map(), .applymap()

Lambda functions

✅ 6. Sorting & Filtering
.sort_values(), .sort_index()

.query() for filtering

✅ 7. Grouping & Aggregating
.groupby() + .agg()

python
Copy
Edit
df.groupby('gender')['salary'].mean()
df.groupby(['department']).agg({'salary': 'sum', 'age': 'mean'})
✅ 8. Merging & Joining
pd.merge() – SQL-style joins

df.concat() – stacking dataframes vertically/horizontally

df.join() – join on index

✅ 9. Pivoting & Reshaping
.pivot(), .pivot_table()

.melt() – unpivot

.stack(), .unstack()

✅ 10. DateTime Operations
pd.to_datetime()

Extracting features: .dt.year, .dt.month, .dt.day_name()

Time filtering, resampling (.resample())

Bonus:
Exporting: .to_csv(), .to_excel()

Profiling tools: pandas-profiling, df.describe(include='all')
'''