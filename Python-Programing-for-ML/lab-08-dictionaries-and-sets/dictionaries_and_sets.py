print("=== Lab 8: Python Data Structures - Dictionaries and Sets ===")

# Task 1: Create Dictionary

book = {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "year_published": 1960
}

print("\nOriginal Dictionary:")
print(book)

# Task 2: Access Dictionary Value

author_name = book["author"]

print("\nAuthor Name:")
print(author_name)

# Update Dictionary Value

book["year_published"] = 1961

print("\nUpdated Publication Year:")
print(book)

# Add New Key-Value Pair

book["genre"] = "Fiction"

print("\nDictionary After Adding Genre:")
print(book)

# Task 3: Sets

fruits = {"apple", "banana", "cherry"}

print("\nOriginal Set:")
print(fruits)

# Add Element

fruits.add("orange")

print("\nAfter Adding Orange:")
print(fruits)

# Remove Element

fruits.discard("banana")

print("\nAfter Removing Banana:")
print(fruits)

# Another Set

tropical_fruits = {
    "pineapple",
    "mango",
    "papaya",
    "apple"
}

# Union

all_fruits = fruits.union(tropical_fruits)

print("\nUnion of Sets:")
print(all_fruits)

# Intersection

common_fruits = fruits.intersection(tropical_fruits)

print("\nIntersection of Sets:")
print(common_fruits)

print("\nLab completed successfully.")
