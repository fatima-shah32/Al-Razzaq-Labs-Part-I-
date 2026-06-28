import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GRU, LSTM, Dense

print("=== Lab 17: Exploring GRU Networks ===")

# Task 1: Create sample time-series dataset
np.random.seed(42)

time_steps = np.arange(0, 500)
values = np.sin(0.05 * time_steps) + 0.1 * np.random.randn(500)

df = pd.DataFrame({
    "time_step": time_steps,
    "value": values
})

df.to_csv("sample_time_series.csv", index=False)

print("\nSample time-series dataset created")
print(df.head())

# Scale data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(df[["value"]])

# Create sequences
def create_sequences(data, seq_length):
    X = []
    y = []

    for i in range(len(data) - seq_length):
        X.append(data[i:i + seq_length])
        y.append(data[i + seq_length])

    return np.array(X), np.array(y)

sequence_length = 50

X, y = create_sequences(scaled_data, sequence_length)

print("\nSequence data prepared")
print("X shape:", X.shape)
print("y shape:", y.shape)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)

# Task 2: Build GRU model
def build_gru_model():
    model = Sequential([
        GRU(
            units=50,
            return_sequences=True,
            input_shape=(sequence_length, 1)
        ),
        GRU(units=50),
        Dense(units=1)
    ])

    model.compile(
        optimizer="adam",
        loss="mean_squared_error"
    )

    return model

# Build LSTM model for comparison
def build_lstm_model():
    model = Sequential([
        LSTM(
            units=50,
            return_sequences=True,
            input_shape=(sequence_length, 1)
        ),
        LSTM(units=50),
        Dense(units=1)
    ])

    model.compile(
        optimizer="adam",
        loss="mean_squared_error"
    )

    return model

gru_model = build_gru_model()
lstm_model = build_lstm_model()

print("\nGRU Model Summary:")
gru_model.summary()

print("\nTraining GRU model")
start_time = time.time()

history_gru = gru_model.fit(
    X_train,
    y_train,
    epochs=20,
    batch_size=32,
    validation_data=(X_test, y_test),
    verbose=1
)

gru_training_time = time.time() - start_time

# Train LSTM model for comparison
print("\nTraining LSTM model for comparison")
start_time = time.time()

history_lstm = lstm_model.fit(
    X_train,
    y_train,
    epochs=20,
    batch_size=32,
    validation_data=(X_test, y_test),
    verbose=1
)

lstm_training_time = time.time() - start_time

# Task 3: Evaluate models
gru_test_loss = gru_model.evaluate(X_test, y_test, verbose=0)
lstm_test_loss = lstm_model.evaluate(X_test, y_test, verbose=0)

print("\nModel Evaluation:")
print(f"GRU Test Loss: {gru_test_loss:.6f}")
print(f"LSTM Test Loss: {lstm_test_loss:.6f}")

print(f"GRU Training Time: {gru_training_time:.2f} seconds")
print(f"LSTM Training Time: {lstm_training_time:.2f} seconds")

# Predictions
gru_predictions = gru_model.predict(X_test)
lstm_predictions = lstm_model.predict(X_test)

# Save comparison results
comparison_df = pd.DataFrame({
    "Model": ["GRU", "LSTM"],
    "Test_Loss": [gru_test_loss, lstm_test_loss],
    "Training_Time_Seconds": [gru_training_time, lstm_training_time]
})

comparison_df.to_csv("gru_lstm_comparison.csv", index=False)

# Plot GRU training history
plt.figure(figsize=(8, 5))
plt.plot(history_gru.history["loss"], label="GRU Training Loss")
plt.plot(history_gru.history["val_loss"], label="GRU Validation Loss")
plt.title("GRU Training and Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.tight_layout()
plt.savefig("gru_training_loss.png")
plt.close()

# Plot GRU vs LSTM validation loss
plt.figure(figsize=(8, 5))
plt.plot(history_gru.history["val_loss"], label="GRU Validation Loss")
plt.plot(history_lstm.history["val_loss"], label="LSTM Validation Loss")
plt.title("GRU vs LSTM Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.tight_layout()
plt.savefig("gru_lstm_validation_comparison.png")
plt.close()

# Plot predictions
plt.figure(figsize=(10, 5))
plt.plot(y_test[:50].flatten(), label="Actual")
plt.plot(gru_predictions[:50].flatten(), label="GRU Prediction", linestyle="--")
plt.plot(lstm_predictions[:50].flatten(), label="LSTM Prediction", linestyle=":")
plt.title("GRU vs LSTM Predictions")
plt.xlabel("Sample Index")
plt.ylabel("Scaled Value")
plt.legend()
plt.tight_layout()
plt.savefig("gru_lstm_predictions.png")
plt.close()

# Save models
gru_model.save("gru_model.keras")
lstm_model.save("lstm_model.keras")

# Save report
with open("gru_report.txt", "w") as file:
    file.write("Lab 17: Exploring GRU Networks\n\n")
    file.write("Dataset: Synthetic noisy sine wave time-series dataset\n")
    file.write(f"Sequence Length: {sequence_length}\n\n")

    file.write("Model Comparison:\n")
    file.write(f"GRU Test Loss: {gru_test_loss:.6f}\n")
    file.write(f"LSTM Test Loss: {lstm_test_loss:.6f}\n")
    file.write(f"GRU Training Time: {gru_training_time:.2f} seconds\n")
    file.write(f"LSTM Training Time: {lstm_training_time:.2f} seconds\n\n")

    file.write("Observation:\n")
    file.write("GRU networks are simpler than LSTM networks because they use fewer gates.\n")
    file.write("GRU models can train faster while still performing well on sequence data.\n")
    file.write("LSTM models may perform better on longer or more complex sequences.\n")

print("\nFiles saved:")
print("sample_time_series.csv")
print("gru_lstm_comparison.csv")
print("gru_training_loss.png")
print("gru_lstm_validation_comparison.png")
print("gru_lstm_predictions.png")
print("gru_model.keras")
print("lstm_model.keras")
print("gru_report.txt")

print("\nLab completed successfully.")
