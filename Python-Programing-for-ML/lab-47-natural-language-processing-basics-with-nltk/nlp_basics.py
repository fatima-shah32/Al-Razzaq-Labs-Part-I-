import nltk

# Download required datasets
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

sample_text = """
Natural Language Processing (NLP) enables computers to understand and communicate in human language.
It's an exciting field!
"""

print("Original Text:\n")
print(sample_text)

# Sentence Tokenization
sentences = sent_tokenize(sample_text)

print("\nSentence Tokens:")
print(sentences)

# Word Tokenization
words = word_tokenize(sample_text)

print("\nWord Tokens:")
print(words)

# Stopword Removal
stop_words = set(stopwords.words('english'))

filtered_words = [
    word for word in words
    if word.lower() not in stop_words
]

print("\nAfter Stopword Removal:")
print(filtered_words)

# Stemming
ps = PorterStemmer()

stemmed_words = [ps.stem(word) for word in filtered_words]

print("\nStemmed Words:")
print(stemmed_words)
