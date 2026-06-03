# Lab 10: Dictionary Operations

# Task 1: Create a dictionary
person_info = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

print("Original Dictionary:")
print(person_info)

# Task 2: Retrieve a value by key
name_value = person_info["name"]
print("\nName:", name_value)

# Task 3: Update a value
person_info["age"] = 31

# Add a new key-value pair
person_info["occupation"] = "Engineer"

# Print updated dictionary
print("\nUpdated Dictionary:")
print(person_info)
