# Lab 36: Searching with find

## Objective

Learn how to use the Linux find command to search files based on name, size, and execute commands on found files.

---

## Prerequisites

* Linux Operating System
* Terminal Access
* Basic Command Line Knowledge

---

## Task 1: Find All .txt Files in Home Directory

### Command

```bash
find ~ -name "*.txt"
```

### Purpose

Searches for all files ending with .txt in the home directory and its subdirectories.

---

## Task 2: Find Files Larger Than 1MB

### Command

```bash
find ~ -size +1M
```

### Purpose

Finds files larger than 1 Megabyte.

---

## Task 3: Execute Commands on Found Files

### Count Lines in All .txt Files

```bash
find ~ -name "*.txt" -exec wc -l {} \;
```

### Explanation

* -exec executes a command on each file found.
* {} represents the current file.
* ; terminates the command.

---

## Summary

| Command                               | Purpose              |
| ------------------------------------- | -------------------- |
| find ~ -name "*.txt"                  | Find text files      |
| find ~ -size +1M                      | Find large files     |
| find ~ -name "*.txt" -exec wc -l {} ; | Count lines in files |

---

## Conclusion

In this lab, I learned how to search files by name and size and execute commands on search results using the find command. This is a powerful tool for Linux system administration and file management.
