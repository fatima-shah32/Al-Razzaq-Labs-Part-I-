import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.datasets import mnist

print("=== Lab 14: Building a Simple Autoencoder ===")

# Task 1: Load and preprocess MNIST dataset
(x_train, _), (x_test, _) = mnist.load_data()

x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))

print("\nTraining data shape:", x_train.shape)
print("Testing data shape:", x_test.shape)

# Task 2: Define autoencoder architecture
input_dim = x_train.shape[1]
encoding_dim = 32

input_img = Input(shape=(input_dim,))

encoded = Dense(
    encoding_dim,
    activation="relu"
)(input_img)

decoded = Dense(
    input_dim,
    activation="sigmoid"
)(encoded)

autoencoder = Model(input_img, decoded)

autoencoder.compile(
    optimizer="adam",
    loss="binary_crossentropy"
)

print("\nAutoencoder Summary:")
autoencoder.summary()

# Train autoencoder
history = autoencoder.fit(
    x_train,
    x_train,
    epochs=10,
    batch_size=256,
    shuffle=True,
    validation_data=(x_test, x_test),
    verbose=1
)

# Task 3: Reconstruct test images
decoded_imgs = autoencoder.predict(x_test)

# Save model
autoencoder.save("simple_autoencoder.keras")

# Plot training loss
plt.figure(figsize=(8, 5))
plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.title("Autoencoder Training Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.tight_layout()
plt.savefig("autoencoder_loss.png")
plt.close()

# Visualize original vs reconstructed images
n = 10
plt.figure(figsize=(20, 4))

for i in range(n):
    # Original image
    ax = plt.subplot(2, n, i + 1)
    plt.imshow(x_test[i].reshape(28, 28), cmap="gray")
    ax.set_title("Original")
    ax.axis("off")

    # Reconstructed image
    ax = plt.subplot(2, n, i + 1 + n)
    plt.imshow(decoded_imgs[i].reshape(28, 28), cmap="gray")
    ax.set_title("Reconstructed")
    ax.axis("off")

plt.tight_layout()
plt.savefig("original_vs_reconstructed.png")
plt.close()

# Save report
with open("autoencoder_report.txt", "w") as file:
    file.write("Lab 14: Building a Simple Autoencoder\n\n")
    file.write("Dataset: MNIST\n")
    file.write("Input Dimension: 784\n")
    file.write("Encoding Dimension: 32\n")
    file.write("Architecture: Input -> Dense Encoder -> Dense Decoder\n\n")
    file.write(f"Final Training Loss: {history.history['loss'][-1]:.4f}\n")
    file.write(f"Final Validation Loss: {history.history['val_loss'][-1]:.4f}\n\n")
    file.write("Conclusion:\n")
    file.write("The autoencoder learned to compress MNIST images into a smaller representation and reconstruct them.\n")

print("\nFiles saved:")
print("simple_autoencoder.keras")
print("autoencoder_loss.png")
print("original_vs_reconstructed.png")
print("autoencoder_report.txt")

print("\nLab completed successfully.")
