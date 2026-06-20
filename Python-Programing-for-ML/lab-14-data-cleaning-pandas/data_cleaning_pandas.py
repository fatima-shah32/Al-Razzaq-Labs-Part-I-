import pandas as pd

print("=== Lab 14: Data Cleaning using Pandas ===")

# Create sample dataset with missing values, duplicates, and messy text
data = {
    "Name": [" Ali ", "Sara", "Ahmed", "Sara", "Fatima", None],
    "Age": [22, 25, None, 25, 30, 28],
    "City": [" Lahore ", "Karachi", " Islamabad ", "Karachi", None, "Quetta"],
    "Salary": [50000, 60000, 55000, 60000, None, 45000]
}

df = pd.DataFrame(data)

# Save sample data
df.to_csv("example_data.csv", index=False)

print("\nOriginal Dataset:")
print(df)

# Task 1: Check missing values
missing_values_count = df.isnull().sum()

print("\nMissing Values Count:")
print(missing_values_count)

# Task 1: Check duplicate rows
duplicate_rows = df.duplicated().sum()

print("\nNumber of duplicate rows:", duplicate_rows)

# Remove duplicate rows
df_no_duplicates = df.drop_duplicates()

print("\nDataset After Removing Duplicates:")
print(df_no_duplicates)

# Task 2: Remove rows with missing values
cleaned_df = df_no_duplicates.dropna()

print("\nDataset After dropna():")
print(cleaned_df)

# Task 2: Fill missing values
filled_df = df_no_duplicates.fillna({
    "Name": "Unknown",
    "Age": df_no_duplicates["Age"].mean(),
    "City": "Unknown",
    "Salary": df_no_duplicates["Salary"].mean()
})

print("\nDataset After fillna():")
print(filled_df)

# Task 3: Strip whitespace from string columns
filled_df["Name"] = filled_df["Name"].str.strip()
filled_df["City"] = filled_df["City"].str.strip()

# Task 3: Change data types
filled_df["Age"] = filled_df["Age"].astype(float)
filled_df["Salary"] = filled_df["Salary"].astype(float)

# Task 3: Rename columns
filled_df = filled_df.rename(columns={
    "Name": "Employee_Name",
    "Age": "Employee_Age",
    "City": "Employee_City",
    "Salary": "Employee_Salary"
})

print("\nFinal Cleaned Dataset:")
print(filled_df)

# Save cleaned dataset
filled_df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned dataset saved as cleaned_data.csv")
