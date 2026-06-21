import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


print("=== Lab 39: Introduction to Ensemble Methods ===")

# Step 1: Load dataset
data = load_iris()
X = data.data
y = data.target

print("\nDataset loaded successfully")
print("Feature shape:", X.shape)
print("Target shape:", y.shape)
print("Target classes:", data.target_names)

# Step 2: Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

print("\nTraining data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)

# Task 1: Train Random Forest model
rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

y_pred_rf = rf_model.predict(X_test)
rf_accuracy = accuracy_score(y_test, y_pred_rf)

print("\nRandom Forest Accuracy:", round(rf_accuracy, 2))

# Task 2: Train Single Decision Tree model
dt_model = DecisionTreeClassifier(
    random_state=42
)

dt_model.fit(X_train, y_train)

y_pred_dt = dt_model.predict(X_test)
dt_accuracy = accuracy_score(y_test, y_pred_dt)

print("Decision Tree Accuracy:", round(dt_accuracy, 2))

# Task 3: Train Gradient Boosting model
gb_model = GradientBoostingClassifier(
    n_estimators=100,
    random_state=42
)

gb_model.fit(X_train, y_train)

y_pred_gb = gb_model.predict(X_test)
gb_accuracy = accuracy_score(y_test, y_pred_gb)

print("Gradient Boosting Accuracy:", round(gb_accuracy, 2))

# Comparison table
results = pd.DataFrame({
    "Model": [
        "Decision Tree",
        "Random Forest",
        "Gradient Boosting"
    ],
    "Technique": [
        "Single Model",
        "Bagging",
        "Boosting"
    ],
    "Accuracy": [
        dt_accuracy,
        rf_accuracy,
        gb_accuracy
    ]
})

print("\nModel Comparison:")
print(results)

# Save results
results.to_csv("model_comparison.csv", index=False)

print("\nResults saved as model_comparison.csv")

print("\nAnalysis:")
print("Decision Tree is a single model.")
print("Random Forest uses Bagging and reduces variance.")
print("Gradient Boosting uses Boosting and improves weak models step by step.")

print("\nLab completed successfully.")
