# Lab 20: Data Preprocessing with scikit-learn - Encoding Categorical Variables

## Objective

Learn how to encode categorical variables using LabelEncoder and OneHotEncoder and integrate them into a preprocessing pipeline.

## Tools Used

- Python
- Pandas
- NumPy
- Scikit-learn

## Tasks Performed

1. Created a sample categorical dataset
2. Applied LabelEncoder
3. Applied OneHotEncoder
4. Built a preprocessing pipeline
5. Trained a Logistic Regression model using encoded data

## Main Code

```python
label_encoder = LabelEncoder()

df["Category_encoded"] = label_encoder.fit_transform(
    df["Category"]
)
```

```python
onehot_encoder = OneHotEncoder(
    sparse_output=False
)
```

```python
pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier", LogisticRegression())
    ]
)
```

## Final Structure

```text
lab-20-categorical-encoding/
├── README.md
├── categorical_encoding.py
└── ml-env/
```

## Conclusion

In this lab, I learned how to preprocess categorical variables using LabelEncoder and OneHotEncoder. I also integrated categorical encoding into a scikit-learn pipeline and trained a Logistic Regression model using the transformed data.
