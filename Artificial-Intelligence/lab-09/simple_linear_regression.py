import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

print("=== Lab 09: Simple Linear Regression Concept ===")

# Task 1: Create and load small dataset
data = {
    "Size": [1500, 1600, 1700, 1800, 1900, 2000, 2100],
    "Price": [250000, 270000, 290000, 310000, 330000, 350000, 370000]
}

df = pd.DataFrame(data)

print("\nDataset:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Task 2: Prepare data
X = df[["Size"]]
y = df["Price"]

# Create and train model
model = LinearRegression()
model.fit(X, y)

# Get coefficient and intercept
coefficient = model.coef_[0]
intercept = model.intercept_

print("\nModel Results:")
print("Coefficient/Slope:", coefficient)
print("Intercept:", intercept)

# Predict prices
df["Predicted_Price"] = model.predict(X)

print("\nDataset with Predictions:")
print(df)

# Save dataset
df.to_csv("house_price_predictions.csv", index=False)

# Task 3: Plot regression line
plt.figure(figsize=(8, 6))
plt.scatter(X, y, label="Data Points")
plt.plot(X, model.predict(X), linewidth=2, label="Regression Line")

plt.xlabel("Size (sq ft)")
plt.ylabel("Price (USD)")
plt.title("Simple Linear Regression: House Size vs Price")
plt.legend()
plt.tight_layout()
plt.savefig("linear_regression_plot.png")
plt.close()

print("\nPlot saved as linear_regression_plot.png")
print("Predictions saved as house_price_predictions.csv")

print("\nInterpretation:")
print("The positive slope shows that house price increases as house size increases.")

print("\nLab completed successfully.")
