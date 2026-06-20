import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


print("=== Lab 21: Building a Simple Linear Regression Model ===")

# Load California Housing dataset
housing_dataset = fetch_california_housing()

housing = pd.DataFrame(
    housing_dataset.data,
    columns=housing_dataset.feature_names
)

housing["PRICE"] = housing_dataset.target

print("\nDataset Preview:")
print(housing.head())

print("\nDataset Summary:")
print(housing.describe())

print("\nMissing Values:")
print(housing.isnull().sum())

# Define features and target
X = housing.drop("PRICE", axis=1)
y = housing["PRICE"]

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)

# Train Linear Regression model
lin_reg_model = LinearRegression()
lin_reg_model.fit(X_train, y_train)

print("\nLinear Regression model trained successfully")

# Make predictions
y_pred = lin_reg_model.predict(X_test)

print("\nSample Predictions:")
print(y_pred[:5])

# Evaluate model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print(f"Mean Squared Error: {mse:.4f}")
print(f"R-squared: {r2:.4f}")

# Visualize actual vs predicted values
plt.figure(figsize=(10, 6))

plt.scatter(
    y_test,
    y_pred,
    alpha=0.6
)

plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted Prices")

plt.plot(
    [min(y_test), max(y_test)],
    [min(y_test), max(y_test)],
    color="red",
    linewidth=2
)

plt.tight_layout()
plt.savefig("actual_vs_predicted_prices.png")
plt.close()

print("\nPlot saved as actual_vs_predicted_prices.png")
