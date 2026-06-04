#!/bin/bash

# Create an array of fruits
fruits=("apple" "banana" "cherry")

# Display the array
echo "Fruits array: ${fruits[@]}"

echo ""

# Loop through the array
for fruit in "${fruits[@]}"
do
    echo "Fruit: $fruit"
done

echo ""

# Add a new fruit
fruits+=("mango")

# Display updated array
echo "Updated Fruits array: ${fruits[@]}"
