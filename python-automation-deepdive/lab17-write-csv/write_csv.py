import csv

# Task 1: Data preparation
data_dict = [
    {"Name": "Alice", "Age": 28, "City": "New York"},
    {"Name": "Bob", "Age": 34, "City": "Chicago"},
    {"Name": "Charlie", "Age": 22, "City": "San Francisco"}
]

# Task 2: Write to CSV file
with open("people.csv", "w", newline="") as file:
    fieldnames = ["Name", "Age", "City"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write header
    writer.writeheader()

    # Write rows
    for row in data_dict:
        writer.writerow(row)

print("✅ CSV file 'people.csv' created successfully!")
