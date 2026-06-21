import tensorflow as tf
import matplotlib.pyplot as plt

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten


print("=== Lab 21: Basic MLP with Keras/TensorFlow ===")

# Load MNIST dataset
mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

print("\nDataset loaded successfully")
print("Training data shape:", x_train.shape)
print("Testing data shape:", x_test.shape)

# Normalize pixel values
x_train = x_train / 255.0
x_test = x_test / 255.0

print("\nData normalized successfully")

# Build Sequential MLP model
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation="relu"),
    Dense(10, activation="softmax")
])

print("\nMLP model created successfully")
model.summary()

# Compile model
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

print("\nModel compiled successfully")

# Train model
history = model.fit(
    x_train,
    y_train,
    epochs=5,
    validation_data=(x_test, y_test),
    verbose=1
)

# Evaluate model
test_loss, test_acc = model.evaluate(
    x_test,
    y_test,
    verbose=2
)

print("\nModel Evaluation:")
print(f"Test Loss: {test_loss:.4f}")
print(f"Test Accuracy: {test_acc:.4f}")

# Save model
model.save("basic_mlp_model.h5")

print("\nModel saved as basic_mlp_model.h5")

# Plot accuracy and loss
plt.figure(figsize=(8, 6))
plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.title("MLP Training Accuracy and Loss")
plt.xlabel("Epoch")
plt.ylabel("Value")
plt.legend()
plt.tight_layout()
plt.savefig("mlp_training_plot.png")
plt.close()

print("Training plot saved as mlp_training_plot.png")

# Save report
with open("mlp_report.txt", "w") as file:
    file.write("Lab 21: Basic MLP with Keras/TensorFlow\n\n")
    file.write("Dataset: MNIST handwritten digits\n")
    file.write("Model: Sequential MLP\n\n")
    file.write("Layers Used:\n")
    file.write("- Flatten\n")
    file.write("- Dense 128 ReLU\n")
    file.write("- Dense 10 Softmax\n\n")
    file.write(f"Test Loss: {test_loss:.4f}\n")
    file.write(f"Test Accuracy: {test_acc:.4f}\n")

print("Report saved as mlp_report.txt")

print("\nLab completed successfully.")
