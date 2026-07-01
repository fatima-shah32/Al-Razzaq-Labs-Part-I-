# Lab 33: Transfer Learning for Image Classification

## Objective

Understand and implement transfer learning using a pretrained VGG16 model for image classification.

## Tools Used

- Python
- TensorFlow/Keras
- NumPy
- Pandas
- Matplotlib

## Dataset

CIFAR-10 image dataset subset.

## Base Model

VGG16 pretrained on ImageNet.

## Tasks Performed

1. Loaded CIFAR-10 dataset
2. Resized images to 224x224 for VGG16
3. Loaded pretrained VGG16 without top layers
4. Froze base model layers
5. Added custom classification layers
6. Trained the transfer learning model
7. Evaluated test accuracy
8. Saved model, plots, history, and report

## Files

```text
transfer_learning.py
transfer_learning_vgg16.keras
transfer_learning_history.csv
transfer_learning_accuracy.png
transfer_learning_loss.png
transfer_learning_report.txt
README.md

Conclusion

This lab demonstrated transfer learning by reusing a pretrained VGG16 feature extractor and adding custom layers for CIFAR-10 image classification.
