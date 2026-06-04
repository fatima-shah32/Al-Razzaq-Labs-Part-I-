#!/bin/bash

# Prompt for the first number
echo "Enter the first number:"
read num1

# Prompt for the second number
echo "Enter the second number:"
read num2

# Addition
sum=$((num1 + num2))
echo "The sum is: $sum"

sum_bc=$(echo "$num1 + $num2" | bc)
echo "The sum using bc is: $sum_bc"

# Subtraction
difference=$((num1 - num2))
echo "The difference is: $difference"

difference_bc=$(echo "$num1 - $num2" | bc)
echo "The difference using bc is: $difference_bc"

# Multiplication
product=$((num1 * num2))
echo "The product is: $product"

product_bc=$(echo "$num1 * $num2" | bc)
echo "The product using bc is: $product_bc"

# Division
if [ "$num2" -ne 0 ]; then
    quotient=$((num1 / num2))
    echo "The quotient is: $quotient"

    quotient_bc=$(echo "scale=2; $num1 / $num2" | bc)
    echo "The quotient using bc is: $quotient_bc"
else
    echo "Division by zero is not allowed."
fi
