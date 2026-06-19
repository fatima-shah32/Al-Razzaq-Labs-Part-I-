import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

print("Dataset loaded successfully")
print("Feature shape:", X.shape)
print("Target shape:", y.shape)
print("Target classes:", iris.target_names)

# Split dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create SVC model
model = SVC()

# Define parameter grid
param_grid = {
    "C": [0.1, 1, 10, 100],
    "gamma": [1, 0.1, 0.01, 0.001],
    "kernel": ["linear", "rbf"]
}

# Set up GridSearchCV
grid_search = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=5,
    scoring="accuracy",
    verbose=2,
    n_jobs=-1
)

# Fit GridSearchCV
print("\nStarting GridSearchCV...")
grid_search.fit(X_train, y_train)

# Display best parameters and score
print("\nBest Parameters:")
print(grid_search.best_params_)

print(f"\nBest Cross-Validation Accuracy: {grid_search.best_score_:.2f}")

# Get best model
best_model = grid_search.best_estimator_

# Evaluate on test data
y_pred = best_model.predict(X_test)

test_accuracy = accuracy_score(y_test, y_pred)

print(f"\nTest Set Accuracy: {test_accuracy:.2f}")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# Show full GridSearch results
results = pd.DataFrame(grid_search.cv_results_)

print("\nTop 5 Grid Search Results:")
print(
    results[
        ["param_C", "param_gamma", "param_kernel", "mean_test_score", "rank_test_score"]
    ].sort_values(by="rank_test_score").head()
)
