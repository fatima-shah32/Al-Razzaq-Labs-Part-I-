# Lab 32: Building a Residual Block ResNet Basic Version

## Objective

Understand residual learning, build a basic residual block, integrate it into a CNN, and compare it with a standard CNN.

## Tools Used

- Python
- TensorFlow/Keras
- Pandas
- Matplotlib

## Dataset

CIFAR-10 image dataset subset.

## Key Concept

A residual block uses a shortcut connection that adds the input back to the output of convolutional layers.

```text
Input -> Conv2D -> BatchNorm -> ReLU -> Conv2D -> BatchNorm -> Add(Input) -> ReLU
Tasks Performed
Built a residual block function
Created a basic ResNet-style CNN
Created a standard CNN for comparison
Loaded and normalized CIFAR-10 dataset
Trained both models
Compared accuracy, loss, and training time
Saved models, plots, CSV results, and report
Files
residual_block_resnet.py
resnet_cnn_comparison.csv
resnet_cnn_accuracy_comparison.png
resnet_cnn_loss_comparison.png
basic_resnet_model.keras
standard_cnn_model.keras
resnet_report.txt
README.md
Conclusion

This lab demonstrated how residual blocks help improve information flow in CNNs. Residual connections are useful for training deeper networks and reducing vanishing gradient issues.
