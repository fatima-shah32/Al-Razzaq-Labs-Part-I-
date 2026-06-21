# Lab 9: File I/O in Python for Data

## Objective

Learn how to read and write files in Python and handle file-related exceptions.

## Tools Used

- Python

## Tasks Performed

1. Created a text file
2. Read file contents
3. Read file line by line
4. Wrote data to a file
5. Appended data to a file
6. Handled FileNotFoundError
7. Handled OSError exceptions

## Main Code

```python
with open("sample.txt", "r") as file:
    content = file.read()
```

```python
with open("output.txt", "w") as file:
    file.write("This is a new file.")
```

```python
with open("output.txt", "a") as file:
    file.write("Appending text")
```

```python
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")
```

## Files Created

```text
sample.txt
output.txt
```

## Final Structure

```text
lab-09-file-io-python/
├── README.md
├── file_io_python.py
├── sample.txt
├── output.txt
└── ml-env/
```

## Conclusion

In this lab, I learned how to perform file input and output operations in Python. I read data from files, wrote and appended content to files, and used exception handling to make file operations more reliable.
