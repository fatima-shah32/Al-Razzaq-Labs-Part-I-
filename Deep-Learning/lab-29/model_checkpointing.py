import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.callbacks import ModelCheckpoint

print("=== Lab 29: Model Checkpointing ===")

# Create checkpoints folder
os.makedirs("checkpoints", exist_ok=True)

# Task 1: Load MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize data
x_train = x_train / 255.0
x_test = x_test / 255.0

print("\nDataset loaded successfully")
print("Training data shape:", x_train.shape)
print("Testing data shape:", x_test.shape)

# Task 2: Define simple model
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(64, activation="relu"),
    Dense(64, activation="relu"),
    Dense(10, activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

print("\nModel Summary:")
model.summary()

# Task 3: ModelCheckpoint callback
checkpoint_path = "checkpoints/best_model.weights.h5"

checkpoint = ModelCheckpoint(
    filepath=checkpoint_path,
    monitor="val_accuracy",
    save_best_only=True,
    save_weights_only=True,
    mode="max",
    verbose=1
)

print("\nModelCheckpoint configured")
print("Saving best weights to:", checkpoint_path)

# Task 4: Train model with checkpointing
history = model.fit(
    x_train,
    y_train,
    validation_split=0.2,
    epochs=10,
    batch_size=128,
    callbacks=[checkpoint],
    verbose=1
)

# Evaluate model before loading checkpoint
current_loss, current_accuracy = model.evaluate(
    x_test,
    y_test,
    verbose=0
)

print("\nCurrent Model Test Accuracy:", round(current_accuracy, 4))

# Task 5: Reload best weights
model.load_weights(checkpoint_path)

best_loss, best_accuracy = model.evaluate(
    x_test,
    y_test,
    verbose=0
)

print("Best Checkpoint Test Accuracy:", round(best_accuracy, 4))

# Save final full model after loading best checkpoint
model.save("best_checkpoint_model.keras")

# Save training history
history_df = pd.DataFrame(history.history)
history_df.to_csv("checkpoint_training_history.csv", index=False)

# Plot accuracy
plt.figure(figsize=(8, 5))
plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.title("Model Accuracy with Checkpointing")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.tight_layout()
plt.savefig("checkpoint_accuracy_plot.png")
plt.close()

# Plot loss
plt.figure(figsize=(8, 5))
plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.title("Model Loss with Checkpointing")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.tight_layout()
plt.savefig("checkpoint_loss_plot.png")
plt.close()

# Save report
with open("checkpoint_report.txt", "w") as file:
    file.write("Lab 29: Model Checkpointing\n\n")
    file.write("Dataset: MNIST handwritten digits\n")
    file.write("Model: Dense neural network\n\n")
    file.write("Checkpoint Settings:\n")
    file.write("Monitor: val_accuracy\n")
    file.write("Save Best Only: True\n")
    file.write("Save Weights Only: True\n")
    file.write("Mode: max\n")
    file.write(f"Checkpoint Path: {checkpoint_path}\n\n")
    file.write(f"Current Model Test Accuracy: {current_accuracy:.4f}\n")
    file.write(f"Best Checkpoint Test Accuracy: {best_accuracy:.4f}\n\n")
    file.write("Observation:\n")
    file.write("ModelCheckpoint saves the best model weights during training.\n")
    file.write("Reloading the best checkpoint helps preserve the best validation performance.\n")

print("\nFiles saved:")
print("checkpoints/best_model.weights.h5")
print("best_checkpoint_model.keras")
print("checkpoint_training_history.csv")
print("checkpoint_accuracy_plot.png")
print("checkpoint_loss_plot.png")
print("checkpoint_report.txt")

print("\nLab completed successfully.")
