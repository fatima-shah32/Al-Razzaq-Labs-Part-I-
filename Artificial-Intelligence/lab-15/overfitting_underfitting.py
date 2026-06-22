import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

print("=== Lab 15: Overfitting vs. Underfitting ===")

# Task 1: Load Dataset
iris = load_iris()
X = iris.data
y = iris.target

print("\nDataset loaded successfully")
print("Feature shape:", X.shape)
print("Target shape:", y.shape)

# Split data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

print("\nTraining data shape:", X_train.shape)
print("Validation data shape:", X_val.shape)

# Train basic decision tree
basic_model = DecisionTreeClassifier(random_state=42)
basic_model.fit(X_train, y_train)

train_score = basic_model.score(X_train, y_train)
val_score = basic_model.score(X_val, y_val)

print("\nBasic Decision Tree Scores:")
print(f"Training Score: {train_score:.2f}")
print(f"Validation Score: {val_score:.2f}")

# Task 2: Adjust model complexity using max_depth
depth_range = range(1, 10)

train_scores = []
val_scores = []

for depth in depth_range:
    model = DecisionTreeClassifier(
        max_depth=depth,
        random_state=42
    )

    model.fit(X_train, y_train)

    train_scores.append(model.score(X_train, y_train))
    val_scores.append(model.score(X_val, y_val))

# Save score results
results_df = pd.DataFrame({
    "Max_Depth": list(depth_range),
    "Training_Score": train_scores,
    "Validation_Score": val_scores
})

print("\nScores by Max Depth:")
print(results_df)

results_df.to_csv("depth_scores.csv", index=False)

# Plot training vs validation scores
plt.figure(figsize=(8, 5))
plt.plot(depth_range, train_scores, marker="o", label="Training Score")
plt.plot(depth_range, val_scores, marker="o", label="Validation Score")
plt.xlabel("Max Depth")
plt.ylabel("Score")
plt.title("Decision Tree Performance vs Max Depth")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("overfitting_underfitting_plot.png")
plt.close()

print("\nPlot saved as overfitting_underfitting_plot.png")
print("Scores saved as depth_scores.csv")

# Task 3: Analysis Report
with open("analysis_report.txt", "w") as file:
    file.write("Lab 15: Overfitting vs. Underfitting\n\n")
    file.write(f"Basic Training Score: {train_score:.2f}\n")
    file.write(f"Basic Validation Score: {val_score:.2f}\n\n")
    file.write("Scores by Max Depth:\n")
    file.write(results_df.to_string(index=False))
    file.write("\n\nAnalysis:\n")
    file.write("A very shallow tree may underfit because it cannot learn enough patterns.\n")
    file.write("A very deep tree may overfit because it can memorize training data.\n")
    file.write("The best model is usually where training and validation scores are both high.\n")

print("Analysis report saved as analysis_report.txt")

print("\nLab completed successfully.")
