# Lab 12: Working with Pandas - Series and DataFrames

## Objective

Learn how to create and manipulate Pandas Series and DataFrames.

## Tools Used

- Python
- Pandas

## Tasks Performed

1. Created a Pandas Series
2. Created a Series with custom indexes
3. Built a DataFrame from a dictionary
4. Accessed columns and rows
5. Modified DataFrame values
6. Added a new column
7. Saved DataFrame to CSV

## Main Code

```python
series = pd.Series(data)
```

```python
df = pd.DataFrame(data_dict)
```

```python
df.at[0, "Age"] = 26
```

```python
df["Country"] = ["USA", "USA", "USA"]
```

## Files Created

```text
employees.csv
```

## Final Structure

```text
lab-12-pandas-series-dataframes/
├── README.md
├── pandas_series_dataframe.py
├── employees.csv
└── ml-env/
```

## Conclusion

In this lab, I learned how to work with Pandas Series and DataFrames. I created and modified data structures, accessed rows and columns, added new data, and saved the results to a CSV file.
