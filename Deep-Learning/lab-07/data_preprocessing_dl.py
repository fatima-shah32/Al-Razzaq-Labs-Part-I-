import numpy as np
import pandas as pd

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

print("=== Lab 07: Data Preprocessing for Deep Learning ===")

# Task 1: Sample data
data = np.array([
    [10, 2.7, 3.6],
    [-100, 5, -2],
    [120, 20, 40]
], dtype=np.float64)

print("\nOriginal Data:")
print(data)

# Normalize data using MinMaxScaler
minmax_scaler = MinMaxScaler()
normalized_data = minmax_scaler.fit_transform(data)

print("\nNormalized Data:")
print(normalized_data)

# Standardize data using StandardScaler
standard_scaler = StandardScaler()
standardized_data = standard_scaler.fit_transform(data)

print("\nStandardized Data:")
print(standardized_data)

# Save preprocessing results
normalized_df = pd.DataFrame(
    normalized_data,
    columns=["Feature_1", "Feature_2", "Feature_3"]
)

standardized_df = pd.DataFrame(
    standardized_data,
    columns=["Feature_1", "Feature_2", "Feature_3"]
)

normalized_df.to_csv("normalized_data.csv", index=False)
standardized_df.to_csv("standardized_data.csv", index=False)

# Task 2: Split data into training and testing sets
np.random.seed(42)

X = np.random.rand(100, 5)
y = np.random.randint(0, 2, 100)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

print("\nTraining Features Shape:", X_train.shape)
print("Testing Features Shape:", X_test.shape)
print("Training Target Shape:", y_train.shape)
print("Testing Target Shape:", y_test.shape)

# Save split information
split_info = {
    "Dataset": ["Training Features", "Testing Features", "Training Target", "Testing Target"],
    "Shape": [str(X_train.shape), str(X_test.shape), str(y_train.shape), str(y_test.shape)]
}

split_df = pd.DataFrame(split_info)
split_df.to_csv("train_test_split_info.csv", index=False)

# Task 3: Documentation report
with open("preprocessing_report.txt", "w") as file:
    file.write("Lab 07: Data Preprocessing for Deep Learning\n\n")
    file.write("Step 1: Normalization\n")
    file.write("MinMaxScaler was used to scale data into the range [0, 1].\n\n")

    file.write("Step 2: Standardization\n")
    file.write("StandardScaler was used to transform data with mean 0 and standard deviation 1.\n\n")

    file.write("Step 3: Train-Test Split\n")
    file.write("Data was split into 70% training and 30% testing using train_test_split.\n\n")

    file.write("Training Features Shape: " + str(X_train.shape) + "\n")
    file.write("Testing Features Shape: " + str(X_test.shape) + "\n")
    file.write("Training Target Shape: " + str(y_train.shape) + "\n")
    file.write("Testing Target Shape: " + str(y_test.shape) + "\n\n")

    file.write("Conclusion:\n")
    file.write("Preprocessing is important because it prepares raw data for deep learning models.\n")

print("\nFiles created:")
print("normalized_data.csv")
print("standardized_data.csv")
print("train_test_split_info.csv")
print("preprocessing_report.txt")

print("\nLab completed successfully.")
