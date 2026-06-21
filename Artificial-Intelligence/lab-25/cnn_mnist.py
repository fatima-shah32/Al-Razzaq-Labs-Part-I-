import numpy as np
import matplotlib.pyplot as plt

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D
from keras.utils import to_categorical


print("=== Lab 25: Intro to Convolutional Neural Networks ===")

# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

print("\nDataset loaded successfully")
print("Training data shape:", x_train.shape)
print("Testing data shape:", x_test.shape)

# Normalize pixel values
x_train = x_train / 255.0
x_test = x_test / 255.0

# Reshape data for CNN
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)

# One-hot encode labels
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

print("\nData preprocessing completed")

# Build CNN model
model = Sequential()

model.add(
    Conv2D(
        32,
        kernel_size=(3, 3),
        activation="relu",
        input_shape=(28, 28, 1)
    )
)

model.add(
    MaxPooling2D(
        pool_size=(2, 2)
    )
)

model.add(Flatten())

model.add(
    Dense(
        10,
        activation="softmax"
    )
)

# Compile model
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

print("\nCNN model created successfully")
model.summary()

# Train model
history = model.fit(
    x_train,
    y_train,
    validation_data=(x_test, y_test),
    epochs=3,
    batch_size=128,
    verbose=1
)

# Evaluate model
loss, accuracy = model.evaluate(
    x_test,
    y_test,
    verbose=0
)

print("\nModel Evaluation:")
print(f"Test Loss: {loss:.3f}")
print(f"Test Accuracy: {accuracy:.3f}")

# Save model
model.save("cnn_mnist_model.h5")

print("\nModel saved as cnn_mnist_model.h5")

# Plot accuracy and loss
plt.figure(figsize=(8, 6))
plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.title("CNN Training Accuracy and Loss")
plt.xlabel("Epoch")
plt.ylabel("Value")
plt.legend()
plt.tight_layout()
plt.savefig("cnn_training_plot.png")
plt.close()

print("Training plot saved as cnn_training_plot.png")

# Save report
with open("cnn_report.txt", "w") as file:
    file.write("Lab 25: Intro to Convolutional Neural Networks\n\n")
    file.write("Dataset: MNIST handwritten digits\n")
    file.write("Model: Simple CNN using Conv2D, MaxPooling2D, Flatten, Dense\n\n")
    file.write(f"Test Loss: {loss:.3f}\n")
    file.write(f"Test Accuracy: {accuracy:.3f}\n")
    file.write("\nConclusion: CNN successfully classified MNIST digit images.")

print("Report saved as cnn_report.txt")

print("\nLab completed successfully.")
