import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

print("=== Lab 11: Model Evaluation Using a Confusion Matrix ===")

# Task 1: Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

print("\nDataset loaded successfully")
print("Feature shape:", X.shape)
print("Target shape:", y.shape)
print("Classes:", iris.target_names)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)

# Train Decision Tree model
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

print("\nDecision Tree model trained successfully")

# Generate predictions
y_pred = clf.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy:", round(accuracy, 2))

# Task 2: Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

# Save confusion matrix as CSV
cm_df = pd.DataFrame(
    cm,
    index=iris.target_names,
    columns=iris.target_names
)

cm_df.to_csv("confusion_matrix.csv")

# Visualize confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=iris.target_names,
    yticklabels=iris.target_names
)

plt.xlabel("Predicted")
plt.ylabel("True")
plt.title("Confusion Matrix for Decision Tree Classifier")
plt.tight_layout()
plt.savefig("confusion_matrix_plot.png")
plt.close()

print("\nConfusion matrix plot saved as confusion_matrix_plot.png")

# Task 3: Classification Report
report = classification_report(
    y_test,
    y_pred,
    target_names=iris.target_names
)

print("\nClassification Report:")
print(report)

with open("classification_report.txt", "w") as file:
    file.write("Lab 11: Model Evaluation Using a Confusion Matrix\n\n")
    file.write(f"Accuracy: {accuracy:.2f}\n\n")
    file.write("Confusion Matrix:\n")
    file.write(str(cm))
    file.write("\n\nClassification Report:\n")
    file.write(report)

# Save interpretation report
with open("confusion_matrix_analysis.txt", "w") as file:
    file.write("Confusion Matrix Interpretation\n\n")
    file.write("Diagonal values show correct predictions.\n")
    file.write("Off-diagonal values show classification errors.\n")
    file.write("Precision shows how many predicted positives were correct.\n")
    file.write("Recall shows how many actual positives were correctly identified.\n")
    file.write("F1-score balances precision and recall.\n\n")
    file.write("For this Iris dataset, the Decision Tree model performed strongly.\n")

print("Reports saved successfully")
print("\nLab completed successfully.")
