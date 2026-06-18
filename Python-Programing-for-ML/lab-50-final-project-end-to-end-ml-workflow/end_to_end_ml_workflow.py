import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Task 1: Load Dataset
data = load_iris()
X, y = data.data, data.target

# Convert dataset into DataFrame
df = pd.DataFrame(X, columns=data.feature_names)
df["target"] = y

print("Dataset Preview:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Task 2: Feature Engineering
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Task 3: Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Train Model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Task 4: Evaluation
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print("\nModel Accuracy:")
print(accuracy)

print("\nConfusion Matrix:")
print(cm)

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=data.target_names))

# Plot Confusion Matrix using Matplotlib
fig, ax = plt.subplots()
ax.imshow(cm)

ax.set_title("Confusion Matrix")
ax.set_xlabel("Predicted")
ax.set_ylabel("Actual")

ax.set_xticks(np.arange(len(data.target_names)))
ax.set_yticks(np.arange(len(data.target_names)))
ax.set_xticklabels(data.target_names)
ax.set_yticklabels(data.target_names)

for i in range(len(data.target_names)):
    for j in range(len(data.target_names)):
        ax.text(j, i, cm[i, j], ha="center", va="center")

plt.tight_layout()
plt.savefig("confusion_matrix.png")
print("\nConfusion matrix image saved as confusion_matrix.png")
