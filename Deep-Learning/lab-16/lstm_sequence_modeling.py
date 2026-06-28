import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from tensorflow.keras.preprocessing.sequence import TimeseriesGenerator

print("=== Lab 16: LSTM Networks for Sequence Modeling ===")

# Task 1: Create dummy time-series dataset
data = np.sin(np.linspace(0, 50, 500))

print("\nDataset created successfully")
print("Data shape:", data.shape)

# Save original data
data_df = pd.DataFrame({
    "Index": range(len(data)),
    "Value": data
})

data_df.to_csv("time_series_data.csv", index=False)

# Task 2: Prepare data for LSTM
n_steps = 3
n_features = 1

generator = TimeseriesGenerator(
    data,
    data,
    length=n_steps,
    batch_size=1
)

print("\nTimeseriesGenerator created successfully")
print("Number of generated samples:", len(generator))

# Build LSTM model
model = Sequential([
    LSTM(
        units=50,
        activation="relu",
        input_shape=(n_steps, n_features)
    ),
    Dense(1)
])

model.compile(
    optimizer="adam",
    loss="mse"
)

print("\nModel Summary:")
model.summary()

# Train model
history = model.fit(
    generator,
    epochs=50,
    verbose=1
)

# Task 3: Predictions
predictions = model.predict(generator)

print("\nPredictions generated successfully")
print("Predictions shape:", predictions.shape)

# Save predictions
prediction_df = pd.DataFrame({
    "Actual": data[n_steps:],
    "Predicted": predictions.flatten()
})

prediction_df.to_csv("lstm_predictions.csv", index=False)

# Plot actual vs predicted
plt.figure(figsize=(10, 5))
plt.plot(data, label="Actual Data")
plt.plot(
    range(n_steps, len(predictions) + n_steps),
    predictions,
    label="Predicted Data",
    linestyle="--"
)
plt.title("LSTM Sequence Prediction")
plt.xlabel("Time Step")
plt.ylabel("Value")
plt.legend()
plt.tight_layout()
plt.savefig("lstm_prediction_plot.png")
plt.close()

# Plot training loss
plt.figure(figsize=(8, 5))
plt.plot(history.history["loss"])
plt.title("LSTM Training Loss")
plt.xlabel("Epoch")
plt.ylabel("Mean Squared Error")
plt.tight_layout()
plt.savefig("lstm_training_loss.png")
plt.close()

# Save model
model.save("lstm_sequence_model.keras")

# Save report
with open("lstm_report.txt", "w") as file:
    file.write("Lab 16: LSTM Networks for Sequence Modeling\n\n")
    file.write("Dataset: Synthetic sine wave time-series data\n")
    file.write("Task: Predict next value in a sequence\n\n")
    file.write("Model Architecture:\n")
    file.write("LSTM(50 units, ReLU) -> Dense(1)\n\n")
    file.write(f"Number of time steps: {n_steps}\n")
    file.write(f"Number of features: {n_features}\n")
    file.write(f"Final Training Loss: {history.history['loss'][-1]:.6f}\n\n")
    file.write("Conclusion:\n")
    file.write("The LSTM model learned sequence patterns from sine wave data and generated predictions.\n")

print("\nFiles saved:")
print("time_series_data.csv")
print("lstm_predictions.csv")
print("lstm_prediction_plot.png")
print("lstm_training_loss.png")
print("lstm_sequence_model.keras")
print("lstm_report.txt")

print("\nLab completed successfully.")
