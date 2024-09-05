import pandas as pd

# Sample data
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Score': [90, 85, 88, 92]
})

df2 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Subject': ['Math', 'Science', 'History', 'Math'],
    'Marks': [95, 80, 78, 99]
})

# Merge DataFrames on 'ID'
merged_df = pd.merge(df1, df2, on='ID')
# print(merged_df)

# Group by 'Subject' and calculate the mean of 'Score' and 'Marks'
grouped_df = merged_df.groupby('Subject').agg({
    'Score': 'mean',
    'Marks': 'mean'
})

print(grouped_df)
