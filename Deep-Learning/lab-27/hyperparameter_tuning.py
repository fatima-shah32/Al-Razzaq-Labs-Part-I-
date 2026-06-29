import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

from tensorflow.keras.datasets import mnist

print("=== Lab 27: Hyperparameter Tuning in Deep Learning ===")

# Reproducibility
np.random.seed(42)
tf.random.set_seed(42)

# Task 1: Define hyperparameter grid
learning_rates = [0.001, 0.01, 0.1]
batch_sizes = [16, 32, 64]

parameter_grid = [
    (lr, bs)
    for lr in learning_rates
    for bs in batch_sizes
]

print("\nHyperparameter Grid:")
for lr, bs in parameter_grid:
    print(f"Learning Rate: {lr}, Batch Size: {bs}")

# Load MNIST dataset once
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Use smaller subset for faster lab execution
x_train = x_train[:10000]
y_train = y_train[:10000]
x_test = x_test[:2000]
y_test = y_test[:2000]

# Normalize data
x_train = x_train / 255.0
x_test = x_test / 255.0

print("\nDataset loaded and preprocessed successfully")
print("Training data shape:", x_train.shape)
print("Testing data shape:", x_test.shape)

# Model training function
def train_model(learning_rate, batch_size):
    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dense(10, activation="softmax")
    ])

    model.compile(
        optimizer=tf.keras.optimizers.Adam(
            learning_rate=learning_rate
        ),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )

    start_time = time.time()

    history = model.fit(
        x_train,
        y_train,
        epochs=5,
        batch_size=batch_size,
        validation_split=0.1,
        verbose=1
    )

    training_time = time.time() - start_time

    test_loss, test_accuracy = model.evaluate(
        x_test,
        y_test,
        verbose=0
    )

    return model, history, test_loss, test_accuracy, training_time

# Task 2: Train models with all combinations
results = []
histories = {}

for learning_rate, batch_size in parameter_grid:
    print("\n----------------------------------------")
    print(f"Training with LR={learning_rate}, Batch Size={batch_size}")
    print("----------------------------------------")

    model, history, test_loss, test_accuracy, training_time = train_model(
        learning_rate,
        batch_size
    )

    run_name = f"lr_{learning_rate}_bs_{batch_size}"

    histories[run_name] = history

    results.append({
        "Learning_Rate": learning_rate,
        "Batch_Size": batch_size,
        "Test_Loss": test_loss,
        "Test_Accuracy": test_accuracy,
        "Training_Time_Seconds": training_time,
        "Final_Validation_Accuracy": history.history["val_accuracy"][-1],
        "Final_Validation_Loss": history.history["val_loss"][-1]
    })

    model.save(f"model_{run_name}.keras")

# Task 3: Compare results
results_df = pd.DataFrame(results)
results_df.to_csv("hyperparameter_tuning_results.csv", index=False)

best_result = results_df.sort_values(
    by="Test_Accuracy",
    ascending=False
).iloc[0]

print("\nBest Result:")
print(best_result)

# Plot test accuracy comparison
plt.figure(figsize=(10, 6))

labels = [
    f"lr={row.Learning_Rate}\nbs={int(row.Batch_Size)}"
    for row in results_df.itertuples()
]

plt.bar(labels, results_df["Test_Accuracy"])
plt.title("Test Accuracy for Hyperparameter Combinations")
plt.xlabel("Hyperparameter Combination")
plt.ylabel("Test Accuracy")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("hyperparameter_accuracy_comparison.png")
plt.close()

# Plot validation accuracy curves
plt.figure(figsize=(10, 6))

for run_name, history in histories.items():
    plt.plot(
        history.history["val_accuracy"],
        label=run_name
    )

plt.title("Validation Accuracy Curves")
plt.xlabel("Epoch")
plt.ylabel("Validation Accuracy")
plt.legend(fontsize=7)
plt.tight_layout()
plt.savefig("validation_accuracy_curves.png")
plt.close()

# Save report
with open("hyperparameter_tuning_report.txt", "w") as file:
    file.write("Lab 27: Hyperparameter Tuning in Deep Learning\n\n")
    file.write("Dataset: MNIST subset\n")
    file.write("Hyperparameters Tuned:\n")
    file.write("- Learning Rate: 0.001, 0.01, 0.1\n")
    file.write("- Batch Size: 16, 32, 64\n\n")

    file.write("Results:\n")
    file.write(results_df.to_string(index=False))
    file.write("\n\nBest Result:\n")
    file.write(best_result.to_string())
    file.write("\n\nObservation:\n")
    file.write("Learning rate controls update size during training.\n")
    file.write("Batch size controls how many samples are used per weight update.\n")
    file.write("Very high learning rates can reduce stability, while moderate values often work better.\n")

print("\nFiles saved:")
print("hyperparameter_tuning_results.csv")
print("hyperparameter_accuracy_comparison.png")
print("validation_accuracy_curves.png")
print("hyperparameter_tuning_report.txt")
print("model_lr_*_bs_*.keras")

print("\nLab completed successfully.")
