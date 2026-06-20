# Lab 22: Evaluating Regression Models

## Objective

Learn how to evaluate a regression model using Mean Squared Error (MSE) and R² Score.

## Tools Used

- Python
- NumPy
- Pandas
- Scikit-learn
- Matplotlib

## Dataset

California Housing dataset from scikit-learn.

## Tasks Performed

1. Loaded the California Housing dataset
2. Split data into training and testing sets
3. Trained a Linear Regression model
4. Generated predictions on test data
5. Calculated Mean Squared Error (MSE)
6. Calculated R² Score
7. Visualized actual vs predicted values

## Main Code

```python
model = LinearRegression()
model.fit(X_train, y_train)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
Conclusion

In this lab, I learned how to evaluate regression models using MSE and R² Score. I also visualized actual and predicted values to better understand model performance.
