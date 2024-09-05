import pandas as pd

# Load the CSV files into DataFrames
df1 = pd.read_csv('modified_gender_data.csv')
df2 = pd.read_csv('Transformed Data Set - Sheet1.csv')

df1['Gender'] = df1['Gender'].replace({'Male': 'M', 'Female': 'F'})
# print(df1.Gender)

# print(df2.Gender)

# Merge the DataFrames on the 'Gender' column
merged_df = pd.merge(df1, df2, on='Gender')

# Display the first few rows of the merged DataFrame
# print(merged_df)


# groupBy_df = merged_df.groupby('Age')
# print(groupBy_df.head(5))

# Filter the DataFrame for 25-year-olds who drink wine
filtered_df = merged_df[(merged_df['Age'] == 25) & (merged_df['Favorite Beverage'] == 'Wine')]

# Display the filtered DataFrame
print(filtered_df.value_counts())

