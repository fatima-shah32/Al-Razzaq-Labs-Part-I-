import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

print("=== Lab 24: Custom Loss Functions in Keras ===")

# Task 1: Define custom loss function
def custom_mse(y_true, y_pred):
    return tf.reduce_mean(tf.square(y_true - y_pred))

print("\nCustom MSE loss function created successfully")

# Task 2: Prepare synthetic data
np.random.seed(42)
tf.random.set_seed(42)

X_train = np.random.rand(1000, 10).astype("float32")
y_train = np.random.rand(1000, 1).astype("float32")

X_val = np.random.rand(200, 10).astype("float32")
y_val = np.random.rand(200, 1).astype("float32")

print("\nTraining data shape:", X_train.shape)
print("Validation data shape:", X_val.shape)

# Task 3: Create model with custom loss
model_custom = Sequential([
    Dense(64, activation="relu", input_shape=(10,)),
    Dense(1, activation="linear")
])

model_custom.compile(
    optimizer="adam",
    loss=custom_mse,
    metrics=["mae"]
)

print("\nModel with custom loss summary:")
model_custom.summary()

# Train model with custom loss
history_custom = model_custom.fit(
    X_train,
    y_train,
    epochs=10,
    validation_data=(X_val, y_val),
    verbose=1
)

# Evaluate custom loss model
custom_val_loss, custom_val_mae = model_custom.evaluate(
    X_val,
    y_val,
    verbose=0
)

print("\nValidation Loss with Custom MSE:", custom_val_loss)
print("Validation MAE with Custom MSE:", custom_val_mae)

# Optional comparison with built-in MSE
model_builtin = Sequential([
    Dense(64, activation="relu", input_shape=(10,)),
    Dense(1, activation="linear")
])

model_builtin.compile(
    optimizer="adam",
    loss="mse",
    metrics=["mae"]
)

print("\nTraining comparison model with built-in MSE")

history_builtin = model_builtin.fit(
    X_train,
    y_train,
    epochs=10,
    validation_data=(X_val, y_val),
    verbose=1
)

builtin_val_loss, builtin_val_mae = model_builtin.evaluate(
    X_val,
    y_val,
    verbose=0
)

# Save results
results_df = pd.DataFrame({
    "Model": ["Custom MSE", "Built-in MSE"],
    "Validation_Loss": [custom_val_loss, builtin_val_loss],
    "Validation_MAE": [custom_val_mae, builtin_val_mae]
})

results_df.to_csv("custom_loss_results.csv", index=False)

# Save training history
history_df = pd.DataFrame({
    "custom_loss": history_custom.history["loss"],
    "custom_val_loss": history_custom.history["val_loss"],
    "builtin_loss": history_builtin.history["loss"],
    "builtin_val_loss": history_builtin.history["val_loss"]
})

history_df.to_csv("training_history.csv", index=False)

# Plot validation loss comparison
plt.figure(figsize=(8, 5))
plt.plot(history_custom.history["val_loss"], label="Custom MSE Val Loss")
plt.plot(history_builtin.history["val_loss"], label="Built-in MSE Val Loss")
plt.title("Custom Loss vs Built-in Loss")
plt.xlabel("Epoch")
plt.ylabel("Validation Loss")
plt.legend()
plt.tight_layout()
plt.savefig("custom_loss_comparison.png")
plt.close()

# Save models
model_custom.save("model_custom_loss.keras")
model_builtin.save("model_builtin_mse.keras")

# Save report
with open("custom_loss_report.txt", "w") as file:
    file.write("Lab 24: Custom Loss Functions in Keras\n\n")
    file.write("Custom loss implemented:\n")
    file.write("custom_mse = mean(square(y_true - y_pred))\n\n")
    file.write("Dataset: Synthetic regression dataset\n")
    file.write("Model: Dense neural network\n\n")
    file.write("Results:\n")
    file.write(results_df.to_string(index=False))
    file.write("\n\nObservation:\n")
    file.write("Custom loss functions allow flexible model training for specific problems.\n")
    file.write("The custom MSE behaved similarly to built-in MSE because both compute mean squared error.\n")

print("\nFiles saved:")
print("custom_loss_results.csv")
print("training_history.csv")
print("custom_loss_comparison.png")
print("model_custom_loss.keras")
print("model_builtin_mse.keras")
print("custom_loss_report.txt")

print("\nLab completed successfully.")
