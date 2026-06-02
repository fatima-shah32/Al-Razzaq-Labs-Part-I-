import sys

print("🔹 Number of arguments:", len(sys.argv))
print("🔹 Argument List:", sys.argv)

# Task 2: Handle no arguments case
if len(sys.argv) == 1:
    print("⚠️ No command-line arguments provided.")

# Print each argument
for i, arg in enumerate(sys.argv):
    print(f"Argument {i}: {arg}")

