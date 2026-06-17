# Lab 28: Scheduling Tasks with Crontab

## Objective

Learn how to list, create, edit, and remove scheduled tasks using the Linux crontab utility.

---

## Prerequisites

* Linux Operating System
* Cron Service Installed
* Terminal Access

---

## Task 1: List Existing Cron Jobs

### Command

```bash
crontab -l
```

### Purpose

Displays all scheduled cron jobs for the current user.

---

## Task 2: Create a Script

### Create Script

```bash
nano ~/daily_script.sh
```

### Script Content

```bash
#!/bin/bash
echo "Hello, World!" >> ~/cron_output.txt
```

### Make Executable

```bash
chmod +x ~/daily_script.sh
```

---

## Task 3: Create a Cron Job

### Edit Crontab

```bash
crontab -e
```

### Add Entry

```bash
0 0 * * * /bin/bash ~/daily_script.sh
```

### Purpose

Runs the script every day at midnight.

---

## Task 4: Remove or Comment Cron Job

### Edit Crontab

```bash
crontab -e
```

### Comment Job

```bash
#0 0 * * * /bin/bash ~/daily_script.sh
```

Or remove the line completely.

### Verify

```bash
crontab -l
```

---

## Summary

| Command            | Purpose                |
| ------------------ | ---------------------- |
| crontab -l         | List cron jobs         |
| crontab -e         | Edit cron jobs         |
| chmod +x script.sh | Make script executable |
| 0 0 * * * command  | Run daily at midnight  |

---

## Conclusion

In this lab, I learned how to create automated tasks using crontab, schedule scripts, verify cron jobs, and remove scheduled tasks. Cron is an essential tool for Linux automation and system administration.
