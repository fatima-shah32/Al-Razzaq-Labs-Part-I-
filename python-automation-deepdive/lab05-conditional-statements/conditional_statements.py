# Lab 5: Conditional Statements (if, elif, else)

# Test Case 1: Number 1 is greater
print("=== Test Case 1 ===")
number1 = 30
number2 = 20

if number1 > number2:
    print("Number 1 is larger")
elif number1 < number2:
    print("Number 2 is larger")
else:
    print("Both numbers are equal")

# Test Case 2: Number 2 is greater
print("\n=== Test Case 2 ===")
number1 = 15
number2 = 25

if number1 > number2:
    print("Number 1 is larger")
elif number1 < number2:
    print("Number 2 is larger")
else:
    print("Both numbers are equal")

# Test Case 3: Both numbers are equal
print("\n=== Test Case 3 ===")
number1 = 50
number2 = 50

if number1 > number2:
    print("Number 1 is larger")
elif number1 < number2:
    print("Number 2 is larger")
else:
    print("Both numbers are equal")
