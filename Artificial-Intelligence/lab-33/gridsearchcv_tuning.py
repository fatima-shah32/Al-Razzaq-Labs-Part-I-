import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


print("=== Lab 33: Hyperparameter Tuning with GridSearchCV ===")

# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

print("\nDataset loaded successfully")
print("Feature shape:", X.shape)
print("Target shape:", y.shape)
print("Target classes:", iris.target_names)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

print("\nTraining data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)

# Define parameter grid
param_grid = {
    "C": [0.1, 1, 10, 100],
    "gamma": [1, 0.1, 0.01, 0.001],
    "kernel": ["rbf", "linear"]
}

print("\nParameter Grid:")
print(param_grid)

# Setup GridSearchCV
grid = GridSearchCV(
    SVC(),
    param_grid,
    refit=True,
    verbose=2,
    cv=5
)

# Fit GridSearchCV
grid.fit(X_train, y_train)

print("\nBest Parameters Found:")
print(grid.best_params_)

print("\nBest Cross-Validation Score:")
print(round(grid.best_score_, 4))

# Make predictions
grid_predictions = grid.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, grid_predictions)

print("\nTest Accuracy:")
print(round(accuracy, 4))

print("\nClassification Report:")
report = classification_report(y_test, grid_predictions)
print(report)

print("\nConfusion Matrix:")
cm = confusion_matrix(y_test, grid_predictions)
print(cm)

# Save results
results_df = pd.DataFrame(grid.cv_results_)
results_df.to_csv("gridsearch_results.csv", index=False)

with open("model_evaluation_report.txt", "w") as file:
    file.write("Lab 33: Hyperparameter Tuning with GridSearchCV\n\n")
    file.write(f"Best Parameters: {grid.best_params_}\n")
    file.write(f"Best Cross-Validation Score: {round(grid.best_score_, 4)}\n")
    file.write(f"Test Accuracy: {round(accuracy, 4)}\n\n")
    file.write("Classification Report:\n")
    file.write(report)
    file.write("\nConfusion Matrix:\n")
    file.write(str(cm))

print("\nGridSearch results saved as gridsearch_results.csv")
print("Model evaluation report saved as model_evaluation_report.txt")

print("\nLab completed successfully.")
