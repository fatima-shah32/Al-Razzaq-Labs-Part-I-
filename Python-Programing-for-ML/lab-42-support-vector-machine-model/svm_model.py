import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Load Iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

print("Dataset loaded successfully")
print("Feature shape:", X.shape)
print("Target shape:", y.shape)
print("Target classes:", iris.target_names)

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

# Standardize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train SVM model using RBF kernel
svm_model = SVC(kernel='rbf', C=1.0, gamma='scale')
svm_model.fit(X_train, y_train)

# Make predictions
y_pred = svm_model.predict(X_test)

# Evaluate RBF model
print("\nRBF Kernel Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nRBF Kernel Classification Report:")
print(classification_report(y_test, y_pred))

print("RBF Kernel Accuracy:", accuracy_score(y_test, y_pred))

# Experiment with Linear Kernel
svm_linear = SVC(kernel='linear', C=1.0)
svm_linear.fit(X_train, y_train)

linear_pred = svm_linear.predict(X_test)

print("\nLinear Kernel Performance:")
print(classification_report(y_test, linear_pred))
print("Linear Kernel Accuracy:", accuracy_score(y_test, linear_pred))

# Experiment with Polynomial Kernel
svm_poly = SVC(kernel='poly', degree=3, C=1.0, gamma='scale')
svm_poly.fit(X_train, y_train)

poly_pred = svm_poly.predict(X_test)

print("\nPolynomial Kernel Performance:")
print(classification_report(y_test, poly_pred))
print("Polynomial Kernel Accuracy:", accuracy_score(y_test, poly_pred))

# Experiment with Sigmoid Kernel
svm_sigmoid = SVC(kernel='sigmoid', C=1.0, gamma='scale')
svm_sigmoid.fit(X_train, y_train)

sigmoid_pred = svm_sigmoid.predict(X_test)

print("\nSigmoid Kernel Performance:")
print(classification_report(y_test, sigmoid_pred))
print("Sigmoid Kernel Accuracy:", accuracy_score(y_test, sigmoid_pred))
