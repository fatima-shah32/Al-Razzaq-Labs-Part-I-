import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.ensemble import RandomForestRegressor

# Create sample dataset
data = {
    "feature1": [10, 20, 30, 40, 50, 60, 70, 80],
    "feature2": [2, 4, 5, 8, 10, 12, 15, 16],
    "existing_feature": [5, 10, 15, 20, 25, 30, 35, 40],
    "target": [100, 180, 260, 350, 430, 510, 620, 700]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df.head())

# Create new features
df["feature_square"] = df["existing_feature"] ** 2
df["feature_log"] = np.log1p(df["existing_feature"])
df["feature_sqrt"] = np.sqrt(df["existing_feature"])
df["feature_interaction"] = df["feature1"] * df["feature2"]

print("\nDataset After Feature Engineering:")
print(df.head())

# Save dataset
df.to_csv("sample_data.csv", index=False)

# Correlation matrix
correlation_matrix = df.corr()

print("\nCorrelation Matrix:")
print(correlation_matrix)

# Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.close()

# Pairplot
sns.pairplot(df)
plt.savefig("pairplot.png")
plt.close()

# Feature importance
X = df.drop("target", axis=1)
y = df["target"]

model = RandomForestRegressor(random_state=1)
model.fit(X, y)

feature_importance = pd.DataFrame({
    "feature": X.columns,
    "importance": model.feature_importances_
}).sort_values(by="importance", ascending=False)

print("\nFeature Importance:")
print(feature_importance)

feature_importance.to_csv("feature_importance.csv", index=False)

print("\nFiles created successfully:")
print("sample_data.csv")
print("correlation_heatmap.png")
print("pairplot.png")
print("feature_importance.csv")
