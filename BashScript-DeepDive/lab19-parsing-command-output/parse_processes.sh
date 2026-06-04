#!/bin/bash

echo "==============================="
echo " Process Parsing Demonstration "
echo "==============================="

echo ""
echo "1. Displaying all running processes:"
ps aux

echo ""
echo "2. Filtering processes containing 'bash':"
ps aux | grep 'bash'

echo ""
echo "3. Extracting PID and COMMAND columns:"
ps aux | awk '{print $2, $11}'
