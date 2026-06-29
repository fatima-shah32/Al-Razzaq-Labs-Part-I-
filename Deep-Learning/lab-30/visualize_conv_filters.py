import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

from tensorflow.keras.applications import VGG16

print("=== Lab 30: Visualizing Convolutional Filters ===")

# Task 1: Load pre-trained VGG16 model
model = VGG16(
    weights="imagenet",
    include_top=False
)

print("\nVGG16 model loaded successfully")

# Select convolutional layer
layer_name = "block1_conv1"
layer = model.get_layer(name=layer_name)

# Extract weights
weights = layer.get_weights()
filters, biases = weights[0], weights[1]

print("\nSelected Layer:", layer_name)
print("Filters shape:", filters.shape)
print("Biases shape:", biases.shape)

# Save layer information
layer_info = pd.DataFrame({
    "Layer_Name": [layer_name],
    "Filter_Shape": [str(filters.shape)],
    "Bias_Shape": [str(biases.shape)],
    "Number_of_Filters": [filters.shape[-1]]
})

layer_info.to_csv("filter_layer_info.csv", index=False)

# Task 2: Normalize filter values for visualization
f_min = filters.min()
f_max = filters.max()

normalized_filters = (filters - f_min) / (f_max - f_min)

# Visualize first 6 filters, RGB channels separately
n_filters = 6
index = 1

plt.figure(figsize=(8, 10))

for i in range(n_filters):
    filter_image = normalized_filters[:, :, :, i]

    for channel in range(3):
        plt.subplot(n_filters, 3, index)
        plt.imshow(filter_image[:, :, channel], cmap="gray")
        plt.axis("off")

        if channel == 0:
            plt.title(f"Filter {i + 1}")

        index += 1

plt.tight_layout()
plt.savefig("vgg16_block1_conv1_filters.png")
plt.close()

print("\nFilter visualization saved as vgg16_block1_conv1_filters.png")

# Visualize filters as RGB combined images
plt.figure(figsize=(12, 6))

for i in range(12):
    filter_image = normalized_filters[:, :, :, i]

    plt.subplot(3, 4, i + 1)
    plt.imshow(filter_image)
    plt.title(f"Filter {i + 1}")
    plt.axis("off")

plt.tight_layout()
plt.savefig("vgg16_rgb_filter_patterns.png")
plt.close()

print("RGB filter visualization saved as vgg16_rgb_filter_patterns.png")

# Save summary of first few filters
filter_stats = []

for i in range(12):
    current_filter = filters[:, :, :, i]

    filter_stats.append({
        "Filter_Number": i + 1,
        "Min_Value": current_filter.min(),
        "Max_Value": current_filter.max(),
        "Mean_Value": current_filter.mean(),
        "Std_Value": current_filter.std()
    })

filter_stats_df = pd.DataFrame(filter_stats)
filter_stats_df.to_csv("filter_statistics.csv", index=False)

# Task 3: Save interpretation report
with open("filter_visualization_report.txt", "w") as file:
    file.write("Lab 30: Visualizing Convolutional Filters\n\n")
    file.write("Model Used: VGG16 pretrained on ImageNet\n")
    file.write(f"Selected Layer: {layer_name}\n")
    file.write(f"Filter Shape: {filters.shape}\n")
    file.write(f"Number of Filters: {filters.shape[-1]}\n\n")

    file.write("Interpretation:\n")
    file.write("The first convolutional layer usually learns simple visual patterns.\n")
    file.write("These patterns may include edges, lines, color gradients, and texture detectors.\n")
    file.write("Early CNN filters detect low-level features, while deeper layers detect complex shapes.\n\n")

    file.write("Generated Files:\n")
    file.write("- vgg16_block1_conv1_filters.png\n")
    file.write("- vgg16_rgb_filter_patterns.png\n")
    file.write("- filter_layer_info.csv\n")
    file.write("- filter_statistics.csv\n")

print("\nFiles saved:")
print("vgg16_block1_conv1_filters.png")
print("vgg16_rgb_filter_patterns.png")
print("filter_layer_info.csv")
print("filter_statistics.csv")
print("filter_visualization_report.txt")

print("\nLab completed successfully.")
