# Lab 22: Batch Normalization in Deep Networks

## Objective

Understand and compare deep learning models with and without Batch Normalization.

## Tools Used

- Python
- TensorFlow/Keras
- Pandas
- Matplotlib

## Dataset

MNIST handwritten digit dataset.

## Tasks Performed

1. Loaded and normalized MNIST dataset
2. Created a model with Batch Normalization
3. Created a model without Batch Normalization
4. Trained both models
5. Compared accuracy, loss, and training time
6. Saved comparison graphs, CSV results, models, and report

## Files

```text
batch_normalization.py
batch_normalization_comparison.csv
batch_norm_accuracy_comparison.png
batch_norm_loss_comparison.png
model_with_batch_normalization.keras
model_without_batch_normalization.keras
batch_normalization_report.txt
README.md
Conclusion

Batch Normalization helps stabilize training by normalizing layer activations. It can improve convergence and model generalization depending on the network and dataset.
