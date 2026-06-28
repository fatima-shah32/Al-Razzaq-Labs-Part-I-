import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

print("=== Lab 12: Implementing Dropout Regularization ===")

# Task 1: Load and preprocess MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape((x_train.shape[0], 28, 28, 1)).astype("float32") / 255
x_test = x_test.reshape((x_test.shape[0], 28, 28, 1)).astype("float32") / 255

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

print("\nDataset loaded and preprocessed successfully")
print("Training data shape:", x_train.shape)
print("Testing data shape:", x_test.shape)

# Model without Dropout
def create_model_without_dropout():
    model = Sequential([
        Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(128, activation="relu"),
        Dense(10, activation="softmax")
    ])

    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model

# Model with Dropout
def create_model_with_dropout():
    model = Sequential([
        Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),
        MaxPooling2D((2, 2)),
        Dropout(0.25),
        Flatten(),
        Dense(128, activation="relu"),
        Dropout(0.5),
        Dense(10, activation="softmax")
    ])

    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model

model_without_dropout = create_model_without_dropout()
model_with_dropout = create_model_with_dropout()

print("\nTraining CNN without Dropout")
history_without_dropout = model_without_dropout.fit(
    x_train,
    y_train,
    epochs=5,
    batch_size=128,
    validation_data=(x_test, y_test),
    verbose=1
)

print("\nTraining CNN with Dropout")
history_with_dropout = model_with_dropout.fit(
    x_train,
    y_train,
    epochs=5,
    batch_size=128,
    validation_data=(x_test, y_test),
    verbose=1
)

# Evaluate both models
loss_no_dropout, acc_no_dropout = model_without_dropout.evaluate(
    x_test,
    y_test,
    verbose=0
)

loss_dropout, acc_dropout = model_with_dropout.evaluate(
    x_test,
    y_test,
    verbose=0
)

print("\nFinal Evaluation:")
print(f"No Dropout Accuracy: {acc_no_dropout:.4f}")
print(f"With Dropout Accuracy: {acc_dropout:.4f}")

# Save comparison metrics
results_df = pd.DataFrame({
    "Model": ["Without Dropout", "With Dropout"],
    "Test_Loss": [loss_no_dropout, loss_dropout],
    "Test_Accuracy": [acc_no_dropout, acc_dropout]
})

results_df.to_csv("dropout_comparison_results.csv", index=False)

# Plot accuracy comparison
plt.figure(figsize=(8, 5))
plt.plot(history_without_dropout.history["accuracy"], label="Train No Dropout")
plt.plot(history_without_dropout.history["val_accuracy"], label="Val No Dropout")
plt.plot(history_with_dropout.history["accuracy"], label="Train Dropout")
plt.plot(history_with_dropout.history["val_accuracy"], label="Val Dropout")
plt.title("Model Accuracy Comparison")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.tight_layout()
plt.savefig("dropout_accuracy_comparison.png")
plt.close()

# Plot loss comparison
plt.figure(figsize=(8, 5))
plt.plot(history_without_dropout.history["loss"], label="Train No Dropout")
plt.plot(history_without_dropout.history["val_loss"], label="Val No Dropout")
plt.plot(history_with_dropout.history["loss"], label="Train Dropout")
plt.plot(history_with_dropout.history["val_loss"], label="Val Dropout")
plt.title("Model Loss Comparison")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.tight_layout()
plt.savefig("dropout_loss_comparison.png")
plt.close()

# Save models
model_without_dropout.save("cnn_without_dropout.keras")
model_with_dropout.save("cnn_with_dropout.keras")

# Save report
with open("dropout_report.txt", "w") as file:
    file.write("Lab 12: Implementing Dropout Regularization\n\n")
    file.write("Dataset: MNIST\n")
    file.write("Model: CNN with and without Dropout\n\n")
    file.write(f"No Dropout Accuracy: {acc_no_dropout:.4f}\n")
    file.write(f"With Dropout Accuracy: {acc_dropout:.4f}\n\n")
    file.write("Observation:\n")
    file.write("Dropout randomly disables neurons during training.\n")
    file.write("This helps reduce overfitting and improves generalization.\n")
    file.write("The model with dropout may train slightly slower but often performs better on unseen data.\n")

print("\nFiles saved:")
print("dropout_comparison_results.csv")
print("dropout_accuracy_comparison.png")
print("dropout_loss_comparison.png")
print("cnn_without_dropout.keras")
print("cnn_with_dropout.keras")
print("dropout_report.txt")

print("\nLab completed successfully.")
