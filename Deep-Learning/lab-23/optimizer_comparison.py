import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt

from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten

print("=== Lab 23: Experimenting with Different Optimizers ===")

# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize image data
x_train = x_train / 255.0
x_test = x_test / 255.0

# One-hot encode labels
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

print("\nDataset loaded and preprocessed successfully")

# Define model architecture
def create_model():
    model = Sequential([
        Flatten(input_shape=(28, 28)),
        Dense(128, activation="relu"),
        Dense(10, activation="softmax")
    ])
    return model

optimizers = {
    "SGD": "sgd",
    "Adam": "adam",
    "RMSprop": "rmsprop"
}

histories = {}
results = []

# Train identical models with different optimizers
for optimizer_name, optimizer_value in optimizers.items():
    print(f"\nTraining model with {optimizer_name} optimizer")

    model = create_model()

    model.compile(
        optimizer=optimizer_value,
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )

    history = model.fit(
        x_train,
        y_train,
        epochs=5,
        batch_size=128,
        validation_data=(x_test, y_test),
        verbose=1
    )

    test_loss, test_accuracy = model.evaluate(
        x_test,
        y_test,
        verbose=0
    )

    histories[optimizer_name] = history

    results.append({
        "Optimizer": optimizer_name,
        "Test_Loss": test_loss,
        "Test_Accuracy": test_accuracy,
        "Final_Train_Accuracy": history.history["accuracy"][-1],
        "Final_Validation_Accuracy": history.history["val_accuracy"][-1]
    })

    model.save(f"model_{optimizer_name.lower()}.keras")

# Save results
results_df = pd.DataFrame(results)
results_df.to_csv("optimizer_comparison_results.csv", index=False)

print("\nOptimizer Comparison Results:")
print(results_df)

# Plot validation accuracy comparison
plt.figure(figsize=(8, 5))
for optimizer_name, history in histories.items():
    plt.plot(
        history.history["val_accuracy"],
        label=f"{optimizer_name} Val Accuracy"
    )

plt.title("Validation Accuracy Comparison")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("optimizer_accuracy_comparison.png")
plt.close()

# Plot validation loss comparison
plt.figure(figsize=(8, 5))
for optimizer_name, history in histories.items():
    plt.plot(
        history.history["val_loss"],
        label=f"{optimizer_name} Val Loss"
    )

plt.title("Validation Loss Comparison")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("optimizer_loss_comparison.png")
plt.close()

# Save report
with open("optimizer_report.txt", "w") as file:
    file.write("Lab 23: Experimenting with Different Optimizers\n\n")
    file.write("Dataset: MNIST\n")
    file.write("Optimizers Compared: SGD, Adam, RMSprop\n\n")
    file.write(results_df.to_string(index=False))
    file.write("\n\nObservation:\n")
    file.write("SGD is simple but may converge slower.\n")
    file.write("Adam adapts learning rates and often performs well quickly.\n")
    file.write("RMSprop is also adaptive and commonly works well for sequence-based tasks.\n")

print("\nFiles saved:")
print("optimizer_comparison_results.csv")
print("optimizer_accuracy_comparison.png")
print("optimizer_loss_comparison.png")
print("model_sgd.keras")
print("model_adam.keras")
print("model_rmsprop.keras")
print("optimizer_report.txt")

print("\nLab completed successfully.")
