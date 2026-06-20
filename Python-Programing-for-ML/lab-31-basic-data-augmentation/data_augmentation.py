from PIL import Image, ImageDraw
import nltk

from nltk.corpus import wordnet
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score


print("=== Task 1: Introduction to Data Augmentation ===")
print("Data augmentation means creating new training samples from existing data.")
print("It helps improve model generalization and reduce overfitting.")


print("\n=== Task 2: Image Augmentation ===")

# Create a sample image
image = Image.new("RGB", (300, 200), color="lightblue")
draw = ImageDraw.Draw(image)
draw.text((90, 90), "Sample Image", fill="black")

image.save("sample_image.jpg")
print("Original image saved: sample_image.jpg")

# Load image
image = Image.open("sample_image.jpg")

# Rotate image
rotated_image = image.rotate(90)
rotated_image.save("rotated_image.jpg")
print("Rotated image saved: rotated_image.jpg")

# Flip image
flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
flipped_image.save("flipped_image.jpg")
print("Flipped image saved: flipped_image.jpg")


print("\n=== Task 3: Text Augmentation ===")

nltk.download("wordnet")
nltk.download("omw-1.4")

text = "Data augmentation is a technique to expand dataset diversity."


def synonym_replacement(sentence, n):
    words = sentence.split()
    new_words = words.copy()
    replaced_count = 0

    for index, word in enumerate(words):
        clean_word = word.strip(".,!?")
        synonyms = wordnet.synsets(clean_word)

        if synonyms:
            synonym = synonyms[0].lemmas()[0].name()
            synonym = synonym.replace("_", " ")

            if synonym.lower() != clean_word.lower():
                new_words[index] = synonym
                replaced_count += 1

        if replaced_count == n:
            break

    return " ".join(new_words)


augmented_text = synonym_replacement(text, 2)

print("Original Text:", text)
print("Augmented Text:", augmented_text)


print("\n=== Task 4: Model Training and Evaluation ===")

# Original small dataset
original_texts = [
    "This product is good",
    "I like this item",
    "This is a great experience",
    "This product is bad",
    "I dislike this item",
    "This is a poor experience"
]

labels = [1, 1, 1, 0, 0, 0]

# Create augmented text data
augmented_texts = [
    synonym_replacement(sentence, 1)
    for sentence in original_texts
]

combined_texts = original_texts + augmented_texts
combined_labels = labels + labels

# Train model on original data
vectorizer_original = CountVectorizer()
X_original = vectorizer_original.fit_transform(original_texts)

model_original = LogisticRegression()
model_original.fit(X_original, labels)

pred_original = model_original.predict(X_original)

# Train model on augmented data
vectorizer_augmented = CountVectorizer()
X_augmented = vectorizer_augmented.fit_transform(combined_texts)

model_augmented = LogisticRegression()
model_augmented.fit(X_augmented, combined_labels)

pred_augmented = model_augmented.predict(X_augmented)

# Evaluate original model
original_accuracy = accuracy_score(labels, pred_original)
original_precision = precision_score(labels, pred_original)
original_recall = recall_score(labels, pred_original)

# Evaluate augmented model
augmented_accuracy = accuracy_score(combined_labels, pred_augmented)
augmented_precision = precision_score(combined_labels, pred_augmented)
augmented_recall = recall_score(combined_labels, pred_augmented)

print("\nOriginal Data Model Performance:")
print("Accuracy:", round(original_accuracy, 2))
print("Precision:", round(original_precision, 2))
print("Recall:", round(original_recall, 2))

print("\nAugmented Data Model Performance:")
print("Accuracy:", round(augmented_accuracy, 2))
print("Precision:", round(augmented_precision, 2))
print("Recall:", round(augmented_recall, 2))

print("\nCreated Files:")
print("sample_image.jpg")
print("rotated_image.jpg")
print("flipped_image.jpg")
