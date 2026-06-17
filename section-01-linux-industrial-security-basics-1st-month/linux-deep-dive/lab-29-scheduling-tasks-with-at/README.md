# Lab 29: Scheduling Tasks with at

## Objective

Learn how to schedule one-time tasks using the Linux at command and manage scheduled jobs.

---

## Prerequisites

* Linux Operating System
* Terminal Access
* Sudo Privileges

---

## Task 1: Check and Install at

### Check Version

```bash
at -V
```

### Install at (Ubuntu/Debian)

```bash
sudo apt-get update
sudo apt-get install at -y
```

### Start Service

```bash
sudo systemctl start atd
sudo systemctl enable atd
```

### Ubuntu Note

Some Ubuntu systems use:

```bash
sudo systemctl start atd
```

or

```bash
sudo systemctl start atd.service
```

---

## Task 2: Schedule a One-Time Task

### Schedule Job

```bash
echo "echo 'Hello World' >> ~/hello.txt" | at now + 1 minute
```

### Purpose

Creates a one-time task that runs after one minute.

---

## Task 3: List Scheduled Jobs

### Command

```bash
atq
```

### Purpose

Displays pending at jobs.

---

## Task 4: Remove a Scheduled Job

### Command

```bash
atrm <job_id>
```

Example:

```bash
atrm 1
```

### Verify Removal

```bash
atq
```

---

## Summary

| Command           | Purpose       |
| ----------------- | ------------- |
| at -V             | Check version |
| atq               | List jobs     |
| atrm jobid        | Remove job    |
| at now + 1 minute | Schedule task |

---

## Conclusion

In this lab, I learned how to install the at utility, schedule one-time tasks, verify scheduled jobs, and remove pending jobs. The at command is useful when tasks need to run only once at a specific future time.
