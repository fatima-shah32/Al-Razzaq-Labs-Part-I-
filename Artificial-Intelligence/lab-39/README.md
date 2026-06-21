# Lab 39: Introduction to Ensemble Methods

## Objective

Understand ensemble methods, especially Bagging and Boosting, and compare them with a single Decision Tree model.

## Dataset

Iris dataset from scikit-learn.

## Tools Used

- Python
- Pandas
- Scikit-learn

## Tasks Performed

1. Loaded the Iris dataset
2. Split data into training and testing sets
3. Trained a Random Forest model using Bagging
4. Trained a single Decision Tree model
5. Trained a Gradient Boosting model
6. Compared model accuracies
7. Saved comparison results into CSV file

## Models Used

### Decision Tree

A single machine learning model used for comparison.

### Random Forest

Random Forest is a Bagging method. It trains multiple decision trees and combines their predictions to reduce variance.

### Gradient Boosting

Gradient Boosting is a Boosting method. It improves weak models step by step to reduce errors.

## Main Code

```python
rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
Output

The program displays:

Random Forest accuracy
Decision Tree accuracy
Gradient Boosting accuracy
Model comparison table
Files Created
model_comparison.csv
Final Folder Structure
Artificial-Intelligence/
└── lab-39/
    ├── README.md
    ├── ensemble_methods.py
    ├── model_comparison.csv
    └── ai-env/
Conclusion

In this lab, I learned how ensemble methods improve machine learning models. Random Forest uses Bagging to reduce variance, while Gradient Boosting uses Boosting to improve weak learners. I compared both ensemble methods with a single Decision Tree model.
