# Lab 47: Natural Language Processing Basics with NLTK

## Objective

Learn the fundamentals of Natural Language Processing using the NLTK library.

---

## Task 1: Install and Import NLTK

Install:

```bash
pip install nltk
```

Import:

```python
import nltk
```

---

## Task 2: Tokenization

### Sentence Tokenization

```python
from nltk.tokenize import sent_tokenize

sentences = sent_tokenize(sample_text)
print(sentences)
```

### Word Tokenization

```python
from nltk.tokenize import word_tokenize

words = word_tokenize(sample_text)
print(words)
```

---

## Task 3: Text Preprocessing

### Stopword Removal

```python
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

filtered_words = [
    word for word in words
    if word.lower() not in stop_words
]
```

### Stemming

```python
from nltk.stem import PorterStemmer

ps = PorterStemmer()

stemmed_words = [
    ps.stem(word)
    for word in filtered_words
]
```

---

## Summary

| Technique             | Purpose                   |
| --------------------- | ------------------------- |
| Sentence Tokenization | Split text into sentences |
| Word Tokenization     | Split text into words     |
| Stopword Removal      | Remove common words       |
| Stemming              | Reduce words to root form |

---

## Conclusion

In this lab, I learned the basics of Natural Language Processing using NLTK. I performed sentence tokenization, word tokenization, stopword removal, and stemming to preprocess textual data for NLP applications.
