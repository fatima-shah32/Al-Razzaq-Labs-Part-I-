# Lab 14: Building a Simple Autoencoder

## Objective

Build and train a simple autoencoder using Keras for image compression and reconstruction.

## Tools Used

- Python
- TensorFlow/Keras
- NumPy
- Matplotlib

## Dataset

MNIST handwritten digit dataset.

## Tasks Performed

1. Loaded MNIST dataset
2. Normalized image pixel values
3. Flattened images into vectors
4. Built an encoder and decoder network
5. Trained the autoencoder
6. Reconstructed test images
7. Compared original and reconstructed images
8. Saved model, plots, and report

## Files

```text
simple_autoencoder.py
simple_autoencoder.keras
autoencoder_loss.png
original_vs_reconstructed.png
autoencoder_report.txt
README.md

Conclusion

This lab demonstrated how an autoencoder compresses data into a smaller latent representation and reconstructs it. The original and reconstructed MNIST images show how well the model learned image patterns
