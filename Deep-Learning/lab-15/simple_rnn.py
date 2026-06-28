import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense

print("=== Lab 15: Introduction to Recurrent Neural Networks ===")

# Task 1: Prepare sequence dataset
X = np.array([[i, i + 1, i + 2] for i in range(100)])
y = np.array([i + 3 for i in range(100)])

print("\nOriginal X shape:", X.shape)
print("Original y shape:", y.shape)

# Reshape X into RNN format: samples, timesteps, features
X = X.reshape((X.shape[0], X.shape[1], 1))

print("Reshaped X shape:", X.shape)

# Task 2: Build Simple RNN model
timesteps = X.shape[1]
features = X.shape[2]

model = Sequential([
    SimpleRNN(
        units=50,
        activation="relu",
        input_shape=(timesteps, features)
    ),
    Dense(units=1)
])

model.compile(
    optimizer="adam",
    loss="mse"
)

print("\nModel Summary:")
model.summary()

# Train model
history = model.fit(
    X,
    y,
    epochs=100,
    verbose=1
)

# Task 3: Make predictions
y_pred = model.predict(X)

# Save predictions
results_df = pd.DataFrame({
    "Actual": y,
    "Predicted": y_pred.flatten()
})

results_df.to_csv("rnn_predictions.csv", index=False)

# Plot predictions vs actual
plt.figure(figsize=(10, 5))
plt.plot(y, label="Actual Sequence")
plt.plot(y_pred, label="Predicted Sequence", linestyle="--")
plt.legend()
plt.title("Sequence Prediction using Simple RNN")
plt.xlabel("Sample Index")
plt.ylabel("Value")
plt.tight_layout()
plt.savefig("rnn_sequence_prediction.png")
plt.close()

# Plot training loss
plt.figure(figsize=(8, 5))
plt.plot(history.history["loss"])
plt.title("RNN Training Loss")
plt.xlabel("Epoch")
plt.ylabel("Mean Squared Error")
plt.tight_layout()
plt.savefig("rnn_training_loss.png")
plt.close()

# Save model
model.save("simple_rnn_model.keras")

# Save report
with open("rnn_report.txt", "w") as file:
    file.write("Lab 15: Introduction to Recurrent Neural Networks\n\n")
    file.write("Dataset: Simple numerical sequence dataset\n")
    file.write("Task: Predict next number in a sequence\n\n")
    file.write("Example:\n")
    file.write("Input: [0, 1, 2]\n")
    file.write("Expected Output: 3\n\n")
    file.write("Model Architecture:\n")
    file.write("SimpleRNN(50 units, ReLU) -> Dense(1)\n\n")
    file.write(f"Final Training Loss: {history.history['loss'][-1]:.4f}\n")
    file.write("Predictions saved in rnn_predictions.csv\n")

print("\nFiles saved:")
print("simple_rnn_model.keras")
print("rnn_predictions.csv")
print("rnn_sequence_prediction.png")
print("rnn_training_loss.png")
print("rnn_report.txt")

print("\nLab completed successfully.")
