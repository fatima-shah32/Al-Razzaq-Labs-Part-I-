# Lab 33: Basic Grep Usage

## Objective

Learn how to search text within files and directories using the grep command.

---

## Prerequisites

* Linux Operating System
* Terminal Access
* Basic Command Line Knowledge

---

## Task 1: Search for a String in a Single File

### Create Sample File

```bash
echo -e "network error at node 3\noperation successful at node 5\nnetwork connection established\nunexpected error at node 7" > sample.txt
```

### Search for a String

```bash
grep "error" sample.txt
```

### Expected Output

```text
network error at node 3
unexpected error at node 7
```

---

## Task 2: Search Recursively in Directories

### Command

```bash
grep -r "error" .
```

### Purpose

Searches all files and subdirectories for the specified string.

---

## Task 3: Display Context Lines

### Command

```bash
grep -A 2 -B 2 "error" sample.txt
```

### Explanation

* A 2 = Show 2 lines after match
* B 2 = Show 2 lines before match

---

## Summary

| Command                    | Purpose                 |
| -------------------------- | ----------------------- |
| grep "text" file           | Search text in file     |
| grep -r "text" directory   | Recursive search        |
| grep -A 2 "text" file      | Show lines after match  |
| grep -B 2 "text" file      | Show lines before match |
| grep -A 2 -B 2 "text" file | Show context            |

---

## Conclusion

In this lab, I learned how to use grep for searching text within files and directories. I also learned recursive searching and displaying context around matching lines, which are essential skills for Linux administration and troubleshooting.
