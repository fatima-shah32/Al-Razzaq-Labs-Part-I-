import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

print("=== Lab 10: Simple Logistic Regression Concept ===")

# Task 1: Create binary classification dataset
data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "pass_fail": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

print("\nDataset:")
print(df)

# Save dataset
df.to_csv("student_pass_fail.csv", index=False)

# Visualize data
plt.figure(figsize=(8, 5))
plt.scatter(df["study_hours"], df["pass_fail"], label="Data Points")
plt.xlabel("Study Hours")
plt.ylabel("Pass/Fail")
plt.title("Study Hours vs Pass/Fail")
plt.legend()
plt.tight_layout()
plt.savefig("study_hours_scatter.png")
plt.close()

print("\nScatter plot saved as study_hours_scatter.png")

# Task 2: Train Logistic Regression Model
X = df[["study_hours"]]
y = df["pass_fail"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

print("\nModel trained successfully")

# Task 3: Evaluate Model
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:")
print(f"{accuracy * 100:.2f}%")

# Coefficient and intercept
coefficient = model.coef_[0][0]
intercept = model.intercept_[0]

print("\nModel Coefficient and Intercept:")
print("Coefficient:", coefficient)
print("Intercept:", intercept)

print("\nInterpretation:")
print("A positive coefficient means more study hours increase the chance of passing.")

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

# Predict probabilities for all data points
df["Pass_Probability"] = model.predict_proba(X)[:, 1]
df["Predicted_Result"] = model.predict(X)

print("\nDataset with Predictions:")
print(df)

df.to_csv("logistic_regression_predictions.csv", index=False)

# Decision boundary / probability curve
x_values = np.linspace(
    df["study_hours"].min(),
    df["study_hours"].max(),
    100
).reshape(-1, 1)

probabilities = model.predict_proba(x_values)[:, 1]

plt.figure(figsize=(8, 5))
plt.scatter(df["study_hours"], df["pass_fail"], label="Actual Data")
plt.plot(x_values, probabilities, linewidth=2, label="Passing Probability")
plt.xlabel("Study Hours")
plt.ylabel("Probability of Passing")
plt.title("Logistic Regression Decision Curve")
plt.legend()
plt.tight_layout()
plt.savefig("logistic_regression_curve.png")
plt.close()

print("\nPrediction CSV saved as logistic_regression_predictions.csv")
print("Decision curve saved as logistic_regression_curve.png")

print("\nLab completed successfully.")
