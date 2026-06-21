import re
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


print("=== Lab 28: Sentiment Analysis Concept ===")

# Task 1: Prepare labeled text dataset
data = {
    "review": [
        "This movie was amazing and I loved it",
        "The story was excellent and very emotional",
        "I enjoyed the acting and the music",
        "This film was boring and too long",
        "I hated the movie and the acting was bad",
        "The plot was weak and disappointing",
        "Fantastic movie with great characters",
        "Terrible experience and waste of time",
        "The movie was beautiful and inspiring",
        "Bad story and poor direction"
    ],
    "sentiment": [
        "positive",
        "positive",
        "positive",
        "negative",
        "negative",
        "negative",
        "positive",
        "negative",
        "positive",
        "negative"
    ]
}

df = pd.DataFrame(data)

df.to_csv("sentiment_dataset.csv", index=False)

print("\nDataset Preview:")
print(df.head())

# Clean text
def clean_text(text):
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"[^\w\s]", "", text)
    text = text.lower()
    return text

df["review"] = df["review"].apply(clean_text)

print("\nCleaned Text Preview:")
print(df.head())

# Task 2: Split data
X = df["review"]
y = df["sentiment"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(max_features=5000)

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

print("\nText vectorization completed")

# Train Logistic Regression model
model = LogisticRegression()
model.fit(X_train_vec, y_train)

print("Model trained successfully")

# Task 3: Evaluate model
y_pred = model.predict(X_test_vec)

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", round(accuracy, 2))

print("\nClassification Report:")
report = classification_report(y_test, y_pred)
print(report)

# Save report
with open("sentiment_report.txt", "w") as file:
    file.write("Lab 28: Sentiment Analysis Concept\n\n")
    file.write(f"Model Accuracy: {round(accuracy, 2)}\n\n")
    file.write("Classification Report:\n")
    file.write(report)

print("\nFiles created:")
print("sentiment_dataset.csv")
print("sentiment_report.txt")

print("\nLab completed successfully.")
