#!/bin/bash

# Check if an argument is passed
if [ -z "$1" ]; then
    echo "Usage: $0 {start|stop|status}"
    exit 1
fi

# Use case statement to handle different arguments
case $1 in
    start)
        echo "Starting the service..."
        ;;
    stop)
        echo "Stopping the service..."
        ;;
    status)
        echo "Checking the service status..."
        ;;
    *)
        echo "Invalid command"
        ;;
esac
