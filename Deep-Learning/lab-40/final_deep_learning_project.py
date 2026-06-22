import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import cifar10

print("Loading CIFAR-10 Dataset...")

# Load Dataset
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Normalize Images
x_train = x_train / 255.0
x_test = x_test / 255.0

print("Training Samples:", len(x_train))
print("Testing Samples:", len(x_test))

# CNN Model
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(
        32, (3,3),
        activation='relu',
        input_shape=(32,32,3)
    ),
    tf.keras.layers.MaxPooling2D((2,2)),

    tf.keras.layers.Conv2D(64,(3,3),activation='relu'),
    tf.keras.layers.MaxPooling2D((2,2)),

    tf.keras.layers.Flatten(),

    tf.keras.layers.Dense(64,activation='relu'),

    tf.keras.layers.Dense(10,activation='softmax')
])

# Compile Model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

print("\nTraining Model...\n")

history = model.fit(
    x_train,
    y_train,
    epochs=10,
    validation_data=(x_test, y_test)
)

# Evaluate
test_loss, test_acc = model.evaluate(x_test, y_test)

print("\nTest Accuracy:", test_acc)

# Save Model
model.save("cifar10_cnn_model.keras")

print("Model Saved Successfully")

# Accuracy Plot
plt.figure(figsize=(8,5))

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])

plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')

plt.legend(['Train','Validation'])

plt.savefig('accuracy_plot.png')

plt.show()

# Loss Plot
plt.figure(figsize=(8,5))

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])

plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')

plt.legend(['Train','Validation'])

plt.savefig('loss_plot.png')

plt.show()

# Create Report
with open("project_report.txt", "w") as report:
    report.write("Lab 40: Final Deep Learning Project\n\n")
    report.write("Dataset: CIFAR-10\n")
    report.write("Problem Type: Image Classification\n")
    report.write(f"Test Accuracy: {test_acc:.4f}\n")
    report.write("\nModel Architecture:\n")
    report.write("Conv2D -> MaxPool -> Conv2D -> MaxPool -> Flatten -> Dense -> Output\n")

print("Project Report Generated")
