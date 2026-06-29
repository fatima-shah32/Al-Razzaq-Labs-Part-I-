# Lab 26: Building a Variational Autoencoder

## Objective

Build and train a Variational Autoencoder using TensorFlow/Keras and generate new MNIST-style digit images.

## Tools Used

- Python
- TensorFlow/Keras
- NumPy
- Pandas
- Matplotlib

## Dataset

MNIST handwritten digit dataset.

## Key Concepts

- Encoder network
- Decoder network
- Latent space
- Reparameterization trick
- Reconstruction loss
- KL divergence

## Tasks Performed

1. Loaded and preprocessed MNIST dataset
2. Built encoder network
3. Built decoder network
4. Created VAE model
5. Added VAE custom loss
6. Trained the VAE
7. Sampled new points from latent space
8. Generated new digit-like images
9. Saved models, plots, history, and report

## Files

```text
variational_autoencoder.py
vae_model.keras
vae_encoder.keras
vae_decoder.keras
vae_generated_digits.png
vae_training_loss.png
vae_training_history.csv
vae_report.txt
README.md

Conclusion

This lab demonstrated how a Variational Autoencoder compresses MNIST images into a latent space and generates new digit-like samples from that learned space.
