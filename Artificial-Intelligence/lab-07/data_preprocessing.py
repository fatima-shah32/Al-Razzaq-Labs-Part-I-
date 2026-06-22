import pandas as pd
from sklearn.preprocessing import MinMaxScaler

print("=== Lab 07: Data Preprocessing Techniques ===")

# Create sample dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Age": [25, 30, None, 28, 35],
    "Salary": [50000, 60000, 55000, None, 70000],
    "Department": ["HR", "IT", "Finance", "IT", "HR"]
}

df = pd.DataFrame(data)
df.to_csv("sample_data.csv", index=False)

print("\nOriginal Data:")
print(df)

# Task 1: Identify Missing Data
print("\nMissing Values:")
print(df.isnull().sum())

# Drop missing values
df_dropped = df.dropna()

print("\nData After Dropping Missing Values:")
print(df_dropped)

# Fill missing values with mean for numeric columns only
df_filled = df.copy()

numeric_columns = df_filled.select_dtypes(include=["number"]).columns

df_filled[numeric_columns] = df_filled[numeric_columns].fillna(
    df_filled[numeric_columns].mean()
)

print("\nData After Filling Missing Values:")
print(df_filled)

# Task 2: Normalize numeric column using Min-Max Scaling
scaler = MinMaxScaler()

df_filled["normalized_salary"] = scaler.fit_transform(
    df_filled[["Salary"]]
)

print("\nNormalized Salary:")
print(df_filled[["Salary", "normalized_salary"]])

# Task 3: One-Hot Encoding
df_encoded = pd.get_dummies(
    df_filled,
    columns=["Department"]
)

print("\nOne-Hot Encoded Data:")
print(df_encoded)

# Save processed data
df_encoded.to_csv("processed_data.csv", index=False)

print("\nProcessed data saved as processed_data.csv")
print("\nLab completed successfully.")
