import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import classification_report, accuracy_score

print("=== Lab 13: Evaluating Classification Models ===")

# Task 1: Load Iris dataset
data = load_iris()
X = data.data
y = data.target

print("\nDataset loaded successfully")
print("Feature shape:", X.shape)
print("Target shape:", y.shape)
print("Target classes:", data.target_names)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

print("\nTraining data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)

# Train Random Forest Classifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

print("\nRandom Forest model trained successfully")

# Predictions
y_pred = clf.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy:", round(accuracy, 2))

# Task 1: Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=data.target_names
)

disp.plot(cmap="viridis")
plt.title("Confusion Matrix - Random Forest Classifier")
plt.tight_layout()
plt.savefig("confusion_matrix.png")
plt.close()

print("\nConfusion matrix plot saved as confusion_matrix.png")

# Task 2: Classification Report
report = classification_report(
    y_test,
    y_pred,
    target_names=data.target_names
)

print("\nClassification Report:")
print(report)

# Save classification report
with open("classification_report.txt", "w") as file:
    file.write("Lab 13: Evaluating Classification Models\n\n")
    file.write(f"Accuracy: {round(accuracy, 2)}\n\n")
    file.write("Confusion Matrix:\n")
    file.write(str(cm))
    file.write("\n\nClassification Report:\n")
    file.write(report)

print("Classification report saved as classification_report.txt")

# Save metrics summary as CSV
report_dict = classification_report(
    y_test,
    y_pred,
    target_names=data.target_names,
    output_dict=True
)

report_df = pd.DataFrame(report_dict).transpose()
report_df.to_csv("classification_metrics.csv")

print("Classification metrics saved as classification_metrics.csv")

# Task 3: Brief Interpretation
with open("evaluation_summary.txt", "w") as file:
    file.write("Brief Evaluation Summary\n\n")
    file.write("The Random Forest Classifier performed strongly on the Iris dataset.\n")
    file.write("The diagonal values in the confusion matrix show correct predictions.\n")
    file.write("Precision, recall, and F1-score help evaluate classification quality.\n")
    file.write("High values indicate that the model correctly classified most samples.\n")

print("Evaluation summary saved as evaluation_summary.txt")

print("\nLab completed successfully.")
