#!/bin/bash

# Prompt user for input
echo "Enter a string:"
read user_input

# Display input
echo "You entered: $user_input"

# Calculate string length
string_length=${#user_input}
echo "The length of the string is: $string_length"

# Extract substring from position 2 to 5
substring=${user_input:2:4}
echo "Substring from position 2 to 5 is: $substring"

# Replace 'abc' with 'xyz'
modified_string=${user_input//abc/xyz}
echo "Modified string: $modified_string"
