# Lab 21: Building a Simple Linear Regression Model

## Objective

Build and evaluate a Linear Regression model using Python and scikit-learn.

## Tools Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn

## Dataset

California Housing dataset from scikit-learn.

## Tasks Performed

1. Loaded the dataset
2. Inspected dataset preview and summary
3. Checked missing values
4. Split data into features and target
5. Split dataset into training and testing sets
6. Trained a Linear Regression model
7. Made predictions
8. Evaluated model using MSE and R² score
9. Visualized actual vs predicted values

## Main Code

```python
lin_reg_model = LinearRegression()
lin_reg_model.fit(X_train, y_train)
y_pred = lin_reg_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
Conclusion

In this lab, I learned how to build a Linear Regression model. I loaded a dataset, split it into training and testing sets, trained the model, made predictions, and evaluated performance using Mean Squared Error and R² score.
