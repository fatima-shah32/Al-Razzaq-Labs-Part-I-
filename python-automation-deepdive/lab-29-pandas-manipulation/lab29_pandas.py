import pandas as pd

# Task 2: Read CSV
df = pd.read_csv("employees.csv")
print("\n📊 Original Data:")
print(df)

# Task 3: Filter rows where Age > 30
filtered_df = df[df["Age"] > 30]

print("\n🔎 Filtered Data (Age > 30):")
print(filtered_df)

# Task 4: Save filtered data
filtered_df.to_csv("filtered_data.csv", index=False)

print("\n✅ Filtered data saved to filtered_data.csv")
