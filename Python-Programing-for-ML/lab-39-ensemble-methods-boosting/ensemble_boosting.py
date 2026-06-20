import numpy as np
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier, BaggingClassifier, StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Step 1: Load Dataset
iris = load_iris()
X = iris.data
y = iris.target

print("Features:", iris.feature_names)
print("Number of classes:", len(np.unique(y)))

# Step 2: Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Step 3: Train AdaBoost Model
boosting_model = AdaBoostClassifier(
    n_estimators=50,
    random_state=42
)

boosting_model.fit(X_train, y_train)

# Step 4: Evaluate AdaBoost
y_pred = boosting_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy of AdaBoost model:", accuracy)

# Step 5: Train Bagging Model
bagging_model = BaggingClassifier(
    n_estimators=50,
    random_state=42
)

bagging_model.fit(X_train, y_train)

y_pred_bag = bagging_model.predict(X_test)
accuracy_bag = accuracy_score(y_test, y_pred_bag)

print("Accuracy of Bagging model:", accuracy_bag)

# Step 6: Train Stacking Model
estimators = [
    ("bagging", BaggingClassifier(n_estimators=10, random_state=42)),
    ("boosting", AdaBoostClassifier(n_estimators=10, random_state=42))
]

stacking_model = StackingClassifier(
    estimators=estimators,
    final_estimator=LogisticRegression(max_iter=1000)
)

stacking_model.fit(X_train, y_train)

y_pred_stack = stacking_model.predict(X_test)
accuracy_stack = accuracy_score(y_test, y_pred_stack)

print("Accuracy of Stacking model:", accuracy_stack)

# Step 7: Compare Results
results = pd.DataFrame({
    "Model": ["AdaBoost", "Bagging", "Stacking"],
    "Accuracy": [accuracy, accuracy_bag, accuracy_stack]
})

print("\nModel Comparison:")
print(results)
