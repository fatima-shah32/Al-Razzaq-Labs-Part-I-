import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

print("=== Lab 17: Feature Selection & Importance ===")

# Load Iris Dataset
iris = load_iris()

X = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

y = iris.target

print("\nDataset Shape:", X.shape)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Random Forest
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Feature importance
importances = model.feature_importances_

feature_importance_df = pd.DataFrame({
    "Feature": X.columns,
    "Importance": importances
}).sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature Importance Ranking:")
print(feature_importance_df)

# Plot feature importance
plt.figure(figsize=(8,5))
plt.bar(
    feature_importance_df["Feature"],
    feature_importance_df["Importance"]
)
plt.xticks(rotation=45)
plt.title("Feature Importance")
plt.tight_layout()
plt.savefig("feature_importance.png")
plt.close()

# Original model accuracy
y_pred_original = model.predict(X_test)

accuracy_original = accuracy_score(
    y_test,
    y_pred_original
)

# Remove low importance features
threshold = 0.10

low_importance_features = [
    feature
    for feature, importance
    in zip(X.columns, importances)
    if importance < threshold
]

print("\nRemoved Features:")
print(low_importance_features)

X_train_reduced = X_train.drop(
    columns=low_importance_features
)

X_test_reduced = X_test.drop(
    columns=low_importance_features
)

# Train reduced model
model_reduced = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model_reduced.fit(
    X_train_reduced,
    y_train
)

y_pred_reduced = model_reduced.predict(
    X_test_reduced
)

accuracy_reduced = accuracy_score(
    y_test,
    y_pred_reduced
)

print(f"\nAccuracy with all features: {accuracy_original:.2f}")
print(f"Accuracy with selected features: {accuracy_reduced:.2f}")

# Save report
with open("results.txt", "w") as file:
    file.write("Lab 17: Feature Selection & Importance\n\n")

    file.write("Feature Ranking:\n")
    file.write(feature_importance_df.to_string(index=False))

    file.write("\n\nRemoved Features:\n")
    file.write(str(low_importance_features))

    file.write(
        f"\n\nAccuracy with all features: {accuracy_original:.2f}"
    )

    file.write(
        f"\nAccuracy with selected features: {accuracy_reduced:.2f}"
    )

    file.write(
        "\n\nConclusion:\n"
        "Feature selection reduces complexity and can "
        "maintain similar performance while removing "
        "less useful features."
    )

print("\nResults saved in results.txt")
print("Feature importance chart saved as feature_importance.png")
print("\nLab completed successfully.")
