# Lab 34: sed for Text Manipulation

## Objective

Learn how to use the sed command for text replacement and deletion in Linux.

---

## Prerequisites

* Linux Operating System
* Terminal Access
* Basic Command Line Knowledge

---

## Task 1: Replace a Word in a File

### Create Sample File

```bash
echo -e "Hello World\nHello Universe\nGoodbye World" > example.txt
```

### View File

```bash
cat example.txt
```

### Replace Text

```bash
sed 's/World/Earth/g' example.txt
```

### Output

```text
Hello Earth
Hello Universe
Goodbye Earth
```

### Save Changes

```bash
sed -i 's/World/Earth/g' example.txt
```

---

## Task 2: Remove Lines Matching a Pattern

### Delete Lines Containing Universe

```bash
sed '/Universe/d' example.txt
```

### Output

```text
Hello Earth
Goodbye Earth
```

### Save Changes

```bash
sed -i '/Universe/d' example.txt
```

---

## Summary

| Command                   | Purpose               |
| ------------------------- | --------------------- |
| sed 's/old/new/g' file    | Replace text          |
| sed -i 's/old/new/g' file | Replace and save      |
| sed '/pattern/d' file     | Delete matching lines |
| sed -i '/pattern/d' file  | Delete and save       |

---

## Conclusion

In this lab, I learned how to use sed for text manipulation, including replacing words and deleting lines matching a specific pattern. These operations are useful for automating file editing tasks in Linux.
