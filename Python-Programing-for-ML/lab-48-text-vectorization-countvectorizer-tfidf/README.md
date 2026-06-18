# Lab 48: Text Vectorization with CountVectorizer and TF-IDF

## Objective

Understand text vectorization techniques used in Natural Language Processing.

---

## Task 1: CountVectorizer

### Import Libraries

```python
from sklearn.feature_extraction.text import CountVectorizer
```

### Sample Dataset

```python
documents = [
    "Text analysis is an interesting field.",
    "Machine Learning is part of data science.",
    "Text analysis involves understanding data."
]
```

### Apply CountVectorizer

```python
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)
```

### Display Results

```python
print(vectorizer.get_feature_names_out())
print(X.toarray())
```

---

## Task 2: TF-IDF Transformation

### Import

```python
from sklearn.feature_extraction.text import TfidfTransformer
```

### Apply TF-IDF

```python
tfidf_transformer = TfidfTransformer()
tfidf_matrix = tfidf_transformer.fit_transform(X)
```

### Display Results

```python
print(tfidf_matrix.toarray())
```

---

## Comparison

### CountVectorizer

Shows raw frequency of words.

### TF-IDF

Shows weighted importance of words across documents.

---

## Conclusion

In this lab, I learned how CountVectorizer converts text into token counts and how TF-IDF provides weighted word importance for NLP applications.
