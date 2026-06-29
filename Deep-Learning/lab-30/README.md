# Lab 30: Visualizing Convolutional Filters

## Objective

Extract and visualize convolutional filters from a CNN model to understand how early CNN layers learn visual patterns.

## Tools Used

- Python
- TensorFlow/Keras
- NumPy
- Pandas
- Matplotlib

## Model Used

VGG16 pretrained on ImageNet.

## Selected Layer

```text
block1_conv1
Tasks Performed
Loaded VGG16 pretrained model
Selected first convolutional layer
Extracted convolutional filter weights
Normalized filter values
Visualized grayscale channel filters
Visualized RGB filter patterns
Saved filter statistics and interpretation report
Files
visualize_conv_filters.py
vgg16_block1_conv1_filters.png
vgg16_rgb_filter_patterns.png
filter_layer_info.csv
filter_statistics.csv
filter_visualization_report.txt
README.md
Conclusion

This lab demonstrated how CNN filters can be extracted and visualized. Early convolutional filters often learn simple patterns such as edges, textures, and color gradients.
