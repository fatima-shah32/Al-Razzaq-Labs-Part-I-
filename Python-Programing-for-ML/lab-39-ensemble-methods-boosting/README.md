# Lab 39: Introduction to Ensemble Methods: Boosting with Python

## Objective

The objective of this lab is to understand ensemble methods, especially boosting, using Python and scikit-learn.

In this lab, I used AdaBoostClassifier and compared it with BaggingClassifier and StackingClassifier.

## Tools Used

- Python
- NumPy
- Pandas
- Scikit-learn

## Dataset Used

The Iris dataset was used in this lab.

It contains 150 samples and 4 features:

- Sepal length
- Sepal width
- Petal length
- Petal width

The target classes are:

- Setosa
- Versicolor
- Virginica

## Step 1: Import Libraries

```python
import numpy as np
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier, BaggingClassifier, StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
ep 2: Load Dataset
iris = load_iris()
X = iris.data
y = iris.target

print("Features:", iris.feature_names)
print("Number of classes:", len(np.unique(y)))
Step 3: Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

The dataset was divided into 70% training data and 30% testing data.

Step 4: Train AdaBoost Model
boosting_model = AdaBoostClassifier(
    n_estimators=50,
    random_state=42
)

boosting_model.fit(X_train, y_train)

AdaBoost is a boosting technique that combines multiple weak learners to create a strong model.

Step 5: Evaluate AdaBoost Model
y_pred = boosting_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy of AdaBoost model:", accuracy)

Accuracy score was used to evaluate the AdaBoost model.

Step 6: Train Bagging Model
bagging_model = BaggingClassifier(
    n_estimators=50,
    random_state=42
)

bagging_model.fit(X_train, y_train)

Bagging trains multiple models independently and combines their results.

Step 7: Evaluate Bagging Model
y_pred_bag = bagging_model.predict(X_test)
accuracy_bag = accuracy_score(y_test, y_pred_bag)

print("Accuracy of Bagging model:", accuracy_bag)
Step 8: Train Stacking Model
estimators = [
    ("bagging", BaggingClassifier(n_estimators=10, random_state=42)),
    ("boosting", AdaBoostClassifier(n_estimators=10, random_state=42))
]

stacking_model = StackingClassifier(
    estimators=estimators,
    final_estimator=LogisticRegression(max_iter=1000)
)

stacking_model.fit(X_train, y_train)

Stacking combines different base learners and uses a final estimator to make predictions.

Step 9: Evaluate Stacking Model
y_pred_stack = stacking_model.predict(X_test)
accuracy_stack = accuracy_score(y_test, y_pred_stack)

print("Accuracy of Stacking model:", accuracy_stack)
Step 10: Compare Results
results = pd.DataFrame({
    "Model": ["AdaBoost", "Bagging", "Stacking"],
    "Accuracy": [accuracy, accuracy_bag, accuracy_stack]
})

print(results)
Output

The output shows the accuracy of:

AdaBoost model
Bagging model
Stacking model
Final Folder Structure
lab-39-ensemble-methods-boosting/
├── README.md
├── ensemble_boosting.py
└── ml-env/
Conclusion

In this lab, I learned how ensemble methods improve machine learning model performance.

I implemented AdaBoostClassifier for boosting and compared it with BaggingClassifier and StackingClassifier.

AdaBoost works by training weak learners sequentially and focusing on previous errors. Bagging trains models independently, while stacking combines multiple models using a final estimator.

This lab helped me understand the difference between boosting, bagging, and stacking in machine learning.
