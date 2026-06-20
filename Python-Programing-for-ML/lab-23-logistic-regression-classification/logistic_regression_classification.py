import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix


print("=== Lab 23: Logistic Regression for Classification ===")

# Load Iris dataset
iris = load_iris()

X = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

y = pd.Series(iris.target)

# Filter dataset for binary classification
X = X[y != 2]
y = y[y != 2]

print("\nBinary classification dataset prepared")
print("Feature shape:", X.shape)
print("Target shape:", y.shape)
print("Target classes used: 0 and 1")

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)

# Train Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

print("\nLogistic Regression model trained successfully")

# Make predictions
y_pred = model.predict(X_test)

print("\nPredicted Labels:")
print(y_pred)

print("\nActual Labels:")
print(y_test.values)

# Evaluate model accuracy
accuracy = accuracy_score(y_test, y_pred)

print(f"\nModel Accuracy: {accuracy:.2f}")

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

# Plot actual vs predicted labels
plt.figure(figsize=(8, 5))
plt.plot(y_test.values, marker="o", label="Actual")
plt.plot(y_pred, marker="x", label="Predicted")
plt.xlabel("Sample Index")
plt.ylabel("Class Label")
plt.title("Actual vs Predicted Labels")
plt.legend()
plt.tight_layout()
plt.savefig("actual_vs_predicted.png")
plt.close()

print("\nPlot saved as actual_vs_predicted.png")
