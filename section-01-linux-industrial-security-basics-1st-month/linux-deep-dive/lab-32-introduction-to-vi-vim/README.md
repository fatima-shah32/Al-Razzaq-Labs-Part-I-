# Lab 32: Introduction to vi/vim

## Objective

Learn the basic functionality of the vi/vim editor, including file creation, editing, navigation, searching, and replacing text.

---

## Prerequisites

* Linux Operating System
* Terminal Access
* Basic Command Line Knowledge

---

## Task 1: Open a File with vi

### Create File

```bash
touch file.txt
```

### Open File

```bash
vi file.txt
```

### Purpose

Opens an existing file or creates a new file for editing.

---

## Task 2: Enter Insert Mode and Add Text

### Enter Insert Mode

Press:

```text
i
```

### Example Text

```text
Hello World
This is a vi editor lab.
Linux administration is fun.
```

### Save File

Press:

```text
Esc
```

Then type:

```vim
:w
```

### Exit vi

```vim
:q
```

Or save and quit:

```vim
:wq
```

---

## Task 3: Practice Navigation

### Navigation Keys

| Key | Action     |
| --- | ---------- |
| h   | Move Left  |
| j   | Move Down  |
| k   | Move Up    |
| l   | Move Right |

---

## Search Text

Press:

```vim
/example
```

Press Enter.

---

## Replace Text

Replace all occurrences of old with new:

```vim
:%s/old/new/g
```

Example:

```vim
:%s/Linux/Ubuntu/g
```

---

## Summary

| Command       | Purpose       |
| ------------- | ------------- |
| vi file.txt   | Open file     |
| i             | Insert mode   |
| Esc           | Normal mode   |
| :w            | Save          |
| :q            | Quit          |
| :wq           | Save and quit |
| /text         | Search text   |
| :%s/old/new/g | Replace text  |

---

## Conclusion

In this lab, I learned how to create files, edit text, navigate within files, search for text, and perform replacements using the vi/vim editor. These skills are essential for Linux system administration and configuration management.
