import numpy as np
import matplotlib.pyplot as plt

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense


print("=== Lab 24: Basic Image Classification Concept ===")

# Task 1: CNN Concept
print("\nCNN Concepts:")
print("Convolutional Layer: Extracts image features")
print("Pooling Layer: Reduces image dimensions")
print("Fully Connected Layer: Classifies the image")

# Task 2: Load MNIST dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print("\nDataset Loaded Successfully")
print("Training data shape:", train_images.shape)
print("Test data shape:", test_images.shape)

# Save sample image
plt.figure(figsize=(4, 4))
plt.imshow(train_images[0], cmap="gray")
plt.title(f"Label: {train_labels[0]}")
plt.axis("off")
plt.tight_layout()
plt.savefig("sample_mnist_image.png")
plt.close()

print("\nSample MNIST image saved as sample_mnist_image.png")

# Task 3: Preprocess data
train_images = train_images.astype("float32") / 255
test_images = test_images.astype("float32") / 255

train_images = train_images.reshape(
    train_images.shape[0],
    28,
    28,
    1
)

test_images = test_images.reshape(
    test_images.shape[0],
    28,
    28,
    1
)

print("\nData preprocessing completed")
print("New training shape:", train_images.shape)
print("New test shape:", test_images.shape)

# Build CNN model
model = Sequential([
    Conv2D(
        32,
        (3, 3),
        activation="relu",
        input_shape=(28, 28, 1)
    ),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation="relu"),
    Dense(10, activation="softmax")
])

print("\nCNN model created successfully")

# Compile model
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# Train model
history = model.fit(
    train_images,
    train_labels,
    epochs=3,
    batch_size=64,
    validation_data=(test_images, test_labels),
    verbose=1
)

# Evaluate model
test_loss, test_acc = model.evaluate(
    test_images,
    test_labels,
    verbose=0
)

print("\nModel Evaluation:")
print(f"Test Loss: {test_loss:.3f}")
print(f"Test Accuracy: {test_acc:.3f}")

# Save training plot
plt.figure(figsize=(8, 6))
plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.title("Image Classification Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.tight_layout()
plt.savefig("classification_accuracy.png")
plt.close()

print("\nAccuracy plot saved as classification_accuracy.png")

# Save model
model.save("image_classification_model.h5")

print("Model saved as image_classification_model.h5")

# Save report
with open("image_classification_report.txt", "w") as file:
    file.write("Lab 24: Basic Image Classification Concept\n\n")
    file.write("Dataset: MNIST handwritten digits\n")
    file.write("Model: Simple CNN\n\n")
    file.write("CNN Layers Used:\n")
    file.write("- Conv2D\n")
    file.write("- MaxPooling2D\n")
    file.write("- Flatten\n")
    file.write("- Dense\n\n")
    file.write(f"Test Loss: {test_loss:.3f}\n")
    file.write(f"Test Accuracy: {test_acc:.3f}\n")

print("Report saved as image_classification_report.txt")

print("\nLab completed successfully.")
