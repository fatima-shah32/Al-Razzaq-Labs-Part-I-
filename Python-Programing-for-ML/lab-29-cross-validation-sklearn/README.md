# Lab 29: Implementing Cross-Validation in scikit-learn

## Objective

Understand and implement k-fold cross-validation using scikit-learn.

## Tools Used

- Python
- NumPy
- Scikit-learn

## Dataset

Iris dataset from scikit-learn.

## Steps Performed

1. Loaded the Iris dataset
2. Created a Logistic Regression model
3. Used KFold with 5 splits
4. Trained and tested the model on each fold
5. Calculated accuracy for every fold
6. Calculated average accuracy and standard deviation

## Main Code

```python
kf = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)
average_accuracy = np.mean(accuracies)
Output

The program prints:

Accuracy of each fold
List of fold accuracies
Average accuracy
Standard deviation
Final Structure
lab-29-cross-validation-sklearn/
├── README.md
├── cross_validation.py
└── ml-env/
Conclusion

In this lab, I learned how to use k-fold cross-validation to evaluate a machine learning model. Cross-validation gives a more reliable estimate of model performance because it tests the model on different parts of the dataset.
