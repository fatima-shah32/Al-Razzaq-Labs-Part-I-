import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

print("=== Lab 40: Final Mini AI Project ===")
print("Project: House Price Prediction")

# Step 1: Load dataset
housing = fetch_california_housing()

df = pd.DataFrame(
    housing.data,
    columns=housing.feature_names
)

df["target"] = housing.target

print("\nDataset loaded successfully")
print(df.head())

# Step 2: Data cleaning
print("\nMissing Values:")
print(df.isnull().sum())

df.fillna(df.mean(), inplace=True)

print("\nMissing values handled successfully")

# Step 3: Feature engineering
scaler = StandardScaler()

df["scaled_income"] = scaler.fit_transform(
    df[["MedInc"]]
)

print("\nNew feature created: scaled_income")

# Correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(
    df.corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Feature Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.close()

print("Correlation heatmap saved as correlation_heatmap.png")

# Step 4: Model selection
X = df.drop("target", axis=1)
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("\nModel trained successfully")

# Step 5: Model evaluation
predictions = model.predict(X_test)

mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, predictions)

print("\nModel Evaluation Results:")
print("RMSE:", round(rmse, 4))
print("R2 Score:", round(r2, 4))

# Actual vs Predicted plot
plt.figure(figsize=(8, 6))
plt.scatter(y_test, predictions, alpha=0.5)
plt.xlabel("Actual House Prices")
plt.ylabel("Predicted House Prices")
plt.title("Actual vs Predicted House Prices")
plt.tight_layout()
plt.savefig("actual_vs_predicted.png")
plt.close()

print("Actual vs predicted plot saved as actual_vs_predicted.png")

# Feature importance
feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
}).sort_values(by="Importance", ascending=False)

print("\nFeature Importance:")
print(feature_importance)

feature_importance.to_csv("feature_importance.csv", index=False)

print("\nFeature importance saved as feature_importance.csv")
print("\nFinal Mini AI Project completed successfully.")
