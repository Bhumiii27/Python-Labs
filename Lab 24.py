#Write a code snippet to check the data types of each column in a DataFrame.
import pandas as pd 
df = pd.DataFrame({ 
 'Name': ['Alice', 'Bob', 'Charlie'], 
 'Age': [25, 30, 35], 
 'Salary': [50000.50, 60000.75, 70000.00]
  }) 
print(df.dtypes)

#Write a code snippet that demonstrates how to fill missing values with the mean of a column. 
import pandas as pd 
df = pd.DataFrame({ 
'Age': [25, 30, None, 40, None]
  }) 
df['Age'] = df['Age'].fillna(df['Age'].mean())
print(df)
