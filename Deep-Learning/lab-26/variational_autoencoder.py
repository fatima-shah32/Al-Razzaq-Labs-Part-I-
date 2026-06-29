import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

from tensorflow.keras.layers import Input, Dense, Lambda
from tensorflow.keras.models import Model
from tensorflow.keras.losses import mse

print("=== Lab 26: Building a Variational Autoencoder ===")

# Reproducibility
np.random.seed(42)
tf.random.set_seed(42)

# Parameters
original_dim = 784
intermediate_dim_1 = 512
intermediate_dim_2 = 256
latent_dim = 2
batch_size = 128
epochs = 20

# Task 1: Sampling function using reparameterization trick
def sampling(args):
    z_mean, z_log_var = args

    batch = tf.shape(z_mean)[0]
    dim = tf.shape(z_mean)[1]

    epsilon = tf.keras.backend.random_normal(
        shape=(batch, dim)
    )

    return z_mean + tf.exp(0.5 * z_log_var) * epsilon

# Task 1: Build encoder
inputs = Input(shape=(original_dim,), name="encoder_input")

h = Dense(
    intermediate_dim_1,
    activation="relu"
)(inputs)

h = Dense(
    intermediate_dim_2,
    activation="relu"
)(h)

z_mean = Dense(
    latent_dim,
    name="z_mean"
)(h)

z_log_var = Dense(
    latent_dim,
    name="z_log_var"
)(h)

z = Lambda(
    sampling,
    output_shape=(latent_dim,),
    name="z"
)([z_mean, z_log_var])

encoder = Model(
    inputs,
    [z_mean, z_log_var, z],
    name="encoder"
)

print("\nEncoder Summary:")
encoder.summary()

# Task 1: Build decoder
latent_inputs = Input(
    shape=(latent_dim,),
    name="z_sampling"
)

x = Dense(
    intermediate_dim_2,
    activation="relu"
)(latent_inputs)

x = Dense(
    intermediate_dim_1,
    activation="relu"
)(x)

outputs = Dense(
    original_dim,
    activation="sigmoid"
)(x)

decoder = Model(
    latent_inputs,
    outputs,
    name="decoder"
)

print("\nDecoder Summary:")
decoder.summary()

# Task 1: Build VAE
vae_outputs = decoder(
    encoder(inputs)[2]
)

vae = Model(
    inputs,
    vae_outputs,
    name="vae"
)

# Task 2: Load MNIST dataset
(x_train, _), (x_test, _) = tf.keras.datasets.mnist.load_data()

x_train = np.reshape(
    x_train.astype("float32") / 255.0,
    [-1, original_dim]
)

x_test = np.reshape(
    x_test.astype("float32") / 255.0,
    [-1, original_dim]
)

print("\nMNIST dataset loaded successfully")
print("Training data shape:", x_train.shape)
print("Testing data shape:", x_test.shape)

# VAE Loss
reconstruction_loss = mse(inputs, vae_outputs)
reconstruction_loss *= original_dim

kl_loss = 1 + z_log_var - tf.square(z_mean) - tf.exp(z_log_var)
kl_loss = tf.reduce_sum(kl_loss, axis=-1)
kl_loss *= -0.5

vae_loss = tf.reduce_mean(
    reconstruction_loss + kl_loss
)

vae.add_loss(vae_loss)

vae.compile(
    optimizer="adam"
)

print("\nVAE Summary:")
vae.summary()

# Task 2: Train VAE
history = vae.fit(
    x_train,
    epochs=epochs,
    batch_size=batch_size,
    validation_data=(x_test, None),
    verbose=1
)

# Save models
vae.save("vae_model.keras")
encoder.save("vae_encoder.keras")
decoder.save("vae_decoder.keras")

# Task 3: Generate new digits from latent space
n = 15
digit_size = 28

figure = np.zeros(
    (digit_size * n, digit_size * n)
)

grid_x = np.linspace(-3, 3, n)
grid_y = np.linspace(-3, 3, n)

for i, yi in enumerate(grid_x):
    for j, xi in enumerate(grid_y):
        z_sample = np.array([[xi, yi]])

        x_decoded = decoder.predict(
            z_sample,
            verbose=0
        )

        digit = x_decoded[0].reshape(
            digit_size,
            digit_size
        )

        figure[
            i * digit_size: (i + 1) * digit_size,
            j * digit_size: (j + 1) * digit_size
        ] = digit

plt.figure(figsize=(10, 10))
plt.imshow(figure, cmap="Greys_r")
plt.axis("off")
plt.tight_layout()
plt.savefig("vae_generated_digits.png")
plt.close()

# Plot training loss
plt.figure(figsize=(8, 5))
plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.title("VAE Training Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.tight_layout()
plt.savefig("vae_training_loss.png")
plt.close()

# Save history
history_df = pd.DataFrame(history.history)
history_df.to_csv("vae_training_history.csv", index=False)

# Save report
with open("vae_report.txt", "w") as file:
    file.write("Lab 26: Building a Variational Autoencoder\n\n")
    file.write("Dataset: MNIST handwritten digits\n")
    file.write(f"Input Dimension: {original_dim}\n")
    file.write(f"Latent Dimension: {latent_dim}\n")
    file.write(f"Epochs: {epochs}\n\n")

    file.write("Architecture:\n")
    file.write("Encoder: Dense(512) -> Dense(256) -> z_mean, z_log_var, z\n")
    file.write("Decoder: Dense(256) -> Dense(512) -> Dense(784)\n\n")

    file.write("Loss Function:\n")
    file.write("VAE Loss = Reconstruction Loss + KL Divergence\n\n")

    file.write(f"Final Training Loss: {history.history['loss'][-1]:.4f}\n")
    file.write(f"Final Validation Loss: {history.history['val_loss'][-1]:.4f}\n\n")

    file.write("Conclusion:\n")
    file.write("The VAE learned a 2D latent space and generated new digit-like images from sampled latent points.\n")

print("\nFiles saved:")
print("vae_model.keras")
print("vae_encoder.keras")
print("vae_decoder.keras")
print("vae_generated_digits.png")
print("vae_training_loss.png")
print("vae_training_history.csv")
print("vae_report.txt")

print("\nLab completed successfully.")
