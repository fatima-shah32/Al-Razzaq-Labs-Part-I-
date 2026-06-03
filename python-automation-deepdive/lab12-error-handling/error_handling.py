# Lab 12: Error Handling with try-except

try:
    # Get user input
    number = int(input("Enter a number to divide 100: "))

    # Perform division
    result = 100 / number

    # Display result
    print(f"Result: {result}")

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Please enter a valid number!")

except Exception as e:
    print(f"Unexpected error: {e}")

finally:
    print("Program execution completed.")
