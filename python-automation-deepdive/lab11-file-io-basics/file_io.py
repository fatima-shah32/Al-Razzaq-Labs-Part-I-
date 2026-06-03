# Lab 11: File I/O Basics

# Task 1: Create and write to a file
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a test of file I/O.\n")

print("File created and initial content written.")

# Task 2: Append text to the file
with open("output.txt", "a") as file:
    file.write("Appending new text.\n")

print("New text appended successfully.")

# Task 3: Read file contents
with open("output.txt", "r") as file:
    content = file.read()

print("\n📄 File Contents:")
print(content)
