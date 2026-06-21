print("=== Lab 9: File I/O in Python for Data ===")

# Create sample text file
with open("sample.txt", "w") as file:
    file.write("Python is an amazing programming language.\n")
    file.write("It is widely used in data science.\n")
    file.write("File I/O operations are essential.\n")

print("\nSample file created successfully.")

# Task 1: Read entire file
print("\nReading Entire File:")

file_path = "sample.txt"

with open(file_path, "r") as file:
    content = file.read()
    print(content)

# Read line by line
print("Reading File Line by Line:")

with open(file_path, "r") as file:
    for line in file:
        print(line.strip())

# Task 2: Write data to file
output_file = "output.txt"

with open(output_file, "w") as file:
    file.write("This is a new file.\n")
    file.write("We are writing data to it.\n")

print("\nData written to output.txt")

# Append data
with open(output_file, "a") as file:
    file.write("Appending a new line of text.\n")

print("Data appended successfully.")

# Display output file content
print("\nOutput File Content:")

with open(output_file, "r") as file:
    print(file.read())

# Task 3: Exception Handling

print("Testing File Exceptions:")

try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()

except FileNotFoundError:
    print("The file you are trying to read does not exist.")

try:
    with open(file_path, "r") as file:
        content = file.read()

except FileNotFoundError:
    print("The file does not exist.")

except OSError as e:
    print(f"An OS error occurred: {e}")

print("\nLab completed successfully.")
