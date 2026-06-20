import pandas as pd

print("=== Lab 13: Loading CSV Data with Pandas ===")

# Create sample CSV data
sample_data = {
    "Name": ["Ali", "Sara", "Ahmed", None, "Fatima"],
    "Age": [22, 25, 28, 30, None],
    "City": ["Lahore", "Karachi", None, "Islamabad", "Quetta"]
}

df_sample = pd.DataFrame(sample_data)

# Save sample CSV
df_sample.to_csv("sample_data.csv", index=False)

print("\nSample CSV file created successfully")

# Load CSV file
df = pd.read_csv("sample_data.csv")

print("\nCSV Loaded Successfully")

# Display first rows
print("\nFirst Five Rows:")
print(df.head())

# Display DataFrame information
print("\nDataset Information:")
print(df.info())

# Check missing values
print("\nMissing Values Count:")
print(df.isnull().sum())

print("\nLab completed successfully.")
