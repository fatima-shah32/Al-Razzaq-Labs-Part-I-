print("=== Lab 7: Python Data Structures - Lists and Tuples ===")

# Task 1: Lists

fruits = ["apple", "banana", "cherry"]

print("\nOriginal List:")
print(fruits)

# Add Elements
fruits.append("orange")
fruits.insert(1, "grape")

print("\nAfter Adding Elements:")
print(fruits)

# Remove Elements
fruits.remove("banana")
fruits.pop(2)

print("\nAfter Removing Elements:")
print(fruits)

# Slicing
some_fruits = fruits[1:3]

print("\nSliced List:")
print(some_fruits)

# Modify List (Mutability)
fruits[0] = "kiwi"

print("\nModified List:")
print(fruits)

# Task 2: Tuples

vegetables = ("carrot", "broccoli", "spinach")

print("\nTuple:")
print(vegetables)

# Access Tuple Element
first_vegetable = vegetables[0]

print("\nFirst Vegetable:")
print(first_vegetable)

# Task 3: Mutability vs Immutability

print("\nMutability Example (List):")
print("Lists can be modified.")

print("\nImmutability Example (Tuple):")
print("Tuples cannot be modified after creation.")

print("\nLab completed successfully.")
