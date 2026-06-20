# Lab 32: Using Regular Expressions for Data Cleaning

## Objective

Learn how to use regular expressions in Python for pattern matching and data cleaning.

## Tools Used

- Python
- re module

## Tasks Performed

1. Matched a phone number pattern
2. Extracted email addresses from text
3. Removed punctuation from text
4. Standardized phone numbers into one format

## Main Regex Examples

```python
r"\d{3}-\d{3}-\d{4}"
Used to match phone numbers.

r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

Used to extract email addresses.

r"[^\w\s]"

Used to remove punctuation.

Output

The program prints:

Matched phone number
Found email addresses
Cleaned text
Standardized phone numbers
Final Structure
lab-32-regex-data-cleaning/
├── README.md
├── regex_data_cleaning.py
└── ml-env/
Conclusion

In this lab, I learned how to use Python's re module for pattern matching and data cleaning. Regular expressions help clean and prepare text data for machine learning and data analysis tasks.
