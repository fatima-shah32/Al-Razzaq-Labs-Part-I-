import tensorflow as tf
from tensorflow.keras import layers, models, datasets, utils
import numpy as np
import matplotlib.pyplot as plt

print("Loading MNIST Dataset...")

# Load Dataset
(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()

# Normalize
train_images = train_images.astype("float32") / 255.0
test_images = test_images.astype("float32") / 255.0

# Add channel dimension
train_images = np.expand_dims(train_images, -1)
test_images = np.expand_dims(test_images, -1)

# One-hot encoding
train_labels_cat = utils.to_categorical(train_labels, 10)
test_labels_cat = utils.to_categorical(test_labels, 10)

print("Training Images:", train_images.shape)
print("Testing Images:", test_images.shape)


# Simplified Capsule Layer
class CapsuleLayer(layers.Layer):
    def __init__(self, num_capsules, dim_capsules, **kwargs):
        super(CapsuleLayer, self).__init__(**kwargs)
        self.num_capsules = num_capsules
        self.dim_capsules = dim_capsules

    def build(self, input_shape):
        self.flatten = layers.Flatten()
        self.dense = layers.Dense(
            self.num_capsules * self.dim_capsules,
            activation='relu'
        )

    def call(self, inputs):
        x = self.flatten(inputs)
        x = self.dense(x)
        return tf.reshape(
            x,
            (-1, self.num_capsules, self.dim_capsules)
        )


# Build CapsNet
def create_capsnet(input_shape):

    inputs = layers.Input(shape=input_shape)

    x = layers.Conv2D(
        64,
        (3,3),
        activation='relu'
    )(inputs)

    x = layers.MaxPooling2D((2,2))(x)

    x = layers.Conv2D(
        128,
        (3,3),
        activation='relu'
    )(x)

    capsule = CapsuleLayer(
        num_capsules=10,
        dim_capsules=16
    )(x)

    x = layers.Flatten()(capsule)

    outputs = layers.Dense(
        10,
        activation='softmax'
    )(x)

    model = models.Model(inputs, outputs)

    return model


capsnet = create_capsnet((28,28,1))

capsnet.summary()

# Compile
capsnet.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Train
history = capsnet.fit(
    train_images,
    train_labels_cat,
    epochs=5,
    batch_size=128,
    validation_split=0.2
)

# Evaluate
test_loss, test_accuracy = capsnet.evaluate(
    test_images,
    test_labels_cat
)

print("\nTest Accuracy:", test_accuracy)

# Save Model
capsnet.save("capsnet_mnist.keras")

print("Model Saved Successfully")

# Accuracy Plot
plt.figure(figsize=(8,5))
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title("CapsNet Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend(["Train","Validation"])
plt.savefig("accuracy_plot.png")
plt.show()

# Loss Plot
plt.figure(figsize=(8,5))
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title("CapsNet Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend(["Train","Validation"])
plt.savefig("loss_plot.png")
plt.show()

# Predictions
predictions = capsnet.predict(test_images[:5])

fig, axes = plt.subplots(1,5, figsize=(15,3))

for i in range(5):
    axes[i].imshow(test_images[i].squeeze(), cmap="gray")

    true_label = test_labels[i]
    pred_label = np.argmax(predictions[i])

    axes[i].set_title(
        f"T:{true_label}\nP:{pred_label}"
    )

    axes[i].axis("off")

plt.savefig("sample_predictions.png")
plt.show()

# Report
with open("project_report.txt","w") as f:

    f.write("Lab 39 - Simple Capsule Network\n\n")
    f.write("Dataset: MNIST\n")
    f.write(f"Test Accuracy: {test_accuracy:.4f}\n")
    f.write("\nArchitecture:\n")
    f.write("Conv2D -> MaxPool -> Conv2D -> CapsuleLayer -> Dense\n")

print("Report Generated")
