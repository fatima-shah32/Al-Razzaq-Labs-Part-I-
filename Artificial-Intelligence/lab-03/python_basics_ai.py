print("=== Lab 03: Python Basics for AI ===")

# Task 1: Practice Data Types

# Lists
numbers = [10, 20, 30, 40, 50]

print("\nList Example:")
print("Numbers:", numbers)
print("Second element:", numbers[1])
print("Fourth element:", numbers[3])

# Tuples
measurements = (21.5, 22.8, 19.6, 20.0)

print("\nTuple Example:")
print("Measurements:", measurements)
print("First value:", measurements[0])
print("Last value:", measurements[-1])

# Dictionaries
book = {
    "title": "1984",
    "author": "George Orwell",
    "year": 1949
}

print("\nDictionary Example:")
print("Book:", book)
print("Book title:", book["title"])

# Task 2: Function for Basic Arithmetic

def calculate_difference(num1, num2):
    return num1 - num2

print("\nFunction Example:")
difference = calculate_difference(7, 2)
print("Difference:", difference)

# Task 3: Loops and Conditional Statements

# For loop
animals = ["cat", "dog", "bird"]

print("\nFor Loop Example:")
for animal in animals:
    print(animal)

# Conditional statement
number = 4

print("\nConditional Statement Example:")
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

print("\nLab completed successfully.")
