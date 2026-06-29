# Lab 23: Experimenting with Different Optimizers

## Objective

Compare how SGD, Adam, and RMSprop optimizers affect model training performance.

## Tools Used

- Python
- TensorFlow/Keras
- Pandas
- Matplotlib

## Dataset

MNIST handwritten digit dataset.

## Tasks Performed

1. Loaded and preprocessed MNIST dataset
2. Built identical neural network models
3. Trained one model with SGD
4. Trained one model with Adam
5. Trained one model with RMSprop
6. Compared loss and accuracy
7. Saved plots, models, CSV results, and report

## Files

```text
optimizer_comparison.py
optimizer_comparison_results.csv
optimizer_accuracy_comparison.png
optimizer_loss_comparison.png
model_sgd.keras
model_adam.keras
model_rmsprop.keras
optimizer_report.txt
README.md

Conclusion

This lab showed that optimizer choice affects convergence speed and accuracy. Adam and RMSprop usually converge faster than SGD, while SGD may need more tuning.
