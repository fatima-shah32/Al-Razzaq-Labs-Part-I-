print("=== Lab 4: Python Basics - Control Structures ===")

# Task 1: if-elif-else Conditions

print("\nTask 1: Temperature Check")

temperature = 15

if temperature > 25:
    print("It's a warm day!")
elif temperature > 20:
    print("It's a mild day!")
else:
    print("It's a cool day!")

# Task 2: For Loop

print("\nTask 2: For Loop")

for i in range(5):
    print("Iteration", i)

# Task 3: While Loop

print("\nTask 3: While Loop")

counter = 0

while counter < 5:
    print("Count is", counter)
    counter += 1

# Task 4: Even or Odd Number

print("\nTask 4: Even or Odd Check")

user_input = 8

if user_input % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Task 5: Inventory System

print("\nTask 5: Inventory Check")

inventory = {
    "apples": 15,
    "bananas": 5,
    "oranges": 12
}

for fruit, quantity in inventory.items():
    if quantity < 10:
        print(f"Restock {fruit}: Quantity is {quantity}")
    else:
        print(f"{fruit} are sufficiently stocked")

print("\nLab completed successfully.")
