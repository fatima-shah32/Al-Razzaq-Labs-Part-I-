# Lab 16: Scheduling Scripts with Cron (Demo)

## Objective

Learn how to automate tasks using Cron by scheduling a Bash script to execute automatically.

## Tasks Completed

### Task 1
Created a Bash script that writes text to a file.

### Task 2
Made the script executable.

### Task 3
Scheduled the script using Cron.

### Task 4
Verified the Cron job configuration.

### Task 5
Confirmed automatic execution through the output file.

## Concepts Used

- Bash Scripting
- Cron Jobs
- Task Automation
- File Operations
- Linux Scheduling

## Script

```bash
#!/bin/bash
echo "Cron test" >> ~/cron_output.txt
```

## Cron Entry

```bash
* * * * * /path/to/cron_test.sh
```

## Sample Output

Cron test
Cron test
Cron test
