# Lab 24: Disk Usage and File Size

## Objective

Understand how to determine disk usage and file sizes in Linux using disk management commands.

---

## Prerequisites

* Linux Operating System
* Terminal Access
* Basic Linux Command Knowledge

---

## Task 1: Checking Directory Sizes

### Check Size of Current Directory

```bash
du -sh .
```

### Purpose

Displays the total size of the current directory.

---

### Check Size of All Files and Subdirectories

```bash
du -sh *
```

### Purpose

Displays the size of each file and subdirectory separately.

---

## Task 2: Analyze Disk Usage by Directory

### Identify Largest Directories

```bash
du -sh * | sort -hr
```

### Purpose

Sorts files and directories from largest to smallest.

---

## Task 3: Advanced Disk Usage Analysis

### View Detailed Disk Usage

```bash
du -ah . | sort -hr | head -20
```

### Purpose

Displays the largest files and directories in the current location.

---

## Additional Disk Usage Check

### View Filesystem Usage

```bash
df -h
```

### Purpose

Displays total disk usage and available storage.

---

## Summary

| Command             | Purpose                     |
| ------------------- | --------------------------- |
| du -sh .            | Show current directory size |
| du -sh *            | Show subdirectory sizes     |
| du -sh * | sort -hr | Largest directories first   |
| du -ah . | sort -hr | Largest files and folders   |
| df -h               | Filesystem usage            |

---

## Conclusion

In this lab, I learned how to analyze disk usage, identify large directories and files, and monitor available storage space using Linux disk management commands.
