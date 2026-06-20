import numpy as np
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score

# Load Iris dataset
data = load_iris()
X = data.data
y = data.target

print("Dataset loaded successfully")
print("Feature shape:", X.shape)
print("Target shape:", y.shape)

# Define preprocessing pipeline
preprocessing_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler())
])

# Combine preprocessing and model training
model_pipeline = Pipeline([
    ("preprocessing", preprocessing_pipeline),
    ("classifier", LogisticRegression(max_iter=1000))
])

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Cross-validation
scores = cross_val_score(model_pipeline, X_train, y_train, cv=5)

print("\nCross-validation scores:", scores)
print("Mean cross-validation score: {:.2f}".format(scores.mean()))

# Train and test pipeline
model_pipeline.fit(X_train, y_train)
test_score = model_pipeline.score(X_test, y_test)

print("Test set score: {:.2f}".format(test_score))
