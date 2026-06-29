# Lab 21: Data Augmentation for Images

## Objective

Understand and apply image data augmentation techniques, then compare CNN performance with and without augmentation.

## Tools Used

- Python
- TensorFlow/Keras
- NumPy
- Pandas
- Matplotlib

## Dataset

CIFAR-10 image dataset subset.

## Augmentation Techniques Used

- Rotation
- Width shift
- Height shift
- Horizontal flip
- Fill mode nearest

## Tasks Performed

1. Loaded CIFAR-10 dataset
2. Normalized image pixel values
3. Applied image augmentation
4. Visualized augmented images
5. Built CNN model
6. Trained CNN without augmentation
7. Trained CNN with augmentation
8. Compared test accuracy and loss
9. Saved plots, models, CSV results, and report

## Files

```text
image_data_augmentation.py
augmented_images.png
augmentation_comparison_results.csv
augmentation_accuracy_comparison.png
augmentation_loss_comparison.png
cnn_without_augmentation.keras
cnn_with_augmentation.keras
augmentation_report.txt
README.md
Conclusion

This lab showed how data augmentation increases dataset diversity using image transformations. It can help reduce overfitting and improve model generalization on unseen images.
