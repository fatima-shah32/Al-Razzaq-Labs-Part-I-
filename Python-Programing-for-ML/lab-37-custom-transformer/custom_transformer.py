import numpy as np
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline


class MyCustomTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, parameter=5):
        self.parameter = parameter

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        transformed_X = X + self.parameter
        return transformed_X


data = {
    "feature1": [10, 20, 30],
    "feature2": [1, 2, 3]
}

X = pd.DataFrame(data)

print("Original Dataset:")
print(X)

my_pipeline = Pipeline(steps=[
    ("custom_transformer", MyCustomTransformer(parameter=5))
])

transformed_data = my_pipeline.fit_transform(X)

print("\nTransformed Dataset:")
print(transformed_data)
