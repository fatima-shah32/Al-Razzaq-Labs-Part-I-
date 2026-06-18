# Lab 49: Introduction to Sentiment Analysis with Python

## Objective

Learn how to prepare text data, clean text, train a sentiment classifier, and evaluate predictions.

## Tasks Completed

### 1. Created labeled sentiment dataset

A small dataset was created with positive and negative movie review examples.

### 2. Cleaned text data

Text was converted to lowercase, punctuation was removed, tokenization was applied, and stopwords were removed.

### 3. Converted text to numerical features

TF-IDF Vectorizer was used to convert text into machine-readable numerical features.

### 4. Trained sentiment classifier

Logistic Regression was used to classify reviews as positive or negative.

### 5. Evaluated model

Accuracy score and classification report were used to evaluate the model.

## Commands Used

```bash
python3 -m venv ml-env
source ml-env/bin/activate
pip install pandas scikit-learn nltk
python sentiment_analysis.py
Conclusion

In this lab, I learned the basics of sentiment analysis using Python. I prepared a labeled text dataset, cleaned text data, trained a Logistic Regression classifier, and evaluated the model using accuracy and classification metrics.
