import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

print("=== Lab 05: Exploring Activation Functions ===")

# Reproducibility
np.random.seed(42)
tf.random.set_seed(42)

# Sample data
X_train = np.random.rand(100, 10)
y_train = np.random.rand(100, 1)

print("\nTraining data shape:", X_train.shape)
print("Target data shape:", y_train.shape)

# Function to build model
def build_model(activation_name):
    model = Sequential([
        Dense(
            64,
            activation=activation_name,
            input_shape=(10,)
        ),
        Dense(1)
    ])

    model.compile(
        optimizer="adam",
        loss="mse"
    )

    return model


# Build models
model_relu = build_model("relu")
model_sigmoid = build_model("sigmoid")
model_tanh = build_model("tanh")

# Train ReLU model
print("\nTraining model with ReLU activation")
history_relu = model_relu.fit(
    X_train,
    y_train,
    epochs=10,
    verbose=1
)

# Train Sigmoid model
print("\nTraining model with Sigmoid activation")
history_sigmoid = model_sigmoid.fit(
    X_train,
    y_train,
    epochs=10,
    verbose=1
)

# Train Tanh model
print("\nTraining model with Tanh activation")
history_tanh = model_tanh.fit(
    X_train,
    y_train,
    epochs=10,
    verbose=1
)

# Extract losses
loss_values_relu = history_relu.history["loss"]
loss_values_sigmoid = history_sigmoid.history["loss"]
loss_values_tanh = history_tanh.history["loss"]

# Save results as CSV
results_df = pd.DataFrame({
    "Epoch": list(range(1, 11)),
    "ReLU_Loss": loss_values_relu,
    "Sigmoid_Loss": loss_values_sigmoid,
    "Tanh_Loss": loss_values_tanh
})

results_df.to_csv("activation_loss_results.csv", index=False)

print("\nTraining Loss Results:")
print(results_df)

# Plot loss comparison
plt.figure(figsize=(8, 5))
plt.plot(loss_values_relu, marker="o", label="ReLU")
plt.plot(loss_values_sigmoid, marker="o", label="Sigmoid")
plt.plot(loss_values_tanh, marker="o", label="Tanh")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training Loss Comparison")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("activation_loss_comparison.png")
plt.close()

print("\nLoss comparison plot saved as activation_loss_comparison.png")

# Make sample predictions
sample_input = X_train[:5]

relu_predictions = model_relu.predict(sample_input)
sigmoid_predictions = model_sigmoid.predict(sample_input)
tanh_predictions = model_tanh.predict(sample_input)

prediction_df = pd.DataFrame({
    "ReLU_Prediction": relu_predictions.flatten(),
    "Sigmoid_Prediction": sigmoid_predictions.flatten(),
    "Tanh_Prediction": tanh_predictions.flatten()
})

prediction_df.to_csv("activation_predictions.csv", index=False)

print("\nSample Predictions:")
print(prediction_df)

# Final report
with open("activation_report.txt", "w") as file:
    file.write("Lab 05: Exploring Activation Functions\n\n")
    file.write("Activation functions tested: ReLU, Sigmoid, Tanh\n")
    file.write("Dataset: Random synthetic dataset\n")
    file.write("Model: Small feedforward neural network\n\n")

    file.write("Final Loss Values:\n")
    file.write(f"ReLU Final Loss: {loss_values_relu[-1]:.4f}\n")
    file.write(f"Sigmoid Final Loss: {loss_values_sigmoid[-1]:.4f}\n")
    file.write(f"Tanh Final Loss: {loss_values_tanh[-1]:.4f}\n\n")

    file.write("Observation:\n")
    file.write("ReLU usually learns quickly and is commonly used in hidden layers.\n")
    file.write("Sigmoid can be useful but may suffer from vanishing gradients.\n")
    file.write("Tanh centers outputs around zero and can converge better than sigmoid in some cases.\n")

print("Report saved as activation_report.txt")
print("\nLab completed successfully.")
