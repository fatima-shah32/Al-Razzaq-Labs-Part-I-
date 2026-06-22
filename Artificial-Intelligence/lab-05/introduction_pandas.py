import pandas as pd

print("=== Lab 05: Introduction to Pandas ===")

# Task 1: Load CSV File
df = pd.read_csv("data.csv")

print("\nOriginal Data:")
print(df)

# Task 2: View First Few Rows
print("\nFirst Five Rows:")
print(df.head())

# Basic Statistics
print("\nBasic Statistics:")
print(df.describe())

# Task 3: Find Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove Missing Values
df_cleaned = df.dropna()

print("\nCleaned Data:")
print(df_cleaned)

# Verify Cleaning
print("\nMissing Values After Cleaning:")
print(df_cleaned.isnull().sum())

print("\nLab completed successfully.")
