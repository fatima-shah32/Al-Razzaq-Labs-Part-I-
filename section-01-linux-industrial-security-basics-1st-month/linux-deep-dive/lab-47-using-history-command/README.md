# Lab 47: Using the history Command

## Objective

Learn how to view command history, re-run previous commands using history numbers, and clear command history.

---

## Prerequisites

* Linux Operating System
* Terminal Access

---

## Task 1: View Command History

### Command

```bash
history
```

### Purpose

Displays previously executed commands along with their history numbers.

---

## Task 2: Re-run a Command

### Example

If command number 25 is:

```bash
ls -la
```

Execute:

```bash
!25
```

### Purpose

Runs the command associated with history entry 25.

---

## Task 3: Clear History

### Command

```bash
history -c
```

### Verify

```bash
history
```

### Purpose

Clears the command history of the current shell session.

---

## Summary

| Command    | Purpose              |
| ---------- | -------------------- |
| history    | Show command history |
| !number    | Re-run command       |
| history -c | Clear history        |

---

## Conclusion

In this lab, I learned how to use the history command to review previously executed commands, quickly rerun commands, and clear command history when needed.
