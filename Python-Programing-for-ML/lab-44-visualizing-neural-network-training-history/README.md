# Lab 44: Visualizing Neural Network Training History

## Objective

Learn how to visualize and interpret the training history of a neural network using TensorFlow/Keras and Matplotlib.

---

## Task 1: Capture Training History

### Import Libraries

```python
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
Load Dataset
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
Normalize Data
train_images = train_images / 255.0
test_images = test_images / 255.0
Build Model
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dense(10, activation="softmax")
])
Compile Model
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)
Train Model
history = model.fit(
    train_images,
    train_labels,
    epochs=10,
    validation_split=0.2
)
Task 2: Plot Loss and Accuracy
Extract History
history_dict = history.history

acc = history_dict["accuracy"]
val_acc = history_dict["val_accuracy"]
loss = history_dict["loss"]
val_loss = history_dict["val_loss"]
Plot Loss
plt.plot(epochs, loss, label="Training Loss")
plt.plot(epochs, val_loss, label="Validation Loss")
plt.legend()
plt.savefig("training_validation_loss.png")
Plot Accuracy
plt.plot(epochs, acc, label="Training Accuracy")
plt.plot(epochs, val_acc, label="Validation Accuracy")
plt.legend()
plt.savefig("training_validation_accuracy.png")
Task 3: Analyze Convergence Trends
Loss Curve
If training loss decreases but validation loss increases, the model may be overfitting.
If both losses remain high, the model may be underfitting.
Accuracy Curve
If training and validation accuracy rise together, the model is learning well.
If training accuracy is much higher than validation accuracy, overfitting may be present.
Summary
Concept	Purpose
Training Loss	Measures model error on training data
Validation Loss	Measures model error on unseen validation data
Training Accuracy	Accuracy on training data
Validation Accuracy	Accuracy on validation data
Matplotlib	Used to visualize training curves
Conclusion

In this lab, I learned how to capture neural network training history and visualize loss and accuracy over epochs. These plots help identify overfitting, underfitting, and model stability.
