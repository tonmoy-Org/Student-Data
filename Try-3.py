import pandas as pd

# Sample data
df1 = pd.DataFrame({
    'EmployeeID': [1, 2, 3, 4],
    'Department': ['HR', 'IT', 'IT', 'HR'],
    'Salary': [50000, 60000, 55000, 52000]
})

df2 = pd.DataFrame({
    'EmployeeID': [1, 2, 3, 4],
    'YearsExperience': [5, 7, 5, 3],
    'PerformanceScore': [88, 92, 85, 90]
})

# Merge the dataframes on 'EmployeeID'
merged_df = pd.merge(df1, df2, on='EmployeeID')

# Print the merged DataFrame
print("Merged DataFrame:")
print(merged_df)

# Group by 'Department' and calculate mean salary and performance score
groupBy_df = merged_df.groupby('Department').agg({
    'Salary': 'mean',
    'PerformanceScore': 'mean'
})

# Print the result
print("\nGrouped and Aggregated DataFrame:")
print(groupBy_df)

# Count unique values in the 'Department' column
unique_count = merged_df['Department'].value_counts()
print(unique_count)

# Filter rows where Salary is greater than 52000
high_salary_df = merged_df[merged_df['Salary'] > 52000]
print(high_salary_df)

# Sort by 'PerformanceScore' in descending order
descending_order = merged_df.sort_values(by="PerformanceScore", ascending=True)
print(descending_order)

# Create a pivot table to show average Salary and PerformanceScore by Department

pivot_table = pd.pivot_table(merged_df, values=["Salary", "PerformanceScore"], index="Department", aggfunc="mean")
print(pivot_table)

# Fill missing values in 'YearsExperience' with the mean of the column
merged_df['YearsExperience'] = merged_df['YearsExperience'].fillna(merged_df['YearsExperience'].mean())
print(merged_df)

# Group by 'Department' and apply multiple aggregation functions
agg_df = merged_df.groupby('Department').agg({
    "Salary": ['mean', 'max', 'min'],
    "PerformanceScore": ['mean', 'max']
})

print(agg_df)

# Drop the 'YearsExperience' column
dropped_df = merged_df.drop(columns=['YearsExperience'])
print(dropped_df)

# Perform a left join (include all rows from df1)
left_join_df = pd.merge(df1, df2, on="EmployeeID", how='left')

print(left_join_df)
