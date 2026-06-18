# Lab 50: Introduction to Shell Variables

## Objective

Learn how to create and use local variables, global variables, and special shell variables in Bash.

---

## Prerequisites

* Linux Operating System
* Bash Shell
* Terminal Access

---

## Task 1: Working with Local Variables

### Create Local Variable

```bash
MYVAR="HelloWorld"
```

### Display Variable

```bash
echo $MYVAR
```

### Expected Output

```text
HelloWorld
```

---

## Task 2: Working with Global Variables

### Create Global Variable

```bash
export MYVAR2="GlobalHello"
```

### Access in Subshell

```bash
bash -c 'echo $MYVAR2'
```

### Expected Output

```text
GlobalHello
```

---

## Task 3: Using Special Variables

### Exit Status Variable

```bash
echo $?
```

### Current Shell PID

```bash
echo $$
```

### Number of Arguments

```bash
bash -c 'echo $#'
```

### Expected Output

```text
0
```

---

## Summary

| Variable | Purpose                    |
| -------- | -------------------------- |
| $MYVAR   | User-defined variable      |
| $MYVAR2  | Exported global variable   |
| $?       | Last command exit status   |
| $$       | Current shell PID          |
| $#       | Number of script arguments |

---

## Conclusion

In this lab, I learned how Bash variables work, including local variables, exported global variables, and special shell variables used in shell scripting and automation.
