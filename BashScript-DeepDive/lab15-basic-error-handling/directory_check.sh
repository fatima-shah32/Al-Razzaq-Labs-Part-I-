#!/bin/bash

# Directory to check
DIRECTORY="$HOME/test_directory"

# Check if directory exists
if [ -d "$DIRECTORY" ]; then
    echo "Directory exists."
else
    echo "Error: Directory does not exist."
    echo "Please create the directory before proceeding."
    exit 1
fi
