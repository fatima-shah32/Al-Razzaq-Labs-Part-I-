#!/bin/bash

# Function to display current date and time
show_date() {
    echo "Current date and time: $(date)"
}

# Function to list files
list_files() {
    echo "Files in the current directory:"
    ls
}

# Function to exit script
exit_script() {
    echo "Exiting..."
    exit 0
}

# Main menu loop
while true; do
    echo "===================="
    echo " Bash Menu Interface"
    echo "===================="
    echo "1. Show date"
    echo "2. List files"
    echo "3. Exit"
    echo -n "Enter your choice: "

    read choice

    case $choice in
        1)
            show_date
            ;;
        2)
            list_files
            ;;
        3)
            exit_script
            ;;
        *)
            echo "Invalid option!"
            ;;
    esac

    echo ""
done
