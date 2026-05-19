# Lab 1: Navigating the Filesystem

## Objectives
- Understand the basic structure of a filesystem.
- Learn how to determine the current working directory.
- Practice listing files and directories.
- Learn filesystem navigation commands.

---

# Prerequisites
- Basic understanding of CLI
- Linux or Unix-like operating system
- Terminal access

---

# Task 1.1: Using pwd Command

## Command
```bash
pwd
```

## Explanation
The `pwd` command stands for Print Working Directory.
It displays the absolute path of the current directory.

## Example Output
```bash
/home/ubuntu/AIOPS-Additional-Labs
```

---

# Task 2.1: Listing Files with ls Command

## Command
```bash
ls
```

## Explanation
The `ls` command lists files and directories in the current directory.

## Example Output
```bash
Documents Downloads Pictures
```

---

# Task 2.2: Listing with Options

## Command
```bash
ls -la
```

## Explanation
- `-l` shows detailed information.
- `-a` includes hidden files.

## Example Output
```bash
drwxr-xr-x  2 ubuntu ubuntu 4096 May 19 10:00 .
drwxr-xr-x 10 ubuntu ubuntu 4096 May 19 09:00 ..
-rw-r--r--  1 ubuntu ubuntu    0 May 19 10:00 README.md
```

---

# Task 3.1: Changing Directories

## Command
```bash
cd Documents
```

## Explanation
The `cd` command changes the current working directory.

---

# Task 3.2: Navigating to Parent Directory

## Command
```bash
cd ..
```

## Explanation
This command moves one directory level upward.

---

# Conclusion

In this lab, we learned:
- How to check the current directory using `pwd`
- How to list files using `ls`
- How to view hidden files using `ls -la`
- How to navigate directories using `cd`
- How to move to the parent directory using `cd ..`

These commands are fundamental for working in Linux environments.
