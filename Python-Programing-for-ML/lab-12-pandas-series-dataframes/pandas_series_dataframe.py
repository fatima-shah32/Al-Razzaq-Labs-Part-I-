import pandas as pd

print("=== Lab 12: Working with Pandas - Series and DataFrames ===")

# Task 1: Create a Pandas Series
print("\nTask 1: Creating a Series")

data = [10, 20, 30, 40, 50]

series = pd.Series(data)

print("\nSeries:")
print(series)

# Series with custom index
series_with_index = pd.Series(
    data,
    index=["a", "b", "c", "d", "e"]
)

print("\nSeries with Custom Index:")
print(series_with_index)

# Task 2: Build a DataFrame from Dictionary
print("\nTask 2: Creating DataFrame")

data_dict = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data_dict)

print("\nDataFrame:")
print(df)

# Task 3: Access and Modify Data
print("\nTask 3: Accessing and Modifying Data")

# Access column
name_column = df["Name"]

print("\nName Column:")
print(name_column)

# Access row
first_row = df.loc[0]

print("\nFirst Row:")
print(first_row)

# Modify data
df.at[0, "Age"] = 26

print("\nAfter Updating Age:")
print(df)

# Add new column
df["Country"] = ["USA", "USA", "USA"]

print("\nAfter Adding Country Column:")
print(df)

# Save DataFrame
df.to_csv("employees.csv", index=False)

print("\nData saved to employees.csv")

print("\nLab completed successfully.")
