# Lab 25: Implementing k-Nearest Neighbors for Classification

## Objective

Understand and implement the k-Nearest Neighbors classification algorithm using scikit-learn.

## Tools Used

- Python
- Pandas
- Scikit-learn
- Matplotlib

## Dataset

Iris dataset from scikit-learn.

## Tasks Performed

1. Loaded the Iris dataset
2. Converted it into a pandas DataFrame
3. Split data into training and testing sets
4. Trained a k-NN classifier with k=3
5. Evaluated model accuracy
6. Tested k values from 1 to 10
7. Plotted accuracy results

## Main Code

```python
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
Conclusion

In this lab, I learned how to implement k-Nearest Neighbors classification using the Iris dataset. I trained the model with k=3 and tested different k values from 1 to 10. This helped me understand how the value of k affects model performance.
