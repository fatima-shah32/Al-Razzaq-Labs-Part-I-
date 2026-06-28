# Lab 12: Implementing Dropout Regularization

## Objective

Understand and implement dropout regularization in a CNN model and compare performance with and without dropout.

## Tools Used

- Python
- TensorFlow/Keras
- NumPy
- Pandas
- Matplotlib

## Dataset

MNIST handwritten digit dataset.

## Tasks Performed

1. Loaded and preprocessed MNIST dataset
2. Built CNN model without dropout
3. Built CNN model with dropout
4. Trained both models
5. Compared accuracy and loss
6. Saved comparison graphs
7. Saved model files and report

## Files

```text
dropout_regularization.py
dropout_comparison_results.csv
dropout_accuracy_comparison.png
dropout_loss_comparison.png
cnn_without_dropout.keras
cnn_with_dropout.keras
dropout_report.txt
README.md

Conclusion

Dropout regularization helps reduce overfitting by randomly disabling neurons during training. This encourages the model to learn stronger and more generalized features.
