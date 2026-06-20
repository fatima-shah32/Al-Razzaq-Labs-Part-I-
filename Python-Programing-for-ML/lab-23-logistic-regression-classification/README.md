# Lab 23: Introduction to Logistic Regression for Classification

## Objective

Implement Logistic Regression for binary classification using scikit-learn.

## Tools Used

- Python
- Pandas
- Scikit-learn
- Matplotlib

## Dataset

Iris dataset from scikit-learn.

Only two classes were selected for binary classification:

- Class 0
- Class 1

## Tasks Performed

1. Loaded the Iris dataset
2. Converted data into pandas DataFrame and Series
3. Filtered dataset for binary classification
4. Split data into training and testing sets
5. Trained a LogisticRegression model
6. Made predictions
7. Evaluated model accuracy
8. Created actual vs predicted plot

## Main Code

```python
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
Conclusion

In this lab, I learned how to use Logistic Regression for binary classification. I trained the model on two Iris classes and evaluated its accuracy using test data.
