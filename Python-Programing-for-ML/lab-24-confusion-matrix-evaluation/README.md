# Lab 24: Model Evaluation using Confusion Matrix

## Objective

Understand how to evaluate a classification model using a confusion matrix and performance metrics.

## Tools Used

- Python
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn

## Dataset

Iris dataset from scikit-learn.

## Tasks Performed

1. Loaded and explored the Iris dataset
2. Split data into training and testing sets
3. Trained a RandomForestClassifier
4. Generated predictions
5. Created a confusion matrix
6. Visualized the confusion matrix using Seaborn
7. Calculated accuracy, precision, recall, and F1 score

## Main Code

```python
cm = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average="weighted")
recall = recall_score(y_test, y_pred, average="weighted")
f1 = f1_score(y_test, y_pred, average="weighted")
Conclusion

In this lab, I learned how to evaluate a classification model using a confusion matrix. I also calculated accuracy, precision, recall, and F1 score to better understand model performance.
