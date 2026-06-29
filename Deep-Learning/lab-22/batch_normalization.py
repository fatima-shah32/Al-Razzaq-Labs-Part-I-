import time
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt

print("=== Lab 22: Batch Normalization in Deep Networks ===")

# Task 1: Load and preprocess MNIST dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train / 255.0
x_test = x_test / 255.0

print("\nDataset loaded successfully")
print("Training data shape:", x_train.shape)
print("Testing data shape:", x_test.shape)

# Model with Batch Normalization
def build_model_with_bn():
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dense(10, activation="softmax")
    ])

    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model

# Model without Batch Normalization
def build_model_without_bn():
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.Dense(10, activation="softmax")
    ])

    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model

model_with_bn = build_model_with_bn()
model_without_bn = build_model_without_bn()

print("\nModel with Batch Normalization Summary:")
model_with_bn.summary()

# Train model with batch normalization
print("\nTraining model WITH Batch Normalization")
start_time = time.time()

batch_norm_history = model_with_bn.fit(
    x_train,
    y_train,
    epochs=10,
    batch_size=128,
    validation_data=(x_test, y_test),
    verbose=1
)

bn_training_time = time.time() - start_time

# Train model without batch normalization
print("\nTraining model WITHOUT Batch Normalization")
start_time = time.time()

no_batch_norm_history = model_without_bn.fit(
    x_train,
    y_train,
    epochs=10,
    batch_size=128,
    validation_data=(x_test, y_test),
    verbose=1
)

no_bn_training_time = time.time() - start_time

# Evaluate both models
test_loss_bn, test_acc_bn = model_with_bn.evaluate(
    x_test,
    y_test,
    verbose=0
)

test_loss_no_bn, test_acc_no_bn = model_without_bn.evaluate(
    x_test,
    y_test,
    verbose=0
)

print("\nFinal Evaluation:")
print(f"Test accuracy with Batch Normalization: {test_acc_bn:.4f}")
print(f"Test accuracy without Batch Normalization: {test_acc_no_bn:.4f}")

# Save comparison results
comparison_df = pd.DataFrame({
    "Model": ["With Batch Normalization", "Without Batch Normalization"],
    "Test_Loss": [test_loss_bn, test_loss_no_bn],
    "Test_Accuracy": [test_acc_bn, test_acc_no_bn],
    "Training_Time_Seconds": [bn_training_time, no_bn_training_time]
})

comparison_df.to_csv("batch_normalization_comparison.csv", index=False)

# Plot validation accuracy comparison
plt.figure(figsize=(8, 5))
plt.plot(batch_norm_history.history["val_accuracy"], label="Validation Accuracy With BN")
plt.plot(no_batch_norm_history.history["val_accuracy"], label="Validation Accuracy Without BN")
plt.title("Validation Accuracy Comparison")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.tight_layout()
plt.savefig("batch_norm_accuracy_comparison.png")
plt.close()

# Plot validation loss comparison
plt.figure(figsize=(8, 5))
plt.plot(batch_norm_history.history["val_loss"], label="Validation Loss With BN")
plt.plot(no_batch_norm_history.history["val_loss"], label="Validation Loss Without BN")
plt.title("Validation Loss Comparison")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.tight_layout()
plt.savefig("batch_norm_loss_comparison.png")
plt.close()

# Save models
model_with_bn.save("model_with_batch_normalization.keras")
model_without_bn.save("model_without_batch_normalization.keras")

# Save report
with open("batch_normalization_report.txt", "w") as file:
    file.write("Lab 22: Batch Normalization in Deep Networks\n\n")
    file.write("Dataset: MNIST\n")
    file.write("Model Type: Feedforward Neural Network\n\n")

    file.write("Comparison Results:\n")
    file.write(f"Accuracy with Batch Normalization: {test_acc_bn:.4f}\n")
    file.write(f"Accuracy without Batch Normalization: {test_acc_no_bn:.4f}\n")
    file.write(f"Training Time with Batch Normalization: {bn_training_time:.2f} seconds\n")
    file.write(f"Training Time without Batch Normalization: {no_bn_training_time:.2f} seconds\n\n")

    file.write("Observation:\n")
    file.write("Batch Normalization stabilizes training by normalizing layer activations.\n")
    file.write("It can improve convergence speed and help the model generalize better.\n")
    file.write("Performance may vary depending on dataset, architecture, and training settings.\n")

print("\nFiles saved:")
print("batch_normalization_comparison.csv")
print("batch_norm_accuracy_comparison.png")
print("batch_norm_loss_comparison.png")
print("model_with_batch_normalization.keras")
print("model_without_batch_normalization.keras")
print("batch_normalization_report.txt")

print("\nLab completed successfully.")
