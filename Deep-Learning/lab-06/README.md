# Lab 06: Overfitting and Underfitting

## Objective

Understand overfitting and underfitting using training and validation losses, and explore dropout as a regularization technique.

## Tools Used

- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- TensorFlow/Keras

## Dataset

California Housing dataset from scikit-learn.

Note: The Boston Housing dataset was not used because `load_boston` has been removed from newer versions of scikit-learn.

## Tasks Performed

1. Loaded a regression dataset
2. Split data into training and validation sets
3. Trained Linear Regression model
4. Calculated training and validation losses
5. Plotted training vs validation loss
6. Created a neural network with Dropout
7. Plotted neural network training and validation loss
8. Saved final report

## Files

```text
overfitting_underfitting.py
training_validation_loss.png
dropout_loss_plot.png
overfitting_underfitting_report.txt
README.md

Conclusion

This lab explained how to identify overfitting and underfitting by comparing training and validation losses. Dropout was introduced as a technique to reduce overfitting in neural networks.
