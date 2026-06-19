# Lab 41: Hyperparameter Tuning using GridSearchCV

## Objective

Understand the concept of hyperparameter tuning and learn how to optimize machine learning models using GridSearchCV in scikit-learn.

## Introduction

Machine learning models contain parameters that are learned during training and hyperparameters that are set before training begins. Choosing the right hyperparameters can significantly improve model performance.

GridSearchCV is a powerful tool in scikit-learn that automates the process of testing multiple combinations of hyperparameters using cross-validation and selects the best-performing model.

In this lab, we use a Support Vector Classifier (SVC) and the Iris dataset to perform hyperparameter tuning using GridSearchCV.

---

## Task 1: Load Dataset

### Import Required Libraries

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd
```

### Load the Iris Dataset

```python
iris = load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

The Iris dataset contains measurements of flower species and is commonly used for classification tasks.

---

## Task 2: Create the Support Vector Classifier Model

### Import SVC

```python
from sklearn.svm import SVC
```

### Instantiate the Model

```python
model = SVC()
```

Support Vector Machines (SVM) are supervised machine learning algorithms commonly used for classification problems.

---

## Task 3: Define Hyperparameter Grid

Hyperparameters are configuration settings used to control the learning process.

### Create Parameter Grid

```python
param_grid = {
    'C': [0.1, 1, 10, 100],
    'gamma': [1, 0.1, 0.01, 0.001],
    'kernel': ['linear', 'rbf']
}
```

### Hyperparameter Explanation

#### C

Controls the trade-off between maximizing the margin and minimizing classification errors.

```python
'C': [0.1, 1, 10, 100]
```

Smaller values create a wider margin.

Larger values focus on correctly classifying training examples.

#### Gamma

Controls how far the influence of a training example reaches.

```python
'gamma': [1, 0.1, 0.01, 0.001]
```

Higher gamma values can lead to overfitting.

Lower gamma values create smoother decision boundaries.

#### Kernel

Determines how data is transformed.

```python
'kernel': ['linear', 'rbf']
```

Linear Kernel:

Used when data is linearly separable.

RBF Kernel:

Used for non-linear classification problems.

---

## Task 4: Configure GridSearchCV

### Import GridSearchCV

```python
from sklearn.model_selection import GridSearchCV
```

### Create Grid Search Object

```python
grid_search = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=5,
    scoring='accuracy',
    verbose=2,
    n_jobs=-1
)
```

### Parameter Explanation

#### estimator

The machine learning model to tune.

#### param_grid

Dictionary containing hyperparameter combinations to test.

#### cv=5

Uses 5-fold cross-validation.

#### scoring='accuracy'

Evaluates models using classification accuracy.

#### verbose=2

Displays progress during training.

#### n_jobs=-1

Uses all available CPU cores for faster computation.

---

## Task 5: Perform Hyperparameter Tuning

### Train Grid Search

```python
grid_search.fit(X_train, y_train)
```

GridSearchCV trains multiple models using all possible parameter combinations and evaluates them using cross-validation.

---

## Task 6: View Best Parameters

### Display Best Results

```python
print(f"Best Parameters: {grid_search.best_params_}")
print(f"Best Cross-Validation Accuracy: {grid_search.best_score_:.2f}")
```

Example Output:

```text
Best Parameters:
{'C': 1, 'gamma': 0.1, 'kernel': 'linear'}

Best Cross-Validation Accuracy:
0.98
```

The exact values may vary depending on the dataset split.

---

## Task 7: Evaluate the Best Model

### Retrieve Best Model

```python
best_model = grid_search.best_estimator_
```

### Test Model Performance

```python
test_accuracy = best_model.score(X_test, y_test)

print(f"Test Set Accuracy: {test_accuracy:.2f}")
```

Example Output:

```text
Test Set Accuracy: 1.00
```

This shows how well the optimized model performs on unseen data.

---

## Understanding Cross-Validation

Cross-validation divides training data into multiple folds.

For 5-fold cross-validation:

1. Data is divided into 5 parts.
2. Four parts are used for training.
3. One part is used for validation.
4. The process repeats five times.
5. Average performance is calculated.

Benefits:

* Better model evaluation
* Reduced overfitting
* More reliable performance estimates

---

## Why Hyperparameter Tuning is Important

Without tuning:

* Model may underfit
* Model may overfit
* Lower predictive performance

With tuning:

* Better accuracy
* Improved generalization
* More reliable predictions

GridSearchCV automates this process and identifies the best hyperparameter combination.

---

## Conclusion

In this lab, I learned how to perform hyperparameter tuning using GridSearchCV in scikit-learn. I created a parameter grid for an SVC model, configured GridSearchCV with cross-validation, trained multiple model combinations, and selected the best-performing hyperparameters. Finally, I evaluated the optimized model on test data and observed improved classification performance. Hyperparameter tuning is an essential step in building high-quality machine learning models.

