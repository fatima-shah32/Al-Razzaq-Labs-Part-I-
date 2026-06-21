print("=== Lab 6: Python Basics - Loops and Iterations ===")

# Task 1: For Loop

numbers = [1, 2, 3, 4, 5]

print("\nTask 1: Using For Loop")

for number in numbers:
    print(number)

# Task 2: While Loop

print("\nTask 2: Using While Loop")

count = 0

while count < 5:
    print("Count is:", count)
    count += 1

# Task 3: Iteration Tracking

print("\nTask 3: Iteration Tracking with For Loop")

for i, number in enumerate(numbers):
    print(f"Iteration {i + 1} - Number is: {number}")

print("\nTask 3: Iteration Tracking with While Loop")

count = 0

while count < 5:
    print(f"\nStart of Iteration {count + 1}")
    print("Count is:", count)
    print(f"End of Iteration {count + 1}")
    count += 1

print("\nLab completed successfully.")
