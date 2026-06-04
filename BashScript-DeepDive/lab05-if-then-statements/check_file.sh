#!/bin/bash

FILENAME="example.txt"

if [ -f "$FILENAME" ]; then
    echo "File exists."
else
    echo "File not found."
fi
