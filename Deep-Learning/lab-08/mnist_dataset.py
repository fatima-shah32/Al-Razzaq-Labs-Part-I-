from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

print("=" * 60)
print("Lab 08: Working with the MNIST Dataset")
print("=" * 60)

# -----------------------------
# Task 1: Load MNIST Dataset
# -----------------------------
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print("\nDataset Loaded Successfully!")

print("\nTraining Images Shape :", train_images.shape)
print("Training Labels Shape :", train_labels.shape)
print("Testing Images Shape  :", test_images.shape)
print("Testing Labels Shape  :", test_labels.shape)

# -----------------------------
# Task 2: Normalize Images
# -----------------------------
train_images = train_images.astype("float32") / 255.0
test_images = test_images.astype("float32") / 255.0

print("\nNormalization Completed")
print("Maximum Pixel Value :", train_images.max())
print("Minimum Pixel Value :", train_images.min())

# -----------------------------
# Save Dataset Information
# -----------------------------
info = pd.DataFrame({
    "Dataset": [
        "Training Images",
        "Training Labels",
        "Testing Images",
        "Testing Labels"
    ],
    "Shape": [
        str(train_images.shape),
        str(train_labels.shape),
        str(test_images.shape),
        str(test_labels.shape)
    ]
})

info.to_csv("dataset_information.csv", index=False)

# -----------------------------
# Task 3: Visualize Sample Digits
# -----------------------------
plt.figure(figsize=(10,5))

for i in range(10):
    plt.subplot(2,5,i+1)
    plt.imshow(train_images[i], cmap="gray")
    plt.title(f"Label: {train_labels[i]}")
    plt.axis("off")

plt.tight_layout()

plt.savefig("mnist_samples.png")

plt.show()

# -----------------------------
# Documentation Report
# -----------------------------
with open("lab_report.txt","w") as file:

    file.write("Lab 08: Working with the MNIST Dataset\n\n")

    file.write("Task 1:\n")
    file.write("Loaded the MNIST handwritten digit dataset using TensorFlow Keras.\n\n")

    file.write("Task 2:\n")
    file.write("Normalized image pixel values from 0-255 to 0-1.\n\n")

    file.write("Task 3:\n")
    file.write("Displayed and saved the first 10 handwritten digit images.\n\n")

    file.write("Dataset Shapes:\n")
    file.write(f"Training Images : {train_images.shape}\n")
    file.write(f"Training Labels : {train_labels.shape}\n")
    file.write(f"Testing Images  : {test_images.shape}\n")
    file.write(f"Testing Labels  : {test_labels.shape}\n\n")

    file.write("Conclusion:\n")
    file.write("MNIST dataset was successfully imported, normalized, and visualized.")

print("\nGenerated Files:")
print("- dataset_information.csv")
print("- mnist_samples.png")
print("- lab_report.txt")

print("\nLab Completed Successfully.")
