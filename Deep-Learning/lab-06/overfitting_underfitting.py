import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

print("=== Lab 06: Overfitting and Underfitting ===")

# Task 1: Load and prepare dataset
# Note: load_boston is removed from new scikit-learn versions.
# California Housing dataset is used as a safe replacement.

housing = fetch_california_housing()

X = housing.data
y = housing.target

print("\nDataset loaded successfully")
print("Feature shape:", X.shape)
print("Target shape:", y.shape)

X_train, X_val, y_train, y_val = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining data shape:", X_train.shape)
print("Validation data shape:", X_val.shape)

# Task 2: Train simple Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

train_predictions = model.predict(X_train)
val_predictions = model.predict(X_val)

train_loss = mean_squared_error(y_train, train_predictions)
val_loss = mean_squared_error(y_val, val_predictions)

print("\nLinear Regression Losses:")
print(f"Training Loss: {train_loss:.4f}")
print(f"Validation Loss: {val_loss:.4f}")

# Plot training and validation losses
losses = [train_loss, val_loss]
labels = ["Training Loss", "Validation Loss"]

plt.figure(figsize=(7, 5))
plt.bar(labels, losses)
plt.title("Training vs Validation Loss")
plt.ylabel("Mean Squared Error")
plt.tight_layout()
plt.savefig("training_validation_loss.png")
plt.close()

print("\nLoss plot saved as training_validation_loss.png")

# Task 3: Dropout example using neural network
nn_model = Sequential([
    Dense(64, activation="relu", input_shape=(X_train.shape[1],)),
    Dropout(0.5),
    Dense(64, activation="relu"),
    Dropout(0.5),
    Dense(1)
])

nn_model.compile(
    optimizer="adam",
    loss="mean_squared_error"
)

print("\nNeural network with Dropout created successfully")
nn_model.summary()

# Train small dropout model for demonstration
history = nn_model.fit(
    X_train,
    y_train,
    validation_data=(X_val, y_val),
    epochs=10,
    batch_size=32,
    verbose=1
)

# Plot neural network loss
plt.figure(figsize=(8, 5))
plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.title("Neural Network Loss with Dropout")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.tight_layout()
plt.savefig("dropout_loss_plot.png")
plt.close()

print("Dropout loss plot saved as dropout_loss_plot.png")

# Save report
with open("overfitting_underfitting_report.txt", "w") as file:
    file.write("Lab 06: Overfitting and Underfitting\n\n")
    file.write("Dataset: California Housing\n")
    file.write("Reason: load_boston is removed in newer scikit-learn versions.\n\n")
    file.write(f"Linear Regression Training Loss: {train_loss:.4f}\n")
    file.write(f"Linear Regression Validation Loss: {val_loss:.4f}\n\n")
    file.write("Interpretation:\n")
    file.write("Overfitting occurs when training loss is low but validation loss is high.\n")
    file.write("Underfitting occurs when both training and validation losses are high.\n")
    file.write("Dropout can help reduce overfitting in neural networks.\n")

print("Report saved as overfitting_underfitting_report.txt")
print("\nLab completed successfully.")
