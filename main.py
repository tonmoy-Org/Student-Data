import pandas as pd

df = pd.read_csv('genderClass.csv')

print(df.head(2))
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
df['Height'] = df['Height'].fillna(df['Height'].mean())


# print(df.isnull().sum())

# Calculate the frequency of each hair color
hairFrequency = df['HairColor'].value_counts()

# Find the most frequent hair color
most_frequent_hair_color = hairFrequency.idxmax()

# Fill missing values in the 'HairColor' column with the most frequent hair color
df['HairColor'].fillna(most_frequent_hair_color, inplace=True)

print(df.isnull().sum())


print(df['HairColor'].head(15))
