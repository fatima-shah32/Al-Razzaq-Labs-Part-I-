import numpy as np
import matplotlib.pyplot as plt

from PIL import Image, ImageDraw, ImageOps
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


print("=== Lab 32: Data Augmentation Concept ===")

# Task 1: Understanding Data Augmentation
print("\nData augmentation creates modified versions of existing data.")
print("It helps reduce overfitting and improves model generalization.")

# Task 2: Create sample image
image = Image.new("RGB", (250, 250), color="lightblue")
draw = ImageDraw.Draw(image)
draw.rectangle((70, 70, 180, 180), fill="orange")
draw.text((75, 115), "Sample", fill="black")

image.save("sample_image.jpg")

print("\nSample image saved as sample_image.jpg")

# Load sample image
img = Image.open("sample_image.jpg")

# Apply rotation
rotated_img = img.rotate(40)
rotated_img.save("rotated_image.jpg")

# Apply horizontal flip
flipped_img = ImageOps.mirror(img)
flipped_img.save("flipped_image.jpg")

# Apply vertical flip
vertical_flipped_img = ImageOps.flip(img)
vertical_flipped_img.save("vertical_flipped_image.jpg")

print("Rotated image saved as rotated_image.jpg")
print("Flipped image saved as flipped_image.jpg")
print("Vertical flipped image saved as vertical_flipped_image.jpg")

# Display augmentation examples in one plot
fig, axes = plt.subplots(1, 4, figsize=(12, 4))

images = [
    img,
    rotated_img,
    flipped_img,
    vertical_flipped_img
]

titles = [
    "Original",
    "Rotated",
    "Horizontal Flip",
    "Vertical Flip"
]

for ax, image_item, title in zip(axes, images, titles):
    ax.imshow(image_item)
    ax.set_title(title)
    ax.axis("off")

plt.tight_layout()
plt.savefig("augmentation_examples.png")
plt.close()

print("Augmentation examples saved as augmentation_examples.png")

# Task 3: Model Performance Comparison
print("\nModel Performance Comparison")

# Load digits dataset
digits = load_digits()

X = digits.data
y = digits.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

# Train model without augmentation
model_original = LogisticRegression(max_iter=2000)
model_original.fit(X_train, y_train)

pred_original = model_original.predict(X_test)

accuracy_original = accuracy_score(y_test, pred_original)

print("\nAccuracy without augmentation:", round(accuracy_original, 4))

# Simple augmentation for tabular image data
# Add small random noise to create extra training samples
np.random.seed(42)

noise = np.random.normal(
    loc=0,
    scale=0.2,
    size=X_train.shape
)

X_train_augmented = X_train + noise
y_train_augmented = y_train.copy()

# Combine original and augmented data
X_combined = np.vstack((X_train, X_train_augmented))
y_combined = np.hstack((y_train, y_train_augmented))

# Train model with augmented data
model_augmented = LogisticRegression(max_iter=2000)
model_augmented.fit(X_combined, y_combined)

pred_augmented = model_augmented.predict(X_test)

accuracy_augmented = accuracy_score(y_test, pred_augmented)

print("Accuracy with augmentation:", round(accuracy_augmented, 4))

# Save performance comparison
with open("performance_comparison.txt", "w") as file:
    file.write("Lab 32: Data Augmentation Concept\n\n")
    file.write(f"Accuracy without augmentation: {round(accuracy_original, 4)}\n")
    file.write(f"Accuracy with augmentation: {round(accuracy_augmented, 4)}\n")
    file.write("\nData augmentation helps increase dataset diversity and reduce overfitting.")

print("\nPerformance comparison saved as performance_comparison.txt")

print("\nLab completed successfully.")
