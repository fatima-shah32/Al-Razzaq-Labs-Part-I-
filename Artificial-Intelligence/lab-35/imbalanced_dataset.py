import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE


print("=== Lab 35: Handling Imbalanced Datasets ===")

# Task 1: Create imbalanced dataset
X, y = make_classification(
    n_classes=2,
    class_sep=2,
    weights=[0.99, 0.01],
    n_informative=3,
    n_redundant=1,
    flip_y=0,
    n_features=5,
    n_clusters_per_class=1,
    n_samples=1000,
    random_state=42
)

data = pd.DataFrame(
    X,
    columns=[f"feature_{i}" for i in range(X.shape[1])]
)

data["target"] = y

print("\nOriginal Class Distribution:")
print(data["target"].value_counts())

# Save original dataset
data.to_csv("imbalanced_dataset.csv", index=False)

# Plot original class distribution
data["target"].value_counts().plot(kind="bar")
plt.title("Original Imbalanced Class Distribution")
plt.xlabel("Class")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("original_class_distribution.png")
plt.close()

print("\nOriginal dataset saved as imbalanced_dataset.csv")
print("Original class distribution plot saved")

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

# Task 2: Apply SMOTE
smote = SMOTE(random_state=42)

X_res, y_res = smote.fit_resample(
    X_train,
    y_train
)

print("\nClass Distribution After SMOTE:")
print(np.bincount(y_res))

# Save balanced dataset
balanced_data = pd.DataFrame(
    X_res,
    columns=[f"feature_{i}" for i in range(X_res.shape[1])]
)

balanced_data["target"] = y_res
balanced_data.to_csv("balanced_dataset_smote.csv", index=False)

# Plot balanced class distribution
pd.Series(y_res).value_counts().plot(kind="bar")
plt.title("Balanced Class Distribution After SMOTE")
plt.xlabel("Class")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("balanced_class_distribution.png")
plt.close()

print("Balanced dataset saved as balanced_dataset_smote.csv")
print("Balanced class distribution plot saved")

# Task 3: Model before balancing
model = LogisticRegression(random_state=42, max_iter=1000)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nClassification Report for Imbalanced Data:")
imbalanced_report = classification_report(y_test, y_pred)
print(imbalanced_report)

# Task 4: Model after balancing
model_res = LogisticRegression(random_state=42, max_iter=1000)

model_res.fit(X_res, y_res)

y_pred_res = model_res.predict(X_test)

print("\nClassification Report for Balanced Data:")
balanced_report = classification_report(y_test, y_pred_res)
print(balanced_report)

# Save reports
with open("model_reports.txt", "w") as file:
    file.write("Classification Report for Imbalanced Data:\n")
    file.write(imbalanced_report)
    file.write("\n\nClassification Report for Balanced Data:\n")
    file.write(balanced_report)

print("\nModel reports saved as model_reports.txt")

print("\nLab completed successfully.")
