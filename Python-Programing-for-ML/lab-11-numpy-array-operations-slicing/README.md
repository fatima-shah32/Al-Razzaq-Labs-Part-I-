# Lab 11: NumPy Array Operations and Slicing

## Objective

Learn array slicing, vectorized operations, broadcasting, and reshaping using NumPy.

## Tools Used

- Python
- NumPy

## Tasks Performed

1. Created a 2D NumPy array
2. Applied basic slicing
3. Applied advanced slicing
4. Performed vectorized addition and multiplication
5. Used broadcasting
6. Reshaped arrays
7. Flattened arrays
8. Transposed arrays

## Main Code

```python
sliced_array = array_2d[:, 1:3]
```

```python
added_array = array_2d + 10
multiplied_array = array_2d * 2
```

```python
reshaped_array = np.arange(12).reshape(3, 4)
```

```python
flattened_array = array_2d.flatten()
transposed_array = array_2d.T
```

## Final Structure

```text
lab-11-numpy-array-operations-slicing/
├── README.md
├── numpy_array_operations.py
└── ml-env/
```

## Conclusion

In this lab, I learned how to perform array slicing, vectorized computations, broadcasting, reshaping, flattening, and transposing using NumPy. These operations are essential for efficient numerical computing and machine learning workflows.
