# Lab 23: Early Stopping and Model Regularization

## Objective

Learn how to prevent overfitting in neural networks using EarlyStopping and L2 regularization.

## Tools Used

- Python
- NumPy
- Matplotlib
- TensorFlow
- Keras

## Dataset

MNIST handwritten digits dataset.

## Tasks Performed

1. Loaded MNIST dataset
2. Preprocessed image data
3. Built a neural network without L2
4. Applied EarlyStopping callback
5. Built another model with L2 regularization
6. Compared validation loss and accuracy
7. Saved plots and report

## Files Created

```text
early_stopping_regularization.py
validation_loss_comparison.png
validation_accuracy_comparison.png
regularization_report.txt
README.md
Conclusion

In this lab, I learned how EarlyStopping and L2 regularization help reduce overfitting. EarlyStopping stops training when validation loss stops improving, while L2 regularization penalizes large weights to improve generalization.
