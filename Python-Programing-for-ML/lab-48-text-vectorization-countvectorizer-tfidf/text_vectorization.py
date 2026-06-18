import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

documents = [
    "Text analysis is an interesting field.",
    "Machine Learning is part of data science.",
    "Text analysis involves understanding data."
]

print("Original Documents:\n")
for doc in documents:
    print(doc)

# Count Vectorizer
vectorizer = CountVectorizer()

X = vectorizer.fit_transform(documents)

print("\nVocabulary:")
print(vectorizer.get_feature_names_out())

print("\nCount Vectorized Matrix:")
print(X.toarray())

# TF-IDF
tfidf_transformer = TfidfTransformer()

tfidf_matrix = tfidf_transformer.fit_transform(X)

print("\nTF-IDF Matrix:")
print(tfidf_matrix.toarray())
