import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


print("=== Lab 22: Evaluating Regression Models ===")

# Load dataset
housing = fetch_california_housing()

X = pd.DataFrame(
    housing.data,
    columns=housing.feature_names
)

y = pd.Series(
    housing.target,
    name="HouseValue"
)

print("\nDataset loaded successfully")
print("Feature shape:", X.shape)
print("Target shape:", y.shape)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)

# Train Linear Regression model
model = LinearRegression()

model.fit(X_train, y_train)

print("\nLinear Regression model trained successfully")

# Make predictions
y_pred = model.predict(X_test)

print("\nSample Predictions:")
print(y_pred[:5])

# Calculate Mean Squared Error
mse = mean_squared_error(y_test, y_pred)

# Calculate R² Score
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation Metrics")
print("Mean Squared Error (MSE):", round(mse, 4))
print("R² Score:", round(r2, 4))

# Plot predictions vs actual values
plt.figure(figsize=(8, 6))

plt.scatter(
    y_test,
    y_pred,
    alpha=0.6
)

plt.plot(
    [min(y_test), max(y_test)],
    [min(y_test), max(y_test)],
    color="red",
    linewidth=2
)

plt.title("Actual vs Predicted Values")
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")

plt.tight_layout()
plt.savefig("actual_vs_predicted.png")
plt.close()

print("\nPlot saved as actual_vs_predicted.png")
