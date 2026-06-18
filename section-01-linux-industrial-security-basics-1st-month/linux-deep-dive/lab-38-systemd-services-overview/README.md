# Lab 38: Systemd Services Overview

## Objective

Learn how to manage Linux services using systemd and the systemctl command.

---

## Prerequisites

* Linux Operating System
* systemd Installed
* Terminal Access
* Sudo Privileges

---

## Task 1: List Running Services

### Command

```bash
systemctl list-units --type=service
```

### Purpose

Displays active systemd services and their status.

---

## Task 2: Start a Service

### Example Service

```bash
sudo systemctl start cron
```

### Verify Status

```bash
systemctl status cron
```

### Purpose

Starts the selected service.

---

## Task 3: Stop a Service

### Command

```bash
sudo systemctl stop cron
```

### Verify Status

```bash
systemctl status cron
```

### Purpose

Stops the selected service.

---

## Task 4: Enable Service at Boot

### Command

```bash
sudo systemctl enable cron
```

### Verify

```bash
systemctl is-enabled cron
```

### Purpose

Starts the service automatically during system boot.

---

## Task 5: Disable Service at Boot

### Command

```bash
sudo systemctl disable cron
```

### Verify

```bash
systemctl is-enabled cron
```

### Purpose

Prevents the service from starting automatically at boot.

---

## Summary

| Command                             | Purpose         |
| ----------------------------------- | --------------- |
| systemctl list-units --type=service | List services   |
| systemctl status service            | Check status    |
| sudo systemctl start service        | Start service   |
| sudo systemctl stop service         | Stop service    |
| sudo systemctl enable service       | Enable at boot  |
| sudo systemctl disable service      | Disable at boot |

---

## Conclusion

In this lab, I learned how to list, start, stop, enable, and disable services using systemd. These commands are essential for Linux system administration and service management.
