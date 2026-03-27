import pandas as pd
data = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
                     'Age': [25, 30, 35, 40, 45],   
                        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']})
print(data)
data['Age in 5 years'] = data['Age'] + 5
print(data)


import csv
df = pd.read_csv("exp1.csv")
print("DataFrame from CSV:")
print(df)
print("Dimensions of the DataFrame:", df.shape)
print("Head of the DataFrame:")
print(df.head(6))
print("Basic Information of the DataFrame:")
print(df.info())
print("Summary Statistics of the DataFrame:")
print(df.describe())

#finding null values and replacing them with mean 
df =pd.read_csv("null_data.csv")
print("DataFrame with Null Values:")
print(df)
print("Null Values in the DataFrame:")
print(df.isnull() , inplace = True)
df = df.fillna(df.mean())
print("DataFrame after Filling Null Values with Mean:")
df_filled = df.fillna(df.mean())
print(df_filled)

#mean median mode etc
print("Mean of the DataFrame:")
print(df.mean())
print("Median of the DataFrame:")
print(df.median())
print("Mode of the DataFrame:")
print(df.mode())
print("Standard Deviation of the DataFrame:")
print(df.std())
print("Variance of the DataFrame:")
print(df.var())
print("Minimum Value in the DataFrame:")
print(df.min())
print("Maximum Value in the DataFrame:")
print(df.max()) 
