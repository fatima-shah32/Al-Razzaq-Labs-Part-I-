import numpy as np
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import model_from_json

print("=== Lab 13: Saving and Loading Deep Learning Models ===")

# Task 1: Create simple model
model = Sequential([
    Dense(32, activation="relu", input_shape=(784,)),
    Dense(10, activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

print("\nOriginal Model Summary:")
model.summary()

# Save model architecture to JSON
model_json = model.to_json()

with open("model_architecture.json", "w") as json_file:
    json_file.write(model_json)

print("\nModel architecture saved as model_architecture.json")

# Save model weights
model.save_weights("model_weights.weights.h5")

print("Model weights saved as model_weights.weights.h5")

# Task 2: Load architecture from JSON
with open("model_architecture.json", "r") as json_file:
    loaded_model_json = json_file.read()

loaded_model = model_from_json(loaded_model_json)

# Load weights
loaded_model.load_weights("model_weights.weights.h5")

loaded_model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

print("\nLoaded Model Summary:")
loaded_model.summary()

# Task 3: Verify predictions post-load
np.random.seed(42)

example_data = np.random.random((1, 784))

original_prediction = model.predict(example_data)
loaded_prediction = loaded_model.predict(example_data)

print("\nOriginal Prediction:")
print(original_prediction)

print("\nLoaded Prediction:")
print(loaded_prediction)

# Compare predictions
difference = np.max(
    np.abs(original_prediction - loaded_prediction)
)

print("\nMaximum prediction difference:", difference)

if difference < 1e-6:
    result = "Predictions match successfully."
else:
    result = "Predictions are different."

print(result)

# Save report
with open("model_persistence_report.txt", "w") as file:
    file.write("Lab 13: Saving and Loading Deep Learning Models\n\n")
    file.write("Tasks Completed:\n")
    file.write("1. Created a simple neural network model.\n")
    file.write("2. Saved model architecture to JSON.\n")
    file.write("3. Saved model weights to HDF5.\n")
    file.write("4. Loaded architecture from JSON.\n")
    file.write("5. Restored weights from HDF5.\n")
    file.write("6. Compared original and loaded model predictions.\n\n")
    file.write(f"Maximum Prediction Difference: {difference}\n")
    file.write(f"Result: {result}\n")

print("\nReport saved as model_persistence_report.txt")
print("\nLab completed successfully.")
