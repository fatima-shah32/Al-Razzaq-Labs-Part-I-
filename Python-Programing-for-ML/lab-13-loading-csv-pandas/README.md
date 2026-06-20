# Lab 13: Loading CSV Data with Pandas

## Objective

Learn how to load CSV files using Pandas and inspect the dataset for missing values.

## Tools Used

- Python
- Pandas

## Tasks Performed

1. Created a sample CSV file
2. Loaded CSV data using Pandas
3. Displayed first rows using head()
4. Viewed dataset information using info()
5. Identified missing values using isnull().sum()

## Main Code

```python
import pandas as pd

df = pd.read_csv("sample_data.csv")
```

```python
print(df.head())
```

```python
print(df.isnull().sum())
```

## Files Created

```text
sample_data.csv
```

## Final Structure

```text
lab-13-loading-csv-pandas/
├── README.md
├── load_csv_pandas.py
├── sample_data.csv
└── ml-env/
```

## Conclusion

In this lab, I learned how to load CSV files using Pandas, inspect the dataset structure, display sample records, and identify missing values for further data cleaning and analysis.
