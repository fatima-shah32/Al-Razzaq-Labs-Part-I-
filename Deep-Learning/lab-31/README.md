# Lab 31: Visualizing Intermediate Activations

## Objective

Extract and visualize intermediate activations from convolutional layers of a neural network.

## Tools Used

- Python
- TensorFlow/Keras
- NumPy
- Pandas
- Matplotlib
- Pillow

## Model Used

VGG16 pretrained on ImageNet.

## Selected Layers

```text
block1_conv1
block1_conv2
block2_conv1
block2_conv2
Tasks Performed
Loaded pretrained VGG16 model
Created and preprocessed a sample input image
Passed image through the network
Extracted intermediate layer activations
Visualized selected feature maps
Saved activation information and interpretation report
Files
intermediate_activations.py
sample_input_image.png
activation_layer_info.csv
selected_layer_activations.png
block1_conv1_feature_maps.png
intermediate_activations_report.txt
README.md
Conclusion

This lab demonstrated how intermediate CNN activations can be visualized. These feature maps show how the network transforms raw input images into learned visual representations.
