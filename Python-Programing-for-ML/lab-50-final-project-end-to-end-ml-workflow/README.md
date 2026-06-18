# Lab 50: Final Project - End-to-End ML Workflow in Python

## Objective

Build a complete Machine Learning workflow using Python, including dataset loading, preprocessing, model training, evaluation, and result visualization.

---

## Prerequisites

- Python 3
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

---

## Task 1: Select Dataset and Define Problem

### Dataset

The Iris dataset is used from Scikit-learn.

### Problem Statement

Classify iris flowers into three species based on:

- Sepal length
- Sepal width
- Petal length
- Petal width

### Load Dataset

```python
from sklearn.datasets import load_iris

data = load_iris()
X, y = data.data, data.target
