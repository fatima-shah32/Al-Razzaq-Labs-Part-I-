import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


print("=== Lab 37: Simple Dimensionality Reduction with PCA ===")

# Task 1: Load dataset
iris = load_iris()
X = iris.data
y = iris.target

print("\nDataset loaded successfully")
print("Feature shape:", X.shape)
print("Target shape:", y.shape)
print("Feature names:", iris.feature_names)

# Task 2: Standardize data
scaler = StandardScaler()
X_std = scaler.fit_transform(X)

print("\nDataset standardized successfully")

# Task 3: Apply PCA
pca = PCA()
X_pca = pca.fit_transform(X_std)

print("\nPCA applied successfully")
print("Explained variance ratio:")
print(pca.explained_variance_ratio_)

# Task 4: Plot explained variance
plt.figure(figsize=(10, 7))

plt.plot(
    range(1, X.shape[1] + 1),
    pca.explained_variance_ratio_,
    marker="o",
    linestyle="--"
)

plt.title("Explained Variance by Principal Components")
plt.xlabel("Number of Components")
plt.ylabel("Explained Variance")
plt.grid(True)
plt.tight_layout()
plt.savefig("explained_variance.png")
plt.close()

print("\nExplained variance plot saved as explained_variance.png")

# Task 5: Select top 2 PCA components
X_pca_2 = X_pca[:, :2]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_pca_2,
    y,
    test_size=0.3,
    random_state=42
)

# Train Logistic Regression
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nLogistic Regression Accuracy using 2 PCA components:")
print(round(accuracy, 2))

# Save PCA data
pca_df = pd.DataFrame(
    X_pca_2,
    columns=["Principal_Component_1", "Principal_Component_2"]
)

pca_df["target"] = y
pca_df.to_csv("pca_reduced_data.csv", index=False)

print("\nReduced PCA data saved as pca_reduced_data.csv")

# PCA scatter plot
plt.figure(figsize=(8, 6))

plt.scatter(
    pca_df["Principal_Component_1"],
    pca_df["Principal_Component_2"],
    c=pca_df["target"],
    alpha=0.7
)

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA Reduced Data - Iris Dataset")
plt.tight_layout()
plt.savefig("pca_scatter_plot.png")
plt.close()

print("PCA scatter plot saved as pca_scatter_plot.png")

print("\nLab completed successfully.")
