import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

print("=== Lab 16: Feature Scaling (Standardization) ===")

# Create sample dataset
np.random.seed(42)

data = {
    "Feature1": np.random.randint(0, 100, 100),
    "Feature2": np.random.randint(100, 200, 100),
    "Target": np.random.choice([0, 1], 100)
}

df = pd.DataFrame(data)

print("\nOriginal Dataset:")
print(df.head())

# Separate features and target
X = df[["Feature1", "Feature2"]]
y = df["Target"]

# Standardization
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_scaled_df = pd.DataFrame(
    X_scaled,
    columns=X.columns
)

print("\nScaled Features:")
print(X_scaled_df.head())

# Model before scaling
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

original_accuracy = accuracy_score(y_test, y_pred)

print(f"\nAccuracy without scaling: {original_accuracy:.2f}")

# Model after scaling
X_train_scaled, X_test_scaled, y_train_scaled, y_test_scaled = train_test_split(
    X_scaled_df,
    y,
    test_size=0.2,
    random_state=42
)

model_scaled = LogisticRegression(max_iter=1000)
model_scaled.fit(X_train_scaled, y_train_scaled)

y_pred_scaled = model_scaled.predict(X_test_scaled)

scaled_accuracy = accuracy_score(
    y_test_scaled,
    y_pred_scaled
)

print(f"Accuracy with scaling: {scaled_accuracy:.2f}")

# Save report
with open("results.txt", "w") as file:
    file.write("Lab 16: Feature Scaling (Standardization)\n\n")
    file.write(f"Accuracy without scaling: {original_accuracy:.2f}\n")
    file.write(f"Accuracy with scaling: {scaled_accuracy:.2f}\n\n")

    file.write("Observation:\n")
    file.write(
        "Feature scaling standardizes numerical features by "
        "removing the mean and scaling to unit variance.\n"
    )
    file.write(
        "Models such as Logistic Regression generally perform "
        "better and converge faster when features are scaled.\n"
    )

print("\nResults saved in results.txt")
print("\nLab completed successfully.")
