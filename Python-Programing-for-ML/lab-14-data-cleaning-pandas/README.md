# Lab 14: Data Cleaning using Pandas

## Objective

Learn how to clean data using Pandas by handling missing values, duplicate rows, and messy column formats.

## Tools Used

- Python
- Pandas

## Tasks Performed

1. Created a sample dataset
2. Checked missing values using `isnull().sum()`
3. Identified duplicate rows using `duplicated().sum()`
4. Removed duplicate rows
5. Removed missing values using `dropna()`
6. Filled missing values using `fillna()`
7. Removed whitespace from text columns
8. Changed column data types
9. Renamed columns
10. Saved cleaned data into a CSV file

## Main Code

```python
df.isnull().sum()
df.duplicated().sum()
df.dropna()
df.fillna()
Conclusion

In this lab, I learned how to clean data using Pandas. I handled missing values, removed duplicates, cleaned text columns, changed data types, renamed columns, and saved the final cleaned dataset.
