import nltk
import pandas as pd

from nltk.corpus import movie_reviews
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

print("=== Lab 27: Introduction to NLP ===")

# Download datasets
nltk.download('movie_reviews')
nltk.download('punkt')

# Task 1: Load Dataset
documents = [
    (list(movie_reviews.words(fileid)), category)
    for category in movie_reviews.categories()
    for fileid in movie_reviews.fileids(category)
]

print(f"\nTotal number of documents: {len(documents)}")

# First document
first_document_text = " ".join(documents[0][0])

print("\nFirst 200 Characters:")
print(first_document_text[:200])

# Task 2: Tokenization
tokens = word_tokenize(first_document_text)

print("\nFirst 20 Tokens:")
print(tokens[:20])

print(f"\nTotal Tokens: {len(tokens)}")

# Save tokens
token_df = pd.DataFrame(tokens, columns=["Token"])
token_df.to_csv("tokens.csv", index=False)

# Task 3: Word Frequency
fdist = FreqDist(tokens)

most_common_words = fdist.most_common(10)

print("\nTop 10 Most Common Words:")
for word, count in most_common_words:
    print(f"{word}: {count}")

# Save frequency report
freq_df = pd.DataFrame(
    most_common_words,
    columns=["Word", "Frequency"]
)

freq_df.to_csv("word_frequency.csv", index=False)

# Create text report
with open("nlp_report.txt", "w") as file:
    file.write("Lab 27: Introduction to NLP\n\n")
    file.write(f"Total Documents: {len(documents)}\n")
    file.write(f"Total Tokens: {len(tokens)}\n\n")

    file.write("Top 10 Most Common Words:\n")

    for word, count in most_common_words:
        file.write(f"{word}: {count}\n")

print("\nFiles Created:")
print("tokens.csv")
print("word_frequency.csv")
print("nlp_report.txt")

print("\nLab completed successfully.")
