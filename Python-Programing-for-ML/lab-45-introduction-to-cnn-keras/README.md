# Lab 45: Introduction to Convolutional Neural Networks using Keras

## Objective

Understand CNN basics and build, train, and evaluate a simple CNN model using Keras on the MNIST dataset.

---

## Key Concepts

### Convolutional Layer
Extracts image features such as edges, shapes, and patterns.

### Pooling Layer
Reduces feature map size and helps reduce computation.

### Fully Connected Layer
Uses extracted features to perform final classification.

---

## Task 1: Import Libraries

```python
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
