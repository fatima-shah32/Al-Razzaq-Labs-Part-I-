import csv

# Task 3: Reading CSV file
print("📂 Reading CSV file...\n")

with open("sample.csv", mode="r") as file:
    csv_reader = csv.reader(file)

    # Print structured rows
    for row in csv_reader:
        print(f"Name: {row[0]}, Age: {row[1]}, Occupation: {row[2]}")

print("\n📊 Summary Section:\n")

# Task 4: Summarizing data
total_age = 0
row_count = 0

with open("sample.csv", mode="r") as file:
    csv_reader = csv.reader(file)

    next(csv_reader)  # Skip header row

    for row in csv_reader:
        total_age += int(row[1])
        row_count += 1

print(f"Total number of entries: {row_count}")
print(f"Total age combined: {total_age}")
