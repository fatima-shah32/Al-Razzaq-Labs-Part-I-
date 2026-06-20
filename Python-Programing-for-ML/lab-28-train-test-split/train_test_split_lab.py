import numpy as np
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

print("=== Lab 28: Train-Test Split ===")

# Load Iris dataset
data = load_iris()

X = data.data
y = data.target

print("\nDataset Loaded Successfully")
print("Total Samples:", len(X))
print("Features Shape:", X.shape)
print("Target Shape:", y.shape)

# Split dataset (80/20)
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\n=== Standard Split (80/20) ===")
print("Training data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)

# Split dataset with stratification
X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\n=== Stratified Split (80/20) ===")
print("Training data shape:", X_train_s.shape)
print("Testing data shape:", X_test_s.shape)

print("\nTraining Samples:", len(X_train))
print("Testing Samples:", len(X_test))

print("\nTraining data is used to fit the model.")
print("Testing data is used to evaluate model performance.")
