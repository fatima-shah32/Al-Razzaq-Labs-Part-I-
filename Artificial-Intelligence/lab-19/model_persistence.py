import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

print("=== Lab 19: Simple Model Persistence Save & Load ===")

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

# Train Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("\nModel trained successfully")

# Evaluate model before saving
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", round(accuracy, 2))

# Task 2: Save model using joblib
joblib.dump(model, "random_forest_model.joblib")

print("\nModel saved as random_forest_model.joblib")

# Task 3: Load saved model
loaded_model = joblib.load("random_forest_model.joblib")

print("Model loaded successfully")

# Make prediction using loaded model
sample_data = [X_test[0]]
predicted_class = loaded_model.predict(sample_data)

print("\nSample Data:")
print(sample_data)

print("\nPredicted class number:")
print(predicted_class[0])

print("\nPredicted class name:")
print(iris.target_names[predicted_class[0]])

# Save report
with open("model_persistence_report.txt", "w") as file:
    file.write("Lab 19: Simple Model Persistence Save & Load\n\n")
    file.write("Model Used: RandomForestClassifier\n")
    file.write("Dataset: Iris\n")
    file.write(f"Model Accuracy: {round(accuracy, 2)}\n")
    file.write("Saved Model File: random_forest_model.joblib\n")
    file.write(f"Predicted Class Number: {predicted_class[0]}\n")
    file.write(f"Predicted Class Name: {iris.target_names[predicted_class[0]]}\n")

print("\nReport saved as model_persistence_report.txt")
print("\nLab completed successfully.")
