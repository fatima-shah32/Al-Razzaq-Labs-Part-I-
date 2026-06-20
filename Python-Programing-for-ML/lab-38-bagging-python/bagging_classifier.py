import numpy as np
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score

# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

print("Dataset loaded successfully")
print("Features:", iris.feature_names)
print("Target classes:", iris.target_names)

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

# Create base estimator
base_estimator = DecisionTreeClassifier(random_state=42)

# Create Bagging model
bagging_clf = BaggingClassifier(
    estimator=base_estimator,
    n_estimators=10,
    random_state=42
)

# Train Bagging model
bagging_clf.fit(X_train, y_train)

# Make predictions using Bagging model
y_pred = bagging_clf.predict(X_test)

# Calculate Bagging accuracy
bagging_accuracy = accuracy_score(y_test, y_pred)

print("\nBagging Classifier Accuracy:", round(bagging_accuracy, 2))

# Train a single Decision Tree for comparison
single_tree_clf = DecisionTreeClassifier(random_state=42)
single_tree_clf.fit(X_train, y_train)

# Make predictions using single Decision Tree
y_single_pred = single_tree_clf.predict(X_test)

# Calculate single Decision Tree accuracy
single_accuracy = accuracy_score(y_test, y_single_pred)

print("Single Decision Tree Accuracy:", round(single_accuracy, 2))

# Compare results
improvement = bagging_accuracy - single_accuracy
print("Improvement in Accuracy:", round(improvement, 2))
