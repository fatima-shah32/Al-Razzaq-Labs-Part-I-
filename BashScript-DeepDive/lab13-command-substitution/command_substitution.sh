#!/bin/bash

# Store current date
CURRENT_DATE=$(date)
echo "Today is $CURRENT_DATE"

# Store current username
USER_NAME=$(whoami)
echo "Current user: $USER_NAME"

# Store current directory
CURRENT_DIR=$(pwd)
echo "Current directory: $CURRENT_DIR"

# Store kernel version
KERNEL_VERSION=$(uname -r)
echo "Kernel Version: $KERNEL_VERSION"
