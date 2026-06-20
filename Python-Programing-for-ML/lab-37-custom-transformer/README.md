# Lab 37: Building a Custom Transformer in scikit-learn

## Objective

The objective of this lab is to understand how to create a custom transformer in scikit-learn and use it inside a machine learning pipeline.

## Introduction

Custom transformers are used when we need our own preprocessing logic that is not already available in scikit-learn.

They are useful for:

- Custom feature engineering
- Encoding
- Scaling
- Adding or modifying feature values
- Preparing data before model training

In this lab, I created a simple custom transformer that adds a constant value to each feature.

## Tools Used

- Python
- NumPy
- Pandas
- Scikit-learn

## Task 1: Import Required Libraries

```python
import numpy as np
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import PipelineTask 2: Create Custom Transformer Class
class MyCustomTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, parameter=5):
        self.parameter = parameter

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        transformed_X = X + self.parameter
        return transformed_X

The custom transformer inherits from:

BaseEstimator
TransformerMixin

This makes it compatible with scikit-learn pipelines.

Task 3: Understand fit Method
def fit(self, X, y=None):
    return self

The fit() method prepares the transformer.

In this lab, no training or calculation is required, so it simply returns self.

Task 4: Understand transform Method
def transform(self, X):
    transformed_X = X + self.parameter
    return transformed_X

The transform() method applies the actual transformation.

Here, it adds the value of parameter to every feature in the dataset.

Task 5: Create Sample Dataset
data = {
    "feature1": [10, 20, 30],
    "feature2": [1, 2, 3]
}

X = pd.DataFrame(data)

A small pandas DataFrame was created to test the custom transformer.

Task 6: Build scikit-learn Pipeline
my_pipeline = Pipeline(steps=[
    ("custom_transformer", MyCustomTransformer(parameter=5))
])

The custom transformer was added inside a scikit-learn pipeline.

This makes the preprocessing step reusable and organized.

Task 7: Apply Pipeline
transformed_data = my_pipeline.fit_transform(X)

The pipeline first calls fit() and then applies transform() to the dataset.

Output
Original Dataset:
   feature1  feature2
0        10         1
1        20         2
2        30         3

Transformed Dataset:
   feature1  feature2
0        15         6
1        25         7
2        35         8
Final Folder Structure
lab-37-custom-transformer/
├── README.md
├── custom_transformer.py
└── ml-env/
Conclusion

In this lab, I learned how to create a custom transformer in scikit-learn using BaseEstimator and TransformerMixin.

I implemented the fit() and transform() methods and tested the transformer inside a scikit-learn pipeline.

This lab helped me understand how custom preprocessing steps can be added to machine learning workflows when built-in transformers are not enough.
