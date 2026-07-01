import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt

from tensorflow.keras.applications import VGG16
from tensorflow.keras.layers import Flatten, Dense, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical

print("=== Lab 33: Transfer Learning for Image Classification ===")

num_classes = 10

# Load CIFAR-10 dataset
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Use subset for faster training
x_train = x_train[:3000]
y_train = y_train[:3000]
x_test = x_test[:500]
y_test = y_test[:500]

# Resize images from 32x32 to 224x224 for VGG16
x_train = tf.image.resize(x_train, (224, 224)) / 255.0
x_test = tf.image.resize(x_test, (224, 224)) / 255.0

y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)

print("\nDataset loaded and preprocessed")
print("Training shape:", x_train.shape)
print("Testing shape:", x_test.shape)

# Task 1: Load pretrained VGG16
base_model = VGG16(
    weights="imagenet",
    include_top=False,
    input_shape=(224, 224, 3)
)

for layer in base_model.layers:
    layer.trainable = False

print("\nBase VGG16 loaded and frozen")

# Task 2: Add custom classifier
x = Flatten()(base_model.output)
x = Dense(256, activation="relu")(x)
x = Dropout(0.5)(x)
output_layer = Dense(num_classes, activation="softmax")(x)

model = Model(
    inputs=base_model.input,
    outputs=output_layer
)

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

print("\nTransfer Learning Model Summary:")
model.summary()

# Task 3: Train model
history = model.fit(
    x_train,
    y_train,
    epochs=5,
    batch_size=32,
    validation_data=(x_test, y_test),
    verbose=1
)

# Evaluate model
loss, accuracy = model.evaluate(x_test, y_test, verbose=0)

print("\nTest Loss:", round(loss, 4))
print("Test Accuracy:", round(accuracy * 100, 2), "%")

# Save model
model.save("transfer_learning_vgg16.keras")

# Save training history
history_df = pd.DataFrame(history.history)
history_df.to_csv("transfer_learning_history.csv", index=False)

# Plot accuracy
plt.figure(figsize=(8, 5))
plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.title("Transfer Learning Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.tight_layout()
plt.savefig("transfer_learning_accuracy.png")
plt.close()

# Plot loss
plt.figure(figsize=(8, 5))
plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.title("Transfer Learning Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.tight_layout()
plt.savefig("transfer_learning_loss.png")
plt.close()

# Save report
with open("transfer_learning_report.txt", "w") as file:
    file.write("Lab 33: Transfer Learning for Image Classification\n\n")
    file.write("Base Model: VGG16 pretrained on ImageNet\n")
    file.write("Dataset: CIFAR-10 subset\n")
    file.write("Custom Layers: Flatten -> Dense(256) -> Dropout(0.5) -> Dense(10)\n\n")
    file.write(f"Test Loss: {loss:.4f}\n")
    file.write(f"Test Accuracy: {accuracy * 100:.2f}%\n\n")
    file.write("Conclusion:\n")
    file.write("Transfer learning uses features learned from a large dataset and adapts them to a new image classification task.\n")

print("\nFiles saved:")
print("transfer_learning_vgg16.keras")
print("transfer_learning_history.csv")
print("transfer_learning_accuracy.png")
print("transfer_learning_loss.png")
print("transfer_learning_report.txt")

print("\nLab completed successfully.")
