import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

print("=== Lab 14: Train-Test Split & Cross-Validation ===")

# Task 1: Load Iris dataset
iris_data = load_iris()

df = pd.DataFrame(
    data=iris_data.data,
    columns=iris_data.feature_names
)

df["target"] = iris_data.target

print("\nDataset Preview:")
print(df.head())

# Define features and target
X = df.drop("target", axis=1)
y = df["target"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)

# Task 2: Logistic Regression model
model = LogisticRegression(max_iter=200)

# Cross-validation
cv_scores = cross_val_score(
    model,
    X,
    y,
    cv=5
)

print("\nCross-validation scores:")
print(cv_scores)

print("\nMean CV score:")
print(round(cv_scores.mean(), 4))

# Task 3: Train-test split evaluation
model.fit(X_train, y_train)

test_score = model.score(X_test, y_test)

print("\nTest score using train-test split:")
print(round(test_score, 4))

# Save results
results = pd.DataFrame({
    "Evaluation_Method": [
        "Train-Test Split",
        "5-Fold Cross-Validation Mean"
    ],
    "Score": [
        test_score,
        cv_scores.mean()
    ]
})

results.to_csv("evaluation_results.csv", index=False)

with open("evaluation_summary.txt", "w") as file:
    file.write("Lab 14: Train-Test Split & Cross-Validation\n\n")
    file.write(f"Train-Test Split Score: {round(test_score, 4)}\n")
    file.write(f"Cross-Validation Scores: {cv_scores}\n")
    file.write(f"Mean Cross-Validation Score: {round(cv_scores.mean(), 4)}\n\n")
    file.write("Train-test split gives one performance estimate.\n")
    file.write("Cross-validation gives a more stable estimate by using multiple folds.\n")

print("\nResults saved as evaluation_results.csv")
print("Summary saved as evaluation_summary.txt")

print("\nLab completed successfully.")
