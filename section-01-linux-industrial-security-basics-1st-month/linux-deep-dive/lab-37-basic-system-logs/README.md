# Lab 37: Basic System Logs

## Objective

Learn how to navigate Linux log files, inspect recent system messages, search logs, and monitor logs in real time.

---

## Prerequisites

* Linux Operating System
* Terminal Access
* Sudo Privileges

---

## Task 1: Navigate to /var/log

### Change Directory

```bash
cd /var/log
```

### List Log Files

```bash
ls -lh
```

### Purpose

The /var/log directory stores system and application log files.

---

## Task 2: View Recent System Logs

### Check Available Log Files

```bash
ls syslog messages
```

### Ubuntu Systems

```bash
less /var/log/syslog
```

### RHEL/CentOS Systems

```bash
less /var/log/messages
```

### Search for Errors

```bash
grep -i "error" /var/log/syslog
```

or

```bash
grep -i "error" /var/log/messages
```

---

## Task 3: Monitor Logs in Real Time

### Ubuntu

```bash
tail -f /var/log/syslog
```

### RHEL/CentOS

```bash
tail -f /var/log/messages
```

### Stop Monitoring

Press:

```text
CTRL + C
```

---

## Summary

| Command            | Purpose            |
| ------------------ | ------------------ |
| cd /var/log        | Open log directory |
| ls -lh             | List log files     |
| less logfile       | View logs          |
| grep error logfile | Search logs        |
| tail -f logfile    | Live monitoring    |

---

## Conclusion

In this lab, I learned how to navigate system log files, search for important events, and monitor logs in real time. These skills are essential for Linux troubleshooting and system administration.
