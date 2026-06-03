# Lab 8: Creating and Using Functions

# Task 1 & 2: Function with Return Value
def greet(name):
    return f"Hello, {name}!"

# Main function
def main():
    greeting1 = greet("Alice")
    greeting2 = greet("Bob")

    print(greeting1)
    print(greeting2)

# Execute program
if __name__ == "__main__":
    main()
