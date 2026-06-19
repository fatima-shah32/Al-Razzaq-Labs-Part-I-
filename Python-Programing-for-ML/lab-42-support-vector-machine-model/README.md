# Lab 42: Building and Evaluating a Support Vector Machine Model

## Objective

Understand how to build, train, and evaluate a Support Vector Machine model using scikit-learn.

## Introduction

Support Vector Machines are supervised machine learning algorithms used for classification and regression tasks. SVM tries to find the best hyperplane that separates data points into different classes.

## Task 1: Train an SVM Model Using scikit-learn

### Import Libraries

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
Load Dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

The Iris dataset is used for classification.

Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)
Standardize Features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

Standardization helps the SVM model perform better because SVM is sensitive to feature scale.

Task 2: Train the SVM Model
svm_model = SVC(kernel='rbf', C=1.0, gamma='scale')
svm_model.fit(X_train, y_train)
Task 3: Evaluate Model Performance
y_pred = svm_model.predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
Evaluation Metrics
Confusion Matrix

Shows correct and incorrect predictions for each class.

Precision

Shows how many predicted positive results were actually correct.

Recall

Shows how many actual positive results were correctly identified.

F1-Score

Combines precision and recall into one balanced metric.

Accuracy

Shows the overall percentage of correct predictions.

Task 4: Experiment with Different Kernels
Linear Kernel
svm_linear = SVC(kernel='linear', C=1.0)
svm_linear.fit(X_train, y_train)

Linear kernel works well when data is linearly separable.

Polynomial Kernel
svm_poly = SVC(kernel='poly', degree=3, C=1.0, gamma='scale')
svm_poly.fit(X_train, y_train)

Polynomial kernel can handle more complex relationships.

Sigmoid Kernel
svm_sigmoid = SVC(kernel='sigmoid', C=1.0, gamma='scale')
svm_sigmoid.fit(X_train, y_train)

Sigmoid kernel behaves similarly to neural network activation functions.

RBF Kernel

RBF kernel is useful for non-linear classification problems and is commonly used with SVM models.

Conclusion

In this lab, I learned how to build and evaluate a Support Vector Machine model using scikit-learn. I trained an SVM model on the Iris dataset, evaluated it using confusion matrix and classification report, and tested different kernels including RBF, linear, polynomial, and sigmoid. This helped me understand how kernel selection affects model performance.

