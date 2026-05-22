# Lab 53 - Checking System Uptime

## Objectives
- Learn how to check system uptime
- Understand load averages
- Analyze Linux system performance

---

# Task 1 - Using uptime Command

## Run Command

```bash
uptime
```

## Example Output

```text
14:33:01 up 10 days, 22:45, 3 users, load average: 0.12, 0.15, 0.10
```

---

# Understanding Output

| Field | Meaning |
|---|---|
| Current Time | Current system time |
| Uptime | Total running time |
| Users | Logged-in users |
| Load Average | CPU/process workload |

---

# Task 2 - Understanding Load Average

## Load Time Periods

| Value | Meaning |
|---|---|
| First | Last 1 minute |
| Second | Last 5 minutes |
| Third | Last 15 minutes |

---

# CPU Load Interpretation

## Single CPU

| Load | Status |
|---|---|
| 1.0 | Fully utilized |
| < 1.0 | Healthy |
| > 1.0 | Heavy load |

---

# Multi-CPU Example

For a 4 CPU system:

| Load | Interpretation |
|---|---|
| 4.0 | Normal |
| 8.0 | Overloaded |

---

# Additional Commands

## Number of CPUs

```bash
nproc
```

## Real-Time Monitoring

```bash
top
```

Press q to quit.

---

# Screenshots

## uptime Command Output
```text
screenshots/01-uptime-command.png
```

## CPU Information
```text
screenshots/02-cpu-information.png
```

## top Command Output
```text
screenshots/03-top-command.png
```

---

# Outcome
Successfully learned:
- System uptime monitoring
- Load average interpretation
- CPU workload analysis
- Linux performance basics
