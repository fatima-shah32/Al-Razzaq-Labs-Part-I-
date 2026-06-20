import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


print("=== Lab 25: k-Nearest Neighbors Classification ===")

# Load Iris dataset
iris = load_iris()

data = pd.DataFrame(
    data=iris.data,
    columns=iris.feature_names
)

data["target"] = iris.target

print("\nDataset loaded successfully")
print(data.head())

# Split dataset
X = data.drop("target", axis=1)
y = data["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)

# Train k-NN model with k=3
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Predict and evaluate
predictions = knn.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nAccuracy with k=3:", accuracy)

# Experiment with different k values
accuracies = []

print("\nAccuracy for different k values:")

for k in range(1, 11):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)

    predictions = knn.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    accuracies.append(accuracy)

    print(f"Accuracy with k={k}: {accuracy}")

# Plot k values vs accuracy
plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), accuracies, marker="o")
plt.xlabel("k value")
plt.ylabel("Accuracy")
plt.title("k-NN Varying k Performance")
plt.xticks(range(1, 11))
plt.grid(True)
plt.savefig("knn_accuracy_plot.png")
plt.close()

print("\nAccuracy plot saved as knn_accuracy_plot.png")
