import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt

print("=== Lab 09: CNN for MNIST Digit Recognition ===")

# Task 1: Load and preprocess dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

train_images = train_images.reshape((60000, 28, 28, 1)).astype("float32") / 255
test_images = test_images.reshape((10000, 28, 28, 1)).astype("float32") / 255

train_labels = tf.keras.utils.to_categorical(train_labels, 10)
test_labels = tf.keras.utils.to_categorical(test_labels, 10)

print("\nData loaded and preprocessed successfully")
print("Training images shape:", train_images.shape)
print("Testing images shape:", test_images.shape)

# Task 2: Build CNN model
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),

    layers.Conv2D(64, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),

    layers.Conv2D(64, (3, 3), activation="relu"),

    layers.Flatten(),
    layers.Dense(64, activation="relu"),
    layers.Dense(10, activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

print("\nModel Summary:")
model.summary()

# Task 3: Train model
history = model.fit(
    train_images,
    train_labels,
    epochs=5,
    batch_size=64,
    validation_split=0.1
)

# Task 4: Evaluate model
test_loss, test_acc = model.evaluate(test_images, test_labels)

print("\nTest Loss:", test_loss)
print("Test Accuracy:", test_acc)

# Save model
model.save("cnn_mnist_model.keras")

# Plot accuracy
plt.figure(figsize=(8, 5))
plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.title("CNN Training Accuracy")
plt.legend()
plt.tight_layout()
plt.savefig("cnn_accuracy_plot.png")
plt.close()

# Plot loss
plt.figure(figsize=(8, 5))
plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("CNN Training Loss")
plt.legend()
plt.tight_layout()
plt.savefig("cnn_loss_plot.png")
plt.close()

# Save report
with open("cnn_report.txt", "w") as file:
    file.write("Lab 09: CNN for MNIST Digit Recognition\n\n")
    file.write("Dataset: MNIST handwritten digits\n")
    file.write("Model: Convolutional Neural Network\n\n")
    file.write("Architecture:\n")
    file.write("Conv2D -> MaxPooling2D -> Conv2D -> MaxPooling2D -> Conv2D -> Flatten -> Dense -> Output\n\n")
    file.write(f"Test Loss: {test_loss:.4f}\n")
    file.write(f"Test Accuracy: {test_acc:.4f}\n")

print("\nFiles saved:")
print("cnn_mnist_model.keras")
print("cnn_accuracy_plot.png")
print("cnn_loss_plot.png")
print("cnn_report.txt")

print("\nLab completed successfully.")
