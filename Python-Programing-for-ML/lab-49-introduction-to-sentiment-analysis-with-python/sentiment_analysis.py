import pandas as pd
import string
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")

data = {
    "text": [
        "I love this movie it is amazing",
        "This film was terrible and boring",
        "What a fantastic experience",
        "I hated the story and acting",
        "The movie was excellent",
        "This was the worst film ever",
        "I really enjoyed the performance",
        "The plot was dull and bad",
        "Beautiful direction and great acting",
        "Awful movie not recommended"
    ],
    "sentiment": [
        "positive",
        "negative",
        "positive",
        "negative",
        "positive",
        "negative",
        "positive",
        "negative",
        "positive",
        "negative"
    ]
}

df = pd.DataFrame(data)

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

df["cleaned_text"] = df["text"].apply(clean_text)

print("Dataset Preview:")
print(df.head())

X_train, X_test, y_train, y_test = train_test_split(
    df["cleaned_text"],
    df["sentiment"],
    test_size=0.2,
    random_state=42
)

vectorizer = TfidfVectorizer(max_features=5000)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

y_pred = model.predict(X_test_tfidf)

print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
