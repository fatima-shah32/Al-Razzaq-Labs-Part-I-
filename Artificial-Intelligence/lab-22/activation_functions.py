import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LeakyReLU
from tensorflow.keras.optimizers import Adam

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler


print("=== Lab 22: Intro to Activation Functions ===")

# Load Iris dataset
iris = load_iris()

X = iris.data
y = iris.target.reshape(-1, 1)

# One-hot encode labels
encoder = OneHotEncoder(sparse_output=False)
y_encoded = encoder.fit_transform(y)

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y_encoded,
    test_size=0.2,
    random_state=42
)

print("\nDataset loaded and prepared successfully")
print("Training shape:", X_train.shape)
print("Testing shape:", X_test.shape)

# Build model function
def build_model(activation_function):
    model = Sequential()

    if activation_function == "leaky_relu":
        model.add(Dense(64, input_shape=(4,)))
        model.add(LeakyReLU(alpha=0.01))
        model.add(Dense(64))
        model.add(LeakyReLU(alpha=0.01))
    else:
        model.add(
            Dense(
                64,
                input_shape=(4,),
                activation=activation_function
            )
        )
        model.add(
            Dense(
                64,
                activation=activation_function
            )
        )

    model.add(Dense(3, activation="softmax"))

    model.compile(
        optimizer=Adam(),
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model


# Activation functions to test
activation_functions = [
    "sigmoid",
    "tanh",
    "relu",
    "leaky_relu"
]

results = []

history_records = {}

for func in activation_functions:

    print(f"\nTraining MLP with {func} activation function")

    model = build_model(func)

    history = model.fit(
        X_train,
        y_train,
        epochs=50,
        batch_size=5,
        validation_split=0.1,
        verbose=0
    )

    loss, accuracy = model.evaluate(
        X_test,
        y_test,
        verbose=0
    )

    print(f"Test Loss: {loss:.4f}")
    print(f"Test Accuracy: {accuracy:.4f}")

    results.append({
        "Activation Function": func,
        "Test Loss": round(loss, 4),
        "Test Accuracy": round(accuracy, 4)
    })

    history_records[func] = history.history

# Save results
results_df = pd.DataFrame(results)

print("\nActivation Function Comparison:")
print(results_df)

results_df.to_csv("activation_results.csv", index=False)

# Plot validation accuracy
plt.figure(figsize=(8, 6))

for func in activation_functions:
    plt.plot(
        history_records[func]["val_accuracy"],
        label=func
    )

plt.title("Validation Accuracy Comparison")
plt.xlabel("Epoch")
plt.ylabel("Validation Accuracy")
plt.legend()
plt.tight_layout()
plt.savefig("activation_accuracy_comparison.png")
plt.close()

# Plot validation loss
plt.figure(figsize=(8, 6))

for func in activation_functions:
    plt.plot(
        history_records[func]["val_loss"],
        label=func
    )

plt.title("Validation Loss Comparison")
plt.xlabel("Epoch")
plt.ylabel("Validation Loss")
plt.legend()
plt.tight_layout()
plt.savefig("activation_loss_comparison.png")
plt.close()

print("\nPlots saved:")
print("activation_accuracy_comparison.png")
print("activation_loss_comparison.png")

# Save report
with open("activation_report.txt", "w") as file:
    file.write("Lab 22: Intro to Activation Functions\n\n")
    file.write("Dataset: Iris\n")
    file.write("Model: Simple MLP\n\n")
    file.write("Activation Function Results:\n")
    file.write(results_df.to_string(index=False))
    file.write("\n\nObservations:\n")
    file.write("Sigmoid can suffer from vanishing gradients.\n")
    file.write("Tanh usually performs better than sigmoid.\n")
    file.write("ReLU often converges faster in neural networks.\n")
    file.write("Leaky ReLU helps avoid the dying ReLU problem.\n")

print("Report saved as activation_report.txt")
print("\nLab completed successfully.")
