# Lab 43: Swap Space Configuration

## Objective

Learn how to check, create, enable, and persist swap space on a Linux system.

---

## Prerequisites

* Linux Operating System
* Terminal Access
* Sudo Privileges

---

## Task 1: Check Current Swap Usage

### Show Active Swap

```bash
swapon --show
```

### Check Memory and Swap

```bash
free -h
```

---

## Task 2: Create Swap File

### Create 1GB Swap File

```bash
sudo fallocate -l 1G /swapfile
```

### Secure Permissions

```bash
sudo chmod 600 /swapfile
```

### Configure as Swap

```bash
sudo mkswap /swapfile
```

---

## Task 3: Enable Swap

### Activate Swap

```bash
sudo swapon /swapfile
```

### Verify

```bash
swapon --show
```

```bash
free -h
```

---

## Task 4: Make Swap Persistent

### Edit fstab

```bash
sudo nano /etc/fstab
```

### Add

```text
/swapfile none swap sw 0 0
```

---

## Summary

| Command       | Purpose          |
| ------------- | ---------------- |
| swapon --show | View swap        |
| free -h       | Memory usage     |
| fallocate     | Create swap file |
| chmod 600     | Secure file      |
| mkswap        | Initialize swap  |
| swapon        | Enable swap      |

---

## Conclusion

In this lab, I learned how to create and manage swap space, which provides additional virtual memory and improves Linux system stability.
