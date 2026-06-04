#!/bin/bash

# This script copies a file from the source to the destination
# and checks for success or failure.

SOURCE=$1
DESTINATION=$2

# Validate arguments
if [ -z "$SOURCE" ] || [ -z "$DESTINATION" ]; then
    echo "Usage: $0 <source_file> <destination_file>"
    exit 1
fi

# Check if source file exists
if [ ! -f "$SOURCE" ]; then
    echo "Error: Source file '$SOURCE' does not exist."
    exit 1
fi

# Copy file
cp "$SOURCE" "$DESTINATION"

# Verify copy operation
if [ $? -eq 0 ]; then
    echo "File copied successfully to '$DESTINATION'."
else
    echo "Error in copying file."
    exit 1
fi
