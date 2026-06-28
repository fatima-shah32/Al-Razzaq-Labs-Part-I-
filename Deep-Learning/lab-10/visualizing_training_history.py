import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.datasets import mnist

print("=== Lab 10: Visualizing Training History ===")

# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize data
x_train = x_train / 255.0
x_test = x_test / 255.0

print("\nDataset loaded and normalized successfully")
print("Training data shape:", x_train.shape)
print("Testing data shape:", x_test.shape)

# Build simple neural network
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation="relu"),
    Dense(10, activation="softmax")
])

# Compile model
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

print("\nModel Summary:")
model.summary()

# Train model and record history
history = model.fit(
    x_train,
    y_train,
    epochs=10,
    validation_split=0.2,
    batch_size=64,
    verbose=1
)

print("\nHistory keys:")
print(history.history.keys())

# Save training history as CSV
history_df = pd.DataFrame(history.history)
history_df.to_csv("training_history.csv", index=False)

# Plot loss curves
plt.figure(figsize=(8, 5))
plt.plot(history.history["loss"], label="Train Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.title("Loss Curves")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()
plt.tight_layout()
plt.savefig("loss_curves.png")
plt.close()

# Plot accuracy curves
plt.figure(figsize=(8, 5))
plt.plot(history.history["accuracy"], label="Train Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.title("Accuracy Curves")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.legend()
plt.tight_layout()
plt.savefig("accuracy_curves.png")
plt.close()

# Evaluate model
test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=0)

print("\nTest Loss:", round(test_loss, 4))
print("Test Accuracy:", round(test_accuracy, 4))

# Analyze convergence
final_train_loss = history.history["loss"][-1]
final_val_loss = history.history["val_loss"][-1]
final_train_acc = history.history["accuracy"][-1]
final_val_acc = history.history["val_accuracy"][-1]

with open("training_analysis_report.txt", "w") as file:
    file.write("Lab 10: Visualizing Training History\n\n")
    file.write("Dataset: MNIST\n")
    file.write("Model: Simple Neural Network\n\n")
    file.write(f"Final Training Loss: {final_train_loss:.4f}\n")
    file.write(f"Final Validation Loss: {final_val_loss:.4f}\n")
    file.write(f"Final Training Accuracy: {final_train_acc:.4f}\n")
    file.write(f"Final Validation Accuracy: {final_val_acc:.4f}\n")
    file.write(f"Test Loss: {test_loss:.4f}\n")
    file.write(f"Test Accuracy: {test_accuracy:.4f}\n\n")
    file.write("Analysis:\n")
    file.write("Training and validation curves help show model convergence.\n")
    file.write("If training loss decreases but validation loss increases, the model may be overfitting.\n")
    file.write("If both losses remain high, the model may be underfitting.\n")

print("\nFiles saved:")
print("training_history.csv")
print("loss_curves.png")
print("accuracy_curves.png")
print("training_analysis_report.txt")

print("\nLab completed successfully.")
