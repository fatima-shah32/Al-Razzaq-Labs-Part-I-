# Lab 7: Looping with while

# Task 1: Print numbers 1 to 5 using a while loop

count = 1

print("Printing numbers from 1 to 5:")

while count <= 5:
    print(count)
    count += 1

print("\nInteractive Loop Started")

# Task 2 & 3: Interactive loop with graceful termination

try:
    while True:
        user_input = input("Enter a string (type 'exit' to quit): ")

        if user_input.lower() == "exit":
            print("Exiting the loop. Goodbye!")
            break

        print("You entered:", user_input)

finally:
    print("Program terminated successfully.")
