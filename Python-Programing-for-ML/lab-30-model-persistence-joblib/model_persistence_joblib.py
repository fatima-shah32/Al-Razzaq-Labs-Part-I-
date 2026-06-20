import numpy as np
import joblib

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


print("=== Lab 30: Model Persistence with Joblib ===")

# Load Iris dataset
data = load_iris()
X, y = data.data, data.target

print("\nDataset loaded successfully")
print("Feature shape:", X.shape)
print("Target shape:", y.shape)

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Random Forest model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

print("\nModel trained successfully")

# Check model accuracy before saving
train_predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, train_predictions)

print("Model Accuracy Before Saving:", round(accuracy, 2))

# Save model using Joblib
joblib.dump(model, "random_forest_model.pkl")

print("\nModel saved successfully as random_forest_model.pkl")

# Load saved model
loaded_model = joblib.load("random_forest_model.pkl")

print("Model loaded successfully from random_forest_model.pkl")

# Make predictions using loaded model
predictions = loaded_model.predict(X_test)

print("\nPredicted Labels:")
print(predictions)

print("\nActual Labels:")
print(y_test)

# Check loaded model accuracy
loaded_accuracy = accuracy_score(y_test, predictions)

print("\nLoaded Model Accuracy:", round(loaded_accuracy, 2))
