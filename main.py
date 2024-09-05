import pandas as pd

df = pd.read_csv('genderClass.csv')

print(df.head())
print(df.tail(3))
print(df.shape)
print(df.columns)

print(df[['HairColor', 'Height']])
print(df.HairColor)

print(df.size)
print(df.dtypes)

print(df.values)
print(df.index)

df['Age'] = df['Age'].fillna(df['Age'].mean())
print(df['Age'].isnull().sum())
df['Height'] = df['Height'].fillna(df['Height'].mean())
print(df.isnull().sum())

# Calculate the frequency of each hair color
hairFrequency = df['HairColor'].value_counts()
print(hairFrequency)

#  Apply one-hot encoding to the 'Color' column
one_hot_encoded_df = pd.get_dummies(df['HairColor'], columns='HairColor')
print(one_hot_encoded_df)

# Find the most frequent hair color
most_frequent_hair_color = hairFrequency.idxmax()
min_frequent_hair_color = hairFrequency.idxmin()
print(most_frequent_hair_color)
print(min_frequent_hair_color)

# Fill missing values in the 'HairColor' column with the most frequent hair color
df['HairColor'].fillna(most_frequent_hair_color, inplace=True)

print(df.isnull().sum())

print(df['HairColor'].head(5))
