import time
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt

from tensorflow.keras.layers import Conv2D, BatchNormalization, ReLU, Add
from tensorflow.keras.layers import Input, Dense, GlobalAveragePooling2D, MaxPooling2D
from tensorflow.keras.models import Model

print("=== Lab 32: Building a Residual Block ResNet Basic Version ===")

# Task 1: Define residual block
def residual_block(x, filters, kernel_size=3, stride=1):
    shortcut = x

    x = Conv2D(
        filters,
        kernel_size=kernel_size,
        strides=stride,
        padding="same"
    )(x)

    x = BatchNormalization()(x)
    x = ReLU()(x)

    x = Conv2D(
        filters,
        kernel_size=kernel_size,
        strides=1,
        padding="same"
    )(x)

    x = BatchNormalization()(x)

    x = Add()([x, shortcut])
    x = ReLU()(x)

    return x

# Task 2: Create ResNet model
def create_resnet(input_shape=(32, 32, 3), num_classes=10):
    inputs = Input(shape=input_shape)

    x = Conv2D(
        64,
        (3, 3),
        padding="same"
    )(inputs)

    x = BatchNormalization()(x)
    x = ReLU()(x)

    x = residual_block(x, 64)
    x = residual_block(x, 64)

    x = GlobalAveragePooling2D()(x)

    outputs = Dense(
        num_classes,
        activation="softmax"
    )(x)

    model = Model(
        inputs,
        outputs,
        name="Basic_ResNet"
    )

    return model

# Standard CNN for comparison
def create_standard_cnn(input_shape=(32, 32, 3), num_classes=10):
    inputs = Input(shape=input_shape)

    x = Conv2D(
        64,
        (3, 3),
        padding="same",
        activation="relu"
    )(inputs)

    x = BatchNormalization()(x)

    x = Conv2D(
        64,
        (3, 3),
        padding="same",
        activation="relu"
    )(x)

    x = BatchNormalization()(x)
    x = MaxPooling2D()(x)

    x = GlobalAveragePooling2D()(x)

    outputs = Dense(
        num_classes,
        activation="softmax"
    )(x)

    model = Model(
        inputs,
        outputs,
        name="Standard_CNN"
    )

    return model

# Task 3: Load CIFAR-10 dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

# Use smaller subset for faster lab execution
x_train = x_train[:10000]
y_train = y_train[:10000]
x_test = x_test[:2000]
y_test = y_test[:2000]

x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

print("\nDataset loaded successfully")
print("Training data shape:", x_train.shape)
print("Testing data shape:", x_test.shape)

# Create models
resnet_model = create_resnet()
cnn_model = create_standard_cnn()

print("\nResNet Model Summary:")
resnet_model.summary()

print("\nStandard CNN Model Summary:")
cnn_model.summary()

# Compile models
resnet_model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

cnn_model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# Train ResNet
print("\nTraining Basic ResNet model")
start_time = time.time()

resnet_history = resnet_model.fit(
    x_train,
    y_train,
    epochs=5,
    batch_size=64,
    validation_data=(x_test, y_test),
    verbose=1
)

resnet_time = time.time() - start_time

# Train Standard CNN
print("\nTraining Standard CNN model")
start_time = time.time()

cnn_history = cnn_model.fit(
    x_train,
    y_train,
    epochs=5,
    batch_size=64,
    validation_data=(x_test, y_test),
    verbose=1
)

cnn_time = time.time() - start_time

# Evaluate models
resnet_loss, resnet_acc = resnet_model.evaluate(
    x_test,
    y_test,
    verbose=0
)

cnn_loss, cnn_acc = cnn_model.evaluate(
    x_test,
    y_test,
    verbose=0
)

print("\nFinal Evaluation:")
print(f"ResNet Accuracy: {resnet_acc:.4f}")
print(f"Standard CNN Accuracy: {cnn_acc:.4f}")

# Save comparison results
comparison_df = pd.DataFrame({
    "Model": ["Basic ResNet", "Standard CNN"],
    "Test_Loss": [resnet_loss, cnn_loss],
    "Test_Accuracy": [resnet_acc, cnn_acc],
    "Training_Time_Seconds": [resnet_time, cnn_time]
})

comparison_df.to_csv("resnet_cnn_comparison.csv", index=False)

# Plot validation accuracy comparison
plt.figure(figsize=(8, 5))
plt.plot(resnet_history.history["val_accuracy"], label="ResNet Val Accuracy")
plt.plot(cnn_history.history["val_accuracy"], label="CNN Val Accuracy")
plt.title("Validation Accuracy: ResNet vs CNN")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.tight_layout()
plt.savefig("resnet_cnn_accuracy_comparison.png")
plt.close()

# Plot validation loss comparison
plt.figure(figsize=(8, 5))
plt.plot(resnet_history.history["val_loss"], label="ResNet Val Loss")
plt.plot(cnn_history.history["val_loss"], label="CNN Val Loss")
plt.title("Validation Loss: ResNet vs CNN")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.tight_layout()
plt.savefig("resnet_cnn_loss_comparison.png")
plt.close()

# Save models
resnet_model.save("basic_resnet_model.keras")
cnn_model.save("standard_cnn_model.keras")

# Save report
with open("resnet_report.txt", "w") as file:
    file.write("Lab 32: Building a Residual Block ResNet Basic Version\n\n")
    file.write("Dataset: CIFAR-10 subset\n\n")

    file.write("Residual Block:\n")
    file.write("Conv2D -> BatchNorm -> ReLU -> Conv2D -> BatchNorm -> Add Shortcut -> ReLU\n\n")

    file.write("Comparison Results:\n")
    file.write(comparison_df.to_string(index=False))
    file.write("\n\nObservation:\n")
    file.write("Residual connections help information flow through the network.\n")
    file.write("They reduce vanishing gradient problems and can improve deeper CNN training.\n")

print("\nFiles saved:")
print("resnet_cnn_comparison.csv")
print("resnet_cnn_accuracy_comparison.png")
print("resnet_cnn_loss_comparison.png")
print("basic_resnet_model.keras")
print("standard_cnn_model.keras")
print("resnet_report.txt")

print("\nLab completed successfully.")
