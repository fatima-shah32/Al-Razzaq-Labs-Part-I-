print("=== Lab 3: Python Basics - Variables and Data Types ===")

# Task 1: Declare Variables

age = 25
pi = 3.14159
name = "Alice"
is_student = True

# Display Variables

print("\nTask 1 & 2: Variable Values")

print("Name:", name)
print("Age:", age)
print("PI Value:", pi)
print("Is Student:", is_student)

# Task 3: Type Conversion

print("\nTask 3: Type Conversion")

# Implicit Conversion
result = age + 5.5
print("Implicit Conversion Result:", result)
print("Result Type:", type(result))

# Explicit Conversion
whole_number = int(pi)
print("Float to Integer:", whole_number)

age_str = str(age)
print("Integer to String:", age_str)

pi_float = float(age)
print("Integer to Float:", pi_float)

student_str = str(is_student)
print("Boolean to String:", student_str)

print("\nData Types")
print(type(age))
print(type(pi))
print(type(name))
print(type(is_student))

print("\nLab completed successfully.")
