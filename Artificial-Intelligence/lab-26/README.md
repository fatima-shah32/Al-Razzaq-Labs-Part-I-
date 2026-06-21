# Lab 26: Basic Transfer Learning Concept

## Objective

Understand transfer learning and use a pre-trained Keras model for a small custom image classification task.

## Tools Used

- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib
- Pillow

## Tasks Performed

1. Created a small custom image dataset
2. Loaded MobileNetV2 pre-trained model
3. Removed top layers using include_top=False
4. Froze pre-trained model layers
5. Added custom classification layers
6. Trained model on circle and square images
7. Saved training plot and report

## Files Created

```text
transfer_learning.py
transfer_learning_model.h5
training_accuracy_loss.png
transfer_learning_report.txt
custom_dataset/
