# Lab 27: Hyperparameter Tuning in Deep Learning

## Objective

Understand and apply hyperparameter tuning by testing different learning rates and batch sizes.

## Tools Used

- Python
- TensorFlow/Keras
- NumPy
- Pandas
- Matplotlib

## Dataset

MNIST handwritten digit dataset subset.

## Hyperparameters Tested

### Learning Rates

```text
0.001, 0.01, 0.1
Batch Sizes
16, 32, 64
Tasks Performed
Defined a hyperparameter grid
Loaded and preprocessed MNIST dataset
Built a training function
Trained models using different hyperparameter combinations
Evaluated each model
Selected best result based on test accuracy
Saved models, results, plots, and report
Files
hyperparameter_tuning.py
hyperparameter_tuning_results.csv
hyperparameter_accuracy_comparison.png
validation_accuracy_curves.png
hyperparameter_tuning_report.txt
model_lr_0.001_bs_16.keras
model_lr_0.001_bs_32.keras
model_lr_0.001_bs_64.keras
model_lr_0.01_bs_16.keras
model_lr_0.01_bs_32.keras
model_lr_0.01_bs_64.keras
model_lr_0.1_bs_16.keras
model_lr_0.1_bs_32.keras
model_lr_0.1_bs_64.keras
README.md
Conclusion

This lab demonstrated how learning rate and batch size affect model performance. Hyperparameter tuning helps identify better training configurations for deep learning models.
