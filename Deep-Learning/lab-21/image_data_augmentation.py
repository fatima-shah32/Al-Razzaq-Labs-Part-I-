import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

print("=== Lab 21: Data Augmentation for Images ===")

# Task 1: Load CIFAR-10 dataset
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Use a smaller dataset for faster lab execution
x_train = x_train[:5000]
y_train = y_train[:5000]
x_test = x_test[:1000]
y_test = y_test[:1000]

# Normalize images
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

print("\nDataset loaded successfully")
print("Training data shape:", x_train.shape)
print("Testing data shape:", x_test.shape)

# CIFAR-10 class names
class_names = [
    "airplane", "automobile", "bird", "cat", "deer",
    "dog", "frog", "horse", "ship", "truck"
]

# Task 1: Apply rotations, flips, and shifts
augmentation_datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
    fill_mode="nearest"
)

sample_image = x_train[0]
sample_label = class_names[int(y_train[0][0])]

aug_iter = augmentation_datagen.flow(
    np.expand_dims(sample_image, axis=0),
    batch_size=1
)

augmented_images = [
    next(aug_iter)[0]
    for _ in range(5)
]

# Visualize original and augmented images
plt.figure(figsize=(15, 4))

plt.subplot(1, 6, 1)
plt.imshow(sample_image)
plt.title(f"Original\n{sample_label}")
plt.axis("off")

for i, aug_img in enumerate(augmented_images):
    plt.subplot(1, 6, i + 2)
    plt.imshow(aug_img)
    plt.title(f"Aug {i + 1}")
    plt.axis("off")

plt.tight_layout()
plt.savefig("augmented_images.png")
plt.close()

print("\nAugmented image examples saved as augmented_images.png")

# Task 2: Generate augmented data batches
train_data_aug = augmentation_datagen.flow(
    x_train,
    y_train,
    batch_size=64
)

print("Augmented data batch generator created successfully")

# Task 3: Compare model with and without augmentation
def build_cnn_model():
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

        Dense(128, activation="relu"),

        Dense(10, activation="softmax")
    ])

    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model

# Train without augmentation
model_no_aug = build_cnn_model()

print("\nTraining model without data augmentation")
history_no_aug = model_no_aug.fit(
    x_train,
    y_train,
    epochs=5,
    batch_size=64,
    validation_data=(x_test, y_test),
    verbose=1
)

# Train with augmentation
model_aug = build_cnn_model()

print("\nTraining model with data augmentation")
history_aug = model_aug.fit(
    train_data_aug,
    epochs=5,
    validation_data=(x_test, y_test),
    verbose=1
)

# Evaluate both models
loss_no_aug, acc_no_aug = model_no_aug.evaluate(
    x_test,
    y_test,
    verbose=0
)

loss_aug, acc_aug = model_aug.evaluate(
    x_test,
    y_test,
    verbose=0
)

print("\nFinal Comparison:")
print(f"Test Accuracy Without Augmentation: {acc_no_aug:.4f}")
print(f"Test Accuracy With Augmentation: {acc_aug:.4f}")

# Save comparison results
comparison_df = pd.DataFrame({
    "Model": ["Without Augmentation", "With Augmentation"],
    "Test_Loss": [loss_no_aug, loss_aug],
    "Test_Accuracy": [acc_no_aug, acc_aug]
})

comparison_df.to_csv("augmentation_comparison_results.csv", index=False)

# Plot accuracy comparison
plt.figure(figsize=(8, 5))
plt.plot(history_no_aug.history["accuracy"], label="Train No Aug")
plt.plot(history_no_aug.history["val_accuracy"], label="Val No Aug")
plt.plot(history_aug.history["accuracy"], label="Train Aug")
plt.plot(history_aug.history["val_accuracy"], label="Val Aug")
plt.title("Accuracy With vs Without Augmentation")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.tight_layout()
plt.savefig("augmentation_accuracy_comparison.png")
plt.close()

# Plot loss comparison
plt.figure(figsize=(8, 5))
plt.plot(history_no_aug.history["loss"], label="Train No Aug")
plt.plot(history_no_aug.history["val_loss"], label="Val No Aug")
plt.plot(history_aug.history["loss"], label="Train Aug")
plt.plot(history_aug.history["val_loss"], label="Val Aug")
plt.title("Loss With vs Without Augmentation")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.tight_layout()
plt.savefig("augmentation_loss_comparison.png")
plt.close()

# Save models
model_no_aug.save("cnn_without_augmentation.keras")
model_aug.save("cnn_with_augmentation.keras")

# Save report
with open("augmentation_report.txt", "w") as file:
    file.write("Lab 21: Data Augmentation for Images\n\n")
    file.write("Dataset: CIFAR-10 subset\n")
    file.write("Augmentation Techniques:\n")
    file.write("- Rotation\n")
    file.write("- Width shift\n")
    file.write("- Height shift\n")
    file.write("- Horizontal flip\n\n")

    file.write("Model Comparison:\n")
    file.write(f"Without Augmentation Accuracy: {acc_no_aug:.4f}\n")
    file.write(f"With Augmentation Accuracy: {acc_aug:.4f}\n\n")

    file.write("Observation:\n")
    file.write("Data augmentation creates transformed versions of images during training.\n")
    file.write("It helps improve generalization and reduces overfitting by increasing data variety.\n")

print("\nFiles saved:")
print("augmented_images.png")
print("augmentation_comparison_results.csv")
print("augmentation_accuracy_comparison.png")
print("augmentation_loss_comparison.png")
print("cnn_without_augmentation.keras")
print("cnn_with_augmentation.keras")
print("augmentation_report.txt")

print("\nLab completed successfully.")
