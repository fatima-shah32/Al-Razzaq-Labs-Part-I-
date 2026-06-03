# Lab 6: Looping with for

# Task 1: Print numbers from 1 to 5

print("Numbers from 1 to 5:")

for number in range(1, 6):
    print(number)

# Task 2: Loop through a list of strings

print("\nList of Fruits:")

fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    print(fruit)

# Task 3: Count processed items

print("\nCounting items processed:")

item_count = 0

for fruit in fruits:
    item_count += 1

print(f"Total number of items processed: {item_count}")
