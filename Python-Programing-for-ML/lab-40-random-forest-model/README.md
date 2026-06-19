# Lab 40: Implementing a Simple Random Forest Model

## Objective

The objective of this lab is to train and evaluate a simple Random Forest model using open-source technology. This lab also explores the feature importances provided by the Random Forest model.

## Prerequisites

- Basic understanding of machine learning concepts
- Familiarity with Python programming language
- Python environment with required libraries installed

## Tools Required

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

## Introduction

Random Forest is a supervised machine learning algorithm used for classification and regression problems. It works by creating multiple decision trees and combining their results to make a final prediction.

Random Forest is powerful because it reduces overfitting and usually gives better accuracy than a single decision tree.

In this lab, the Iris dataset is used to train and evaluate a Random Forest classification model.

## Task 1: Train a Random Forest on a Sample Dataset

### Subtask 1.1: Load the Dataset

The famous Iris dataset is used for this lab.

```python
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
y = iris.target

The dataset contains flower measurements and target classes.

The features include:

Sepal length
Sepal width
Petal length
Petal width

The target classes are:

Setosa
Versicolor
Virginica
Subtask 1.2: Split the Dataset

The dataset is divided into training and testing sets.

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

The training set is used to train the model, while the testing set is used to evaluate the model performance.

Subtask 1.3: Train the Random Forest Model

The RandomForestClassifier from scikit-learn is used to train the model.

from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

The parameter n_estimators=100 means the Random Forest model will use 100 decision trees.

Task 2: Evaluate the Model Performance
Subtask 2.1: Make Predictions

After training the model, predictions are made on the test dataset.

y_pred = rf_model.predict(X_test)
Subtask 2.2: Performance Metrics

The model is evaluated using accuracy score, classification report, and confusion matrix.

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

print("Classification Report:")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
Evaluation Metrics
Accuracy

Accuracy shows the overall percentage of correct predictions made by the model.

Classification Report

The classification report shows precision, recall, F1-score, and support for each class.

Precision

Precision tells how many predicted positive results were actually correct.

Recall

Recall tells how many actual positive results were correctly identified.

F1-Score

F1-score combines precision and recall into one balanced metric.

Confusion Matrix

The confusion matrix shows correct and incorrect predictions for each class.

Task 3: Explore Feature Importances
Subtask 3.1: Extract Feature Importances

Feature importance shows how much each feature contributes to the model prediction.

importances = rf_model.feature_importances_
feature_names = iris.feature_names

feature_importance_df = pd.DataFrame({
    "feature": feature_names,
    "importance": importances
})

feature_importance_df = feature_importance_df.sort_values(
    by="importance",
    ascending=False
)

print(feature_importance_df)

This helps identify which features are most useful for classification.

Subtask 3.2: Visualize Feature Importances

The feature importances are visualized using a bar chart.

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))

sns.barplot(
    x="importance",
    y="feature",
    data=feature_importance_df
)

plt.title("Feature Importances in Random Forest Model")
plt.xlabel("Importance Score")
plt.ylabel("Feature")
plt.tight_layout()
plt.savefig("feature_importances.png")
plt.show()

The chart is saved as:

feature_importances.png
Output

The program displays:

Dataset shape
Target classes
Training and testing data shape
Accuracy score
Classification report
Confusion matrix
Feature importance values
Feature importance graph
Final Files Created
lab-40-random-forest-model/
├── README.md
├── random_forest_model.py
├── feature_importances.png
└── ml-env/
