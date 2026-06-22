import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

print("=== Lab 11: K-Nearest Neighbors Classification ===")

# Task 1: Load Iris dataset
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
    test_size=0.2,
    random_state=42
)

print("\nTraining data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)

# Task 2: Train KNN model with k=3
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nKNN Accuracy with k=3:")
print(round(accuracy, 2))

# Task 3: Test different k values
k_values = range(1, 16)
accuracies = []

for k in k_values:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    acc = accuracy_score(y_test, predictions)
    accuracies.append(acc)

    print(f"k={k}, Accuracy={acc:.2f}")

# Save results
results_df = pd.DataFrame({
    "k_value": list(k_values),
    "accuracy": accuracies
})

results_df.to_csv("knn_accuracy_results.csv", index=False)

# Plot accuracy results
plt.figure(figsize=(8, 5))
plt.plot(k_values, accuracies, marker="o")
plt.xlabel("Number of Neighbors k")
plt.ylabel("Accuracy")
plt.title("KNN Accuracy for Different k Values")
plt.grid(True)
plt.tight_layout()
plt.savefig("knn_accuracy_plot.png")
plt.close()

print("\nAccuracy results saved as knn_accuracy_results.csv")
print("Accuracy plot saved as knn_accuracy_plot.png")

print("\nLab completed successfully.")
