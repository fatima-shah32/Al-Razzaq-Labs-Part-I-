import numpy as np
import matplotlib.pyplot as plt

from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping
from keras.datasets import mnist
from keras.utils import to_categorical
from keras.regularizers import l2


print("=== Lab 23: Early Stopping and Model Regularization ===")

# Load MNIST dataset
(X_train, y_train), (X_val, y_val) = mnist.load_data()

print("\nDataset loaded successfully")
print("Training shape:", X_train.shape)
print("Validation shape:", X_val.shape)

# Preprocess data
X_train = X_train.reshape(X_train.shape[0], -1).astype("float32") / 255
X_val = X_val.reshape(X_val.shape[0], -1).astype("float32") / 255

y_train = to_categorical(y_train)
y_val = to_categorical(y_val)

print("\nData preprocessing completed")
print("New training shape:", X_train.shape)
print("New validation shape:", X_val.shape)

# Early stopping callback
early_stopping = EarlyStopping(
    monitor="val_loss",
    patience=3,
    restore_best_weights=True
)

# Model without L2 regularization
model = Sequential()
model.add(Dense(512, input_dim=784, activation="relu"))
model.add(Dense(10, activation="softmax"))

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

print("\nTraining model without L2 regularization")

history = model.fit(
    X_train,
    y_train,
    validation_data=(X_val, y_val),
    epochs=50,
    batch_size=200,
    callbacks=[early_stopping],
    verbose=2
)

# Model with L2 regularization
model_reg = Sequential()
model_reg.add(
    Dense(
        512,
        input_dim=784,
        activation="relu",
        kernel_regularizer=l2(0.01)
    )
)
model_reg.add(Dense(10, activation="softmax"))

model_reg.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

print("\nTraining model with L2 regularization")

history_reg = model_reg.fit(
    X_train,
    y_train,
    validation_data=(X_val, y_val),
    epochs=50,
    batch_size=200,
    callbacks=[early_stopping],
    verbose=2
)

# Evaluate both models
loss, accuracy = model.evaluate(X_val, y_val, verbose=0)
loss_reg, accuracy_reg = model_reg.evaluate(X_val, y_val, verbose=0)

print("\nModel Evaluation:")
print(f"Without L2 - Loss: {loss:.3f}, Accuracy: {accuracy:.3f}")
print(f"With L2    - Loss: {loss_reg:.3f}, Accuracy: {accuracy_reg:.3f}")

# Plot validation loss comparison
plt.figure(figsize=(8, 6))
plt.plot(history.history["val_loss"], label="Model without L2")
plt.plot(history_reg.history["val_loss"], label="Model with L2")
plt.title("Model Validation Loss Comparison")
plt.ylabel("Loss")
plt.xlabel("Epoch")
plt.legend()
plt.tight_layout()
plt.savefig("validation_loss_comparison.png")
plt.close()

print("\nValidation loss plot saved as validation_loss_comparison.png")

# Plot validation accuracy comparison
plt.figure(figsize=(8, 6))
plt.plot(history.history["val_accuracy"], label="Model without L2")
plt.plot(history_reg.history["val_accuracy"], label="Model with L2")
plt.title("Model Validation Accuracy Comparison")
plt.ylabel("Accuracy")
plt.xlabel("Epoch")
plt.legend()
plt.tight_layout()
plt.savefig("validation_accuracy_comparison.png")
plt.close()

print("Validation accuracy plot saved as validation_accuracy_comparison.png")

# Save report
with open("regularization_report.txt", "w") as file:
    file.write("Lab 23: Early Stopping and Model Regularization\n\n")
    file.write("Dataset: MNIST\n")
    file.write("Technique 1: Early Stopping\n")
    file.write("Technique 2: L2 Regularization\n\n")
    file.write(f"Without L2 - Loss: {loss:.3f}, Accuracy: {accuracy:.3f}\n")
    file.write(f"With L2    - Loss: {loss_reg:.3f}, Accuracy: {accuracy_reg:.3f}\n\n")
    file.write("Early stopping stopped training when validation loss stopped improving.\n")
    file.write("L2 regularization penalized large weights to reduce overfitting.\n")

print("Report saved as regularization_report.txt")

print("\nLab completed successfully.")
