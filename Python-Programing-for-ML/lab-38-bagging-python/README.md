# Lab 38: Introduction to Ensemble Methods - Bagging with Python

## Objective

The objective of this lab is to understand ensemble methods in machine learning and implement the Bagging technique using Python and scikit-learn.

## Introduction

Ensemble methods combine multiple machine learning models to make better predictions. Bagging, also called Bootstrap Aggregating, is an ensemble method that trains multiple models on different subsets of data and combines their results.

Bagging helps reduce variance and makes the model more stable and reliable.

## Tools Used

- Python
- NumPy
- Pandas
- Scikit-learn

## Dataset Used

The Iris dataset was used in this lab.

The dataset contains flower measurements and three target classes:

- Setosa
- Versicolor
- Virginica

## Task 1: Import Required Libraries

```python
import numpy as np
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score
Task 2: Load Dataset
iris = load_iris()
X = iris.data
y = iris.target

The Iris dataset contains input features in X and target labels in y.

Task 3: Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

The dataset was divided into training and testing data.
70% data was used for training and 30% data was used for testing.

Task 4: Train Bagging Classifier
base_estimator = DecisionTreeClassifier(random_state=42)

bagging_clf = BaggingClassifier(
    estimator=base_estimator,
    n_estimators=10,
    random_state=42
)

bagging_clf.fit(X_train, y_train)

A Decision Tree was used as the base estimator.
The BaggingClassifier trained 10 Decision Tree models and combined their predictions.

Task 5: Evaluate Bagging Model
y_pred = bagging_clf.predict(X_test)
bagging_accuracy = accuracy_score(y_test, y_pred)

print("Bagging Classifier Accuracy:", round(bagging_accuracy, 2))

The Bagging model was evaluated using accuracy score.

Task 6: Train Single Decision Tree
single_tree_clf = DecisionTreeClassifier(random_state=42)
single_tree_clf.fit(X_train, y_train)

A single Decision Tree model was trained on the same dataset for comparison.

Task 7: Compare Results
y_single_pred = single_tree_clf.predict(X_test)
single_accuracy = accuracy_score(y_test, y_single_pred)

print("Single Decision Tree Accuracy:", round(single_accuracy, 2))

improvement = bagging_accuracy - single_accuracy
print("Improvement in Accuracy:", round(improvement, 2))

The accuracy of BaggingClassifier was compared with the accuracy of a single Decision Tree.

Output
Bagging Classifier Accuracy: 1.0
Single Decision Tree Accuracy: 1.0
Improvement in Accuracy: 0.0
Final Folder Structure
lab-38-bagging-python/
├── README.md
├── bagging_classifier.py
└── ml-env/
Conclusion

In this lab, I learned how Bagging works as an ensemble learning method. I implemented BaggingClassifier using a DecisionTreeClassifier as the base estimator.

I also compared the Bagging model with a single Decision Tree model. Both models achieved good accuracy on the Iris dataset. This helped me understand that Bagging can improve model stability and reduce variance, especially on larger and more complex datasets.
