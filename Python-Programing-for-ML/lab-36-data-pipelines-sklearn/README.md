# Lab 36: Introduction to Data Pipelines using scikit-learn

## Objective

Create a scikit-learn pipeline that combines preprocessing and model training.

## Tools Used

- Python
- NumPy
- Pandas
- Scikit-learn

## Dataset

Iris dataset from scikit-learn.

## Steps Performed

1. Loaded the Iris dataset
2. Created preprocessing steps using:
   - SimpleImputer
   - StandardScaler
3. Built a preprocessing pipeline
4. Added Logistic Regression model
5. Split data into training and testing sets
6. Evaluated the pipeline using cross-validation
7. Tested the final pipeline on test data

## Main Code

```python
preprocessing_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler())
])

model_pipeline = Pipeline([
    ("preprocessing", preprocessing_pipeline),
    ("classifier", LogisticRegression(max_iter=1000))
])
Output

The program prints:

Cross-validation scores
Mean cross-validation score
Test set score
Final Structure
lab-36-data-pipelines-sklearn/
├── README.md
├── data_pipeline.py
└── ml-env/
Conclusion

In this lab, I learned how to build a machine learning pipeline using scikit-learn. The pipeline combined preprocessing and model training into one workflow, making the process cleaner, reusable, and easier to evaluate.
