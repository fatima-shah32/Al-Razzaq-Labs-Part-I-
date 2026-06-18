# Lab 49: Using and Creating Man Pages

## Objective

Learn how to use existing Linux man pages and create a custom man page for a shell script.

---

## Prerequisites

* Linux Operating System
* Terminal Access
* man Command Installed
* gzip Utility

---

## Task 1: Using Existing Man Pages

### View ls Manual

```bash
man ls
```

### Navigation

* Arrow Keys → Scroll
* Space → Next Page
* q → Quit

### Purpose

Learn how Linux manual pages provide command documentation.

---

## Task 2: Create a Simple Script

### Create Script

```bash
nano test_script.sh
```

### Script Content

```bash
#!/bin/bash
echo "This is a test script."
```

### Make Executable

```bash
chmod +x test_script.sh
```

---

## Task 3: Create Custom Man Page

### Create File

```bash
nano test_script.1
```

### Content

```roff
.TH TEST_SCRIPT 1 "June 2026" "Version 1.0" "Custom Manual"
.SH NAME
test_script \- A simple test script demonstration.
.SH SYNOPSIS
test_script
.SH DESCRIPTION
This script outputs a simple message: "This is a test script."
.SH AUTHOR
Fatima Danyal
```

---

## Task 4: Install Man Page

### Compress File

```bash
gzip test_script.1
```

### Install

```bash
sudo mv test_script.1.gz /usr/local/share/man/man1/
```

### Refresh Database

```bash
sudo mandb
```

### View Custom Page

```bash
man test_script
```

---

## Summary

| Command         | Purpose                |
| --------------- | ---------------------- |
| man ls          | View existing man page |
| gzip file       | Compress man page      |
| mandb           | Update man database    |
| man test_script | View custom page       |

---

## Conclusion

In this lab, I learned how Linux manual pages work and how to create, install, and access a custom man page for a shell script.
