import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler

print("=== Lab 19: Data Scaling with StandardScaler ===")

# Create sample dataset
data = {
    "Feature1": [140, 150, 155, 160, 165],
    "Feature2": [200, 210, 215, 220, 225]
}

df = pd.DataFrame(data)

print("\nOriginal Data:")
print(df)

# Initialize scaler
scaler = StandardScaler()

# Scale data
scaled_data = scaler.fit_transform(df)

# Convert to DataFrame
scaled_df = pd.DataFrame(
    scaled_data,
    columns=df.columns
)

print("\nScaled Data:")
print(scaled_df)

# Compare statistics
print("\nOriginal Data Statistics:")
print(df.describe())

print("\nScaled Data Statistics:")
print(scaled_df.describe())

# Plot original data
plt.figure(figsize=(8, 5))
df.plot(kind="bar")
plt.title("Original Data")
plt.tight_layout()
plt.savefig("original_data.png")
plt.close()

# Plot scaled data
plt.figure(figsize=(8, 5))
scaled_df.plot(kind="bar")
plt.title("Scaled Data")
plt.tight_layout()
plt.savefig("scaled_data.png")
plt.close()

print("\nPlots saved:")
print("original_data.png")
print("scaled_data.png")

print("\nAnalysis:")
print("After scaling, feature values have mean close to 0")
print("and standard deviation close to 1.")
