# Lab 9: Working with Lists and Tuples

# Task 1: Creating and Printing a List
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print("Original list:")
print(fruits)

# Task 2: Modifying the List

# Add an element
fruits.append("fig")
print("\nAfter adding 'fig':")
print(fruits)

# Remove an element
fruits.remove("date")
print("\nAfter removing 'date':")
print(fruits)

# Sort the list
fruits.sort()
print("\nSorted list:")
print(fruits)

# Task 3: Demonstrating Lists vs Tuples

fruit_tuple = ("apple", "banana", "cherry", "elderberry", "fig")

print("\nTuple contents:")
print(fruit_tuple)

# Demonstrate immutability
try:
    fruit_tuple[0] = "avocado"
except TypeError as e:
    print("\nTuple Immutability Demonstration:")
    print("Error:", e)
