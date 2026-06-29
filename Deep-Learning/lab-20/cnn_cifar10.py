import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.datasets import cifar10

print("=== Lab 20: CNN for Basic Image Classification ===")

# Task 1: Load CIFAR-10 dataset
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

print("\nDataset loaded successfully")
print("Training images shape:", x_train.shape)
print("Testing images shape:", x_test.shape)

# CIFAR-10 class names
class_names = [
    "airplane",
    "automobile",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck"
]

# Task 2: Preprocess data
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

y_train_cat = tf.keras.utils.to_categorical(y_train, 10)
y_test_cat = tf.keras.utils.to_categorical(y_test, 10)

print("\nData normalized and labels one-hot encoded")

# Task 3: Build CNN model
model = Sequential([
    Conv2D(
        32,
        (3, 3),
        activation="relu",
        input_shape=(32, 32, 3)
    ),
    MaxPooling2D((2, 2)),

    Conv2D(
        64,
        (3, 3),
        activation="relu"
    ),
    MaxPooling2D((2, 2)),

    Flatten(),

    Dense(64, activation="relu"),

    Dense(10, activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

print("\nModel Summary:")
model.summary()

# Task 4: Train model
history = model.fit(
    x_train,
    y_train_cat,
    epochs=10,
    batch_size=64,
    validation_split=0.1,
    verbose=1
)

# Task 5: Evaluate model
test_loss, test_acc = model.evaluate(
    x_test,
    y_test_cat,
    verbose=0
)

print("\nTest Loss:", round(test_loss, 4))
print("Test Accuracy:", round(test_acc * 100, 2), "%")

# Save model
model.save("cnn_cifar10_model.keras")

# Save training history
history_df = pd.DataFrame(history.history)
history_df.to_csv("training_history.csv", index=False)

# Plot accuracy
plt.figure(figsize=(8, 5))
plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.title("CNN Accuracy on CIFAR-10")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.tight_layout()
plt.savefig("cifar10_accuracy_plot.png")
plt.close()

# Plot loss
plt.figure(figsize=(8, 5))
plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.title("CNN Loss on CIFAR-10")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.tight_layout()
plt.savefig("cifar10_loss_plot.png")
plt.close()

# Make sample predictions
predictions = model.predict(x_test[:10])
predicted_classes = np.argmax(predictions, axis=1)
actual_classes = y_test[:10].flatten()

prediction_df = pd.DataFrame({
    "Image_Index": list(range(10)),
    "Actual_Class": [class_names[i] for i in actual_classes],
    "Predicted_Class": [class_names[i] for i in predicted_classes]
})

prediction_df.to_csv("sample_predictions.csv", index=False)

# Visualize sample predictions
plt.figure(figsize=(12, 6))

for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(x_test[i])
    plt.title(
        f"A: {class_names[actual_classes[i]]}\nP: {class_names[predicted_classes[i]]}"
    )
    plt.axis("off")

plt.tight_layout()
plt.savefig("sample_predictions.png")
plt.close()

# Save report
with open("cnn_cifar10_report.txt", "w") as file:
    file.write("Lab 20: CNN for Basic Image Classification\n\n")
    file.write("Dataset: CIFAR-10\n")
    file.write("Classes: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck\n\n")
    file.write("Model Architecture:\n")
    file.write("Conv2D -> MaxPooling2D -> Conv2D -> MaxPooling2D -> Flatten -> Dense -> Softmax\n\n")
    file.write(f"Test Loss: {test_loss:.4f}\n")
    file.write(f"Test Accuracy: {test_acc * 100:.2f}%\n\n")
    file.write("Conclusion:\n")
    file.write("The CNN model was trained on CIFAR-10 images and evaluated using classification accuracy.\n")

print("\nFiles saved:")
print("cnn_cifar10_model.keras")
print("training_history.csv")
print("cifar10_accuracy_plot.png")
print("cifar10_loss_plot.png")
print("sample_predictions.csv")
print("sample_predictions.png")
print("cnn_cifar10_report.txt")

print("\nLab completed successfully.")
