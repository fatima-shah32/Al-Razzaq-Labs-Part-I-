# Lab 33: Hyperparameter Tuning with GridSearchCV

## Objective

Use GridSearchCV to find the best hyperparameters for an SVM classifier.

## Dataset

Iris dataset from scikit-learn.

## Tools Used

- Python
- Pandas
- Scikit-learn

## Tasks Performed

1. Loaded Iris dataset
2. Split data into training and testing sets
3. Defined SVM parameter grid
4. Ran GridSearchCV
5. Found best parameters
6. Evaluated model on test data
7. Saved GridSearch results and evaluation report

## Parameter Grid

```python
param_grid = {
    "C": [0.1, 1, 10, 100],
    "gamma": [1, 0.1, 0.01, 0.001],
    "kernel": ["rbf", "linear"]
}
