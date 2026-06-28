import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

print("=== Lab 04: Building a Simple Feedforward Neural Network ===")

# Task 1: Create Sequential Model
model = Sequential()

# Task 2: Add Dense Layers
model.add(Dense(units=8, input_shape=(4,), activation="relu"))

model.add(Dense(units=16, activation="relu"))

model.add(Dense(units=3, activation="softmax"))

# Task 3: Compile Model
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

print("\nModel created and compiled successfully.\n")

# Display model summary
model.summary()

# Save model architecture summary
with open("model_summary.txt", "w") as file:
    model.summary(print_fn=lambda x: file.write(x + "\n"))

# Save model
model.save("feedforward_model.keras")

print("\nModel summary saved as model_summary.txt")
print("Model saved as feedforward_model.keras")
print("\nLab completed successfully.")
