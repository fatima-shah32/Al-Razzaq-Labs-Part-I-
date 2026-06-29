# Lab 25: Introduction to Generative Adversarial Networks

## Objective

Understand and implement a simple Generative Adversarial Network using TensorFlow/Keras.

## Tools Used

- Python
- TensorFlow/Keras
- NumPy
- Pandas
- Matplotlib

## Dataset

MNIST handwritten digit dataset.

## GAN Components

### Generator

Creates fake handwritten digit images from random noise.

### Discriminator

Classifies images as real or fake.

## Tasks Performed

1. Loaded and preprocessed MNIST dataset
2. Built generator network
3. Built discriminator network
4. Combined both networks into a GAN
5. Trained discriminator and generator alternately
6. Generated synthetic digit images
7. Saved models, generated images, loss plot, history, and report

## Files

```text
simple_gan_mnist.py
gan_generator.keras
gan_discriminator.keras
gan_combined_model.keras
gan_training_history.csv
gan_loss_plot.png
generated_epoch_100.png
generated_epoch_200.png
generated_epoch_300.png
generated_epoch_400.png
generated_epoch_500.png
generated_epoch_600.png
generated_epoch_700.png
generated_epoch_800.png
generated_epoch_900.png
generated_epoch_1000.png
generated_epoch_final.png
gan_report.txt
README.md

Conclusion

This lab introduced GANs by creating a generator and discriminator. The generator learned to create digit-like images, while the discriminator learned to identify real and fake samples.
