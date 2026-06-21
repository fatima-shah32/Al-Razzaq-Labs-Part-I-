import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn import metrics


print("=== Lab 29: Text Vectorization Bag-of-Words and TF-IDF ===")

# Sample documents
documents = [
    "I love machine learning.",
    "Machine learning is amazing.",
    "I love creating machine learning models.",
    "Models are crucial for predictive analytics."
]

labels = [1, 1, 1, 0]

print("\nOriginal Documents:")
for doc in documents:
    print(doc)

# Task 1: Bag-of-Words
vectorizer = CountVectorizer()
X_bow = vectorizer.fit_transform(documents)

print("\nBag-of-Words Feature Names:")
print(vectorizer.get_feature_names_out())

print("\nBag-of-Words Matrix:")
print(X_bow.toarray())

bow_df = pd.DataFrame(
    X_bow.toarray(),
    columns=vectorizer.get_feature_names_out()
)

bow_df.to_csv("bag_of_words_matrix.csv", index=False)

# Task 2: TF-IDF
tfidf_vectorizer = TfidfVectorizer()
X_tfidf = tfidf_vectorizer.fit_transform(documents)

print("\nTF-IDF Feature Names:")
print(tfidf_vectorizer.get_feature_names_out())

print("\nTF-IDF Matrix:")
print(X_tfidf.toarray())

tfidf_df = pd.DataFrame(
    X_tfidf.toarray(),
    columns=tfidf_vectorizer.get_feature_names_out()
)

tfidf_df.to_csv("tfidf_matrix.csv", index=False)

# Task 3: Train Classifier with Bag-of-Words
X_train_bow, X_test_bow, y_train_bow, y_test_bow = train_test_split(
    X_bow,
    labels,
    test_size=0.25,
    random_state=42
)

clf_bow = MultinomialNB()
clf_bow.fit(X_train_bow, y_train_bow)

y_pred_bow = clf_bow.predict(X_test_bow)

bow_accuracy = metrics.accuracy_score(
    y_test_bow,
    y_pred_bow
)

print("\nBag-of-Words Naive Bayes Accuracy:")
print(bow_accuracy)

# Train Classifier with TF-IDF
X_train_tfidf, X_test_tfidf, y_train_tfidf, y_test_tfidf = train_test_split(
    X_tfidf,
    labels,
    test_size=0.25,
    random_state=42
)

clf_tfidf = MultinomialNB()
clf_tfidf.fit(X_train_tfidf, y_train_tfidf)

y_pred_tfidf = clf_tfidf.predict(X_test_tfidf)

tfidf_accuracy = metrics.accuracy_score(
    y_test_tfidf,
    y_pred_tfidf
)

print("\nTF-IDF Naive Bayes Accuracy:")
print(tfidf_accuracy)

# Save comparison report
with open("vectorization_report.txt", "w") as file:
    file.write("Lab 29: Text Vectorization Bag-of-Words and TF-IDF\n\n")
    file.write("Bag-of-Words Accuracy: " + str(bow_accuracy) + "\n")
    file.write("TF-IDF Accuracy: " + str(tfidf_accuracy) + "\n\n")
    file.write("Bag-of-Words counts word frequency.\n")
    file.write("TF-IDF gives importance to words based on frequency and rarity.\n")
    file.write("Small datasets may not show reliable accuracy results.\n")

print("\nFiles created:")
print("bag_of_words_matrix.csv")
print("tfidf_matrix.csv")
print("vectorization_report.txt")

print("\nLab completed successfully.")
