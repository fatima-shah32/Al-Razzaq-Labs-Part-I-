print("=== Lab 5: Python Basics - Functions ===")

# Task 1: Define Function with Parameter

def greet(name):
    print(f"Hello, {name}!")

# Task 2: Return Value from Function

def square(number):
    return number * number

# Task 3: Call Functions

print("\nCalling greet() Function:")

greet("Alice")
greet("Bob")
greet("Fatima")

print("\nCalling square() Function:")

result1 = square(5)
result2 = square(10)
result3 = square(15)

print("Square of 5 =", result1)
print("Square of 10 =", result2)
print("Square of 15 =", result3)

print("\nLab completed successfully.")
