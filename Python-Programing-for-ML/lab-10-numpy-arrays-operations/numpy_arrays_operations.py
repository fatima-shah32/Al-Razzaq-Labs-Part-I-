import numpy as np

print("=== Lab 10: Introduction to NumPy - Arrays and Operations ===")

# Task 1: Create Arrays

# 1D Array
one_dimensional_array = np.array([1, 2, 3, 4, 5])

print("\n1D Array:")
print(one_dimensional_array)

# 2D Array
two_dimensional_array = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\n2D Array:")
print(two_dimensional_array)

# Task 2: Arithmetic Operations

array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])

# Addition
addition_result = array_a + array_b

print("\nArray Addition:")
print(addition_result)

# Subtraction
subtraction_result = array_b - array_a

print("\nArray Subtraction:")
print(subtraction_result)

# Multiplication
multiplication_result = array_a * array_b

print("\nArray Multiplication:")
print(multiplication_result)

# Division
division_result = array_b / array_a

print("\nArray Division:")
print(division_result)

# Broadcasting
broadcast_result = array_a + 10

print("\nBroadcasting Example:")
print(broadcast_result)

# Task 3: Indexing and Slicing

print("\nFirst Element:")
print(one_dimensional_array[0])

print("\nLast Element:")
print(one_dimensional_array[-1])

# Slice 1D Array
print("\nSlice 1D Array:")
print(one_dimensional_array[1:4])

# Slice 2D Array
print("\nSlice 2D Array:")
print(two_dimensional_array[0:2, 1:3])

print("\nLab completed successfully.")
