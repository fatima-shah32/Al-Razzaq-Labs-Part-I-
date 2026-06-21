import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator


print("=== Lab 26: Basic Transfer Learning Concept ===")

# Create small custom image dataset
base_dir = "custom_dataset/train"
class_names = ["circle", "square"]

for class_name in class_names:
    os.makedirs(os.path.join(base_dir, class_name), exist_ok=True)

# Generate sample images
for i in range(10):
    img = Image.new("RGB", (224, 224), color="white")
    draw = ImageDraw.Draw(img)
    draw.ellipse((60, 60, 160, 160), fill="blue")
    img.save(f"{base_dir}/circle/circle_{i}.jpg")

for i in range(10):
    img = Image.new("RGB", (224, 224), color="white")
    draw = ImageDraw.Draw(img)
    draw.rectangle((60, 60, 160, 160), fill="red")
    img.save(f"{base_dir}/square/square_{i}.jpg")

print("\nSmall custom dataset created successfully")

# Load pre-trained model
base_model = MobileNetV2(
    weights="imagenet",
    include_top=False,
    input_shape=(224, 224, 3)
)

# Freeze base model layers
for layer in base_model.layers:
    layer.trainable = False

print("Pre-trained MobileNetV2 loaded successfully")
print("Base model layers frozen")

# Add custom classification layers
model = Sequential([
    base_model,
    GlobalAveragePooling2D(),
    Dense(64, activation="relu"),
    Dense(1, activation="sigmoid")
])

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

print("\nCustom model created and compiled")

# Prepare image data
train_datagen = ImageDataGenerator(rescale=1.0 / 255)

train_generator = train_datagen.flow_from_directory(
    base_dir,
    target_size=(224, 224),
    batch_size=4,
    class_mode="binary"
)

# Train model
history = model.fit(
    train_generator,
    epochs=3,
    verbose=1
)

# Save model
model.save("transfer_learning_model.h5")

print("\nModel saved as transfer_learning_model.h5")

# Plot accuracy and loss
accuracy = history.history["accuracy"]
loss = history.history["loss"]

plt.figure(figsize=(8, 6))
plt.plot(range(1, len(accuracy) + 1), accuracy, label="Training Accuracy")
plt.plot(range(1, len(loss) + 1), loss, label="Training Loss")
plt.title("Transfer Learning Training Accuracy and Loss")
plt.xlabel("Epoch")
plt.ylabel("Value")
plt.legend()
plt.tight_layout()
plt.savefig("training_accuracy_loss.png")
plt.close()

print("Training plot saved as training_accuracy_loss.png")

# Save report
with open("transfer_learning_report.txt", "w") as file:
    file.write("Lab 26: Basic Transfer Learning Concept\n\n")
    file.write("Pre-trained Model: MobileNetV2\n")
    file.write("Dataset Classes: circle and square\n")
    file.write("Base model layers were frozen.\n")
    file.write("Custom classification layers were added.\n")
    file.write(f"Final Training Accuracy: {accuracy[-1]:.4f}\n")
    file.write(f"Final Training Loss: {loss[-1]:.4f}\n")

print("Report saved as transfer_learning_report.txt")

print("\nLab completed successfully.")
