# Lab 19: Parsing Command Output (cut/grep/awk)

## Objective

Learn how to use Linux text-processing commands such as grep, awk, and cut to filter and extract information from command outputs.

## Tasks Completed

### Task 1
Displayed all running processes using ps aux.

### Task 2
Filtered process output using grep.

### Task 3
Extracted PID and COMMAND fields using awk.

### Task 4
Used cut to extract specific fields from a text file.

### Task 5
Executed and verified all commands successfully.

## Concepts Used

- ps aux
- grep
- awk
- cut
- Pipes (|)
- Process Monitoring
- Text Processing

## Sample Commands

ps aux

ps aux | grep 'bash'

ps aux | awk '{print $2, $11}'

cut -d',' -f1 users.txt

## Sample Output

bash

1234 bash

Alice
Bob
Charlie
