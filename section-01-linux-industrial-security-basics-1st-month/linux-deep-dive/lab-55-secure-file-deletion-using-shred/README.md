# Lab: Secure File Deletion Using shred

## Introduction

In Linux systems, deleting a file using the `rm` command does not permanently erase the file contents. The file data may still remain on the storage device and could potentially be recovered using recovery tools.

The `shred` command securely deletes files by overwriting file contents multiple times with random data before removing them from the filesystem.

This lab demonstrates how to securely delete sensitive files using the `shred` command.

---

# Objectives

- Understand secure file deletion concepts
- Learn how to use the `shred` command
- Securely overwrite and remove files
- Verify that deleted files cannot be recovered easily

---

# Prerequisites

- Linux operating system
- Basic command line knowledge
- Access to terminal
- Basic understanding of file permissions

---

# Overview

The `shred` command overwrites files multiple times with random data before deleting them.

Unlike normal deletion:
- `rm` removes file references only
- `shred` destroys actual file contents

This process makes data recovery significantly harder, especially on HDD storage devices.

---

# Task 1 — Creating a Test File

## Step 1: Create a Sample File

Run the following command:

```bash
echo "This is a sensitive file that needs secure deletion." > sample.txt
```

### Explanation

This command:
- Creates a file named `sample.txt`
- Stores sensitive text inside the file

---

# Screenshot 1

Add screenshot here:

```text
Screenshot of sample file creation
```

---

## Step 2: Verify File Contents

Run:

```bash
cat sample.txt
```

### Expected Output

```text
This is a sensitive file that needs secure deletion.
```

### Explanation

The `cat` command displays the contents of the file.

---

# Screenshot 2

Add screenshot here:

```text
Screenshot of cat sample.txt
```

---

# Task 2 — Using shred for Secure Deletion

## Step 1: Securely Delete the File

Run:

```bash
shred -u sample.txt
```

### Explanation

| Option | Description |
|---|---|
| shred | Overwrites file contents |
| -u | Removes file after overwriting |

The file is:
1. Overwritten multiple times
2. Securely removed afterward

---

# Screenshot 3

Add screenshot here:

```text
Screenshot of shred -u sample.txt
```

---

## Step 2: Increase Overwrite Count

For additional security:

```bash
shred -n 5 -u sample.txt
```

### Explanation

| Option | Description |
|---|---|
| -n 5 | Overwrite file 5 times |
| -u | Delete file after overwrite |

More overwrite passes improve data destruction security.

---

# Important Note

The `shred` command works best on:
- Traditional HDD drives

Limitations exist on:
- SSD drives
- Journaled filesystems

This is due to how SSDs internally manage storage blocks.

---

# Screenshot 4

Add screenshot here:

```text
Screenshot of shred -n 5 -u sample.txt
```

---

# Task 3 — Verification of Unrecoverability

## Step 1: Verify File Deletion

Run:

```bash
ls -l sample.txt
```

### Expected Output

```bash
ls: cannot access 'sample.txt': No such file or directory
```

### Explanation

This confirms that the file no longer exists in the filesystem.

---

# Screenshot 5

Add screenshot here:

```text
Screenshot of ls -l sample.txt
```

---

## Step 2: Attempt File Recovery

Run:

```bash
grep "sensitive" sample.txt
```

### Expected Output

```bash
grep: sample.txt: No such file or directory
```

### Explanation

This verifies:
- File content is inaccessible
- File was securely removed

---

# Screenshot 6

Add screenshot here:

```text
Screenshot of grep sensitive sample.txt
```

---

# Verification Checklist

- [x] Created sensitive test file
- [x] Verified file contents
- [x] Used shred for secure deletion
- [x] Verified file removal
- [x] Confirmed unrecoverability attempt failed

---

# Key Concepts Learned

| Command | Purpose |
|---|---|
| echo | Create file with content |
| cat | Display file contents |
| shred | Securely overwrite files |
| ls | Verify file existence |
| grep | Search file content |

---

# Conclusion

In this lab, we learned how to securely delete files using the Linux `shred` command.

We successfully:
- Created a sensitive file
- Securely overwrote file contents
- Permanently removed the file
- Verified the file could not be accessed afterward

Secure deletion is essential when handling confidential or sensitive information in Linux environments.

---

# Key Takeaway

The `shred` command provides a powerful method for secure file destruction by overwriting file contents multiple times before deletion.

This helps protect sensitive data from unauthorized recovery attempts.
