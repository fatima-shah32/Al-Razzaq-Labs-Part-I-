import numpy as np

from sklearn.datasets import load_iris
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


print("=== Lab 29: Implementing Cross-Validation in scikit-learn ===")

# Load Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

print("\nDataset loaded successfully")
print("Feature shape:", X.shape)
print("Target shape:", y.shape)

# Define number of folds
k = 5

kf = KFold(
    n_splits=k,
    shuffle=True,
    random_state=42
)

model = LogisticRegression(max_iter=200)

accuracies = []

# Apply k-fold cross-validation
fold_number = 1

for train_index, test_index in kf.split(X):
    X_train = X[train_index]
    X_test = X[test_index]

    y_train = y[train_index]
    y_test = y[test_index]

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    accuracies.append(accuracy)

    print(f"Fold {fold_number} Accuracy: {accuracy:.2f}")

    fold_number += 1

# Calculate overall performance
average_accuracy = np.mean(accuracies)
std_accuracy = np.std(accuracies)

print("\nAccuracies for each fold:", accuracies)
print(f"Average accuracy across {k} folds: {average_accuracy:.2f}")
print(f"Standard deviation across folds: {std_accuracy:.2f}")

print("\nInterpretation:")
print("Cross-validation gives a more reliable model evaluation.")
print("Low variation between folds shows that the model is stable.")
