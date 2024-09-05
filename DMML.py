import pandas as pd

df = pd.read_csv('weather_data.csv')
gf = pd.read_csv('modified_gender.csv')
tf = pd.read_csv('Transformed Data Set - Sheet1.csv')

# print(df)
# print(df.head(4))

# print(df.tail(3))
# print(df.dtypes)
# print(df.shape)

# print(df.columns)
# print(df['event'])

# print(df['event'].value_counts())

# print(df.isnull().sum())

# print(df[['temperature', 'event']])
# print(df.temperature)

# print(df.event)


print(tf)
