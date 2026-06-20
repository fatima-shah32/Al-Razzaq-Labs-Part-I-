import numpy as np

print("=== Lab 11: NumPy Array Operations and Slicing ===")

# Task 1: Create 2D Array
array_2d = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print("\nOriginal Array:")
print(array_2d)

# Basic Slicing
sliced_array = array_2d[:, 1:3]

print("\nSliced Array (Columns 2 to 3):")
print(sliced_array)

# Advanced Slicing
advanced_slicing = array_2d[::2, ::2]

print("\nAdvanced Slicing:")
print(advanced_slicing)

# Task 2: Vectorized Operations

# Addition
added_array = array_2d + 10

print("\nArray after Addition:")
print(added_array)

# Multiplication
multiplied_array = array_2d * 2

print("\nArray after Multiplication:")
print(multiplied_array)

# Broadcasting
broadcast_array = array_2d + np.array([1, 0, 1, 0])

print("\nArray after Broadcasting:")
print(broadcast_array)

# Task 3: Reshaping Arrays

# Reshape
reshaped_array = np.arange(12).reshape(3, 4)

print("\nReshaped Array:")
print(reshaped_array)

# Flatten
flattened_array = array_2d.flatten()

print("\nFlattened Array:")
print(flattened_array)

# Transpose
transposed_array = array_2d.T

print("\nTransposed Array:")
print(transposed_array)

print("\nLab completed successfully.")
