import numpy as np

print("=== Lab 04: Introduction to NumPy ===")

# Task 1: Create Arrays

arr1 = np.array([1, 2, 3, 4, 5])

print("\n1D Array:")
print(arr1)

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\n2D Array:")
print(arr2)

# Task 2: Indexing and Slicing

element = arr1[2]

print("\nAccessed Element:")
print(element)

subarray = arr2[0:2, 1:3]

print("\nSliced Array:")
print(subarray)

# Task 3: Built-in NumPy Functions

reshaped_array = arr1.reshape(5, 1)

print("\nReshaped Array:")
print(reshaped_array)

mean_value = np.mean(arr1)

print("\nMean:")
print(mean_value)

total_sum = np.sum(arr2)

print("\nTotal Sum:")
print(total_sum)

print("\nLab completed successfully.")
