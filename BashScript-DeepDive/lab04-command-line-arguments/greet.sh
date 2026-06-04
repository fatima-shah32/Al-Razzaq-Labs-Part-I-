#!/bin/bash

# Check if no arguments are provided
if [ $# -eq 0 ]; then
    echo "Error: No arguments supplied"
    echo "Usage: ./greet.sh <name1> <name2> ..."
    exit 1
fi

# Greet each name provided
for name in "$@"
do
    echo "Hello, $name!"
done
