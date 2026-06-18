# Lab 48: Command Chaining

## Objective

Learn how to execute multiple Linux commands using command chaining operators such as &&, ||, and ;.

---

## Prerequisites

* Linux Operating System
* Terminal Access
* Basic Linux Commands

---

## Task 1: Using && Operator

### Successful Commands

```bash
mkdir new_directory && cd new_directory
```

### Explanation

The second command executes only if the first command succeeds.

### Example with Failure

```bash
echo "Hello World" && cd non_existent_directory
```

---

## Task 2: Using || Operator

### Command

```bash
cd non_existent_directory || echo "Directory does not exist"
```

### Explanation

The second command executes only if the first command fails.

---

## Task 3: Using ; Operator

### Command

```bash
echo "This will always print"; cd non_existent_directory; echo "This prints anyway"
```

### Explanation

All commands execute regardless of success or failure.

---

## Case Study

```bash
mkdir backup || echo "Backup directory already exists" && cp important_file.txt backup/
```

### Explanation

Attempts to create a backup directory and copies files if successful.

---

## Summary

| Operator | Purpose                               |   |                                    |
| -------- | ------------------------------------- | - | ---------------------------------- |
| &&       | Run next command if previous succeeds |   |                                    |
|          |                                       |   | Run next command if previous fails |
| ;        | Run all commands sequentially         |   |                                    |

---

## Conclusion

In this lab, I learned how Linux command chaining works using &&, ||, and ; operators. These techniques are useful for automation, scripting, and efficient command-line operations.
