import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping

print("=== Lab 28: Implementing Early Stopping ===")

# Reproducibility
np.random.seed(42)
tf.random.set_seed(42)

# Task 1: Prepare synthetic dataset
X_train = np.random.rand(1000, 20).astype("float32")
y_train = np.random.randint(2, size=(1000, 1)).astype("float32")

X_val = np.random.rand(200, 20).astype("float32")
y_val = np.random.randint(2, size=(200, 1)).astype("float32")

print("\nTraining data shape:", X_train.shape)
print("Validation data shape:", X_val.shape)

# Task 2: Build Keras model
model = Sequential([
    Dense(64, activation="relu", input_shape=(20,)),
    Dense(32, activation="relu"),
    Dense(1, activation="sigmoid")
])

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

print("\nModel Summary:")
model.summary()

# Task 3: Early Stopping callback
early_stopping = EarlyStopping(
    monitor="val_loss",
    patience=5,
    restore_best_weights=True
)

print("\nEarlyStopping configured:")
print("Monitor: val_loss")
print("Patience: 5")
print("Restore Best Weights: True")

# Train model
history = model.fit(
    X_train,
    y_train,
    epochs=100,
    batch_size=32,
    validation_data=(X_val, y_val),
    callbacks=[early_stopping],
    verbose=1
)

epochs_ran = len(history.history["loss"])

print("\nTraining stopped after", epochs_ran, "epochs")

# Evaluate model
val_loss, val_accuracy = model.evaluate(
    X_val,
    y_val,
    verbose=0
)

print("\nValidation Loss:", round(val_loss, 4))
print("Validation Accuracy:", round(val_accuracy, 4))

# Save model
model.save("early_stopping_model.keras")

# Save training history
history_df = pd.DataFrame(history.history)
history_df.to_csv("early_stopping_history.csv", index=False)

# Plot loss
plt.figure(figsize=(8, 5))
plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("Training Loss with Early Stopping")
plt.legend()
plt.tight_layout()
plt.savefig("early_stopping_loss.png")
plt.close()

# Plot accuracy
plt.figure(figsize=(8, 5))
plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.title("Training Accuracy with Early Stopping")
plt.legend()
plt.tight_layout()
plt.savefig("early_stopping_accuracy.png")
plt.close()

# Save report
with open("early_stopping_report.txt", "w") as file:
    file.write("Lab 28: Implementing Early Stopping\n\n")
    file.write("Dataset: Synthetic binary classification dataset\n")
    file.write("Model: Dense neural network\n\n")
    file.write("Early Stopping Settings:\n")
    file.write("Monitor: val_loss\n")
    file.write("Patience: 5\n")
    file.write("Restore Best Weights: True\n\n")
    file.write(f"Maximum Epochs: 100\n")
    file.write(f"Actual Epochs Completed: {epochs_ran}\n")
    file.write(f"Validation Loss: {val_loss:.4f}\n")
    file.write(f"Validation Accuracy: {val_accuracy:.4f}\n\n")
    file.write("Observation:\n")
    file.write("Early stopping stops training when validation loss stops improving.\n")
    file.write("It saves training time and helps reduce overfitting.\n")

print("\nFiles saved:")
print("early_stopping_model.keras")
print("early_stopping_history.csv")
print("early_stopping_loss.png")
print("early_stopping_accuracy.png")
print("early_stopping_report.txt")

print("\nLab completed successfully.")
