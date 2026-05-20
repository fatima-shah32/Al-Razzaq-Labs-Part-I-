# Lab 05 - File Permissions Basics

## Objectives
- Learn Linux file permissions
- Check permissions using ls -l
- Modify permissions using chmod

---

# Task 1 - Check File Permissions

## Create File

```bash
touch example.txt
```

## View Permissions

```bash
ls -l
```

## Example Output

```text
-rw-r--r-- 1 ubuntu ubuntu 0 example.txt
```

---

# Task 2 - Modify Permissions

## Add Write Permission to Group

```bash
chmod g+w example.txt
```

## Verify Changes

```bash
ls -l
```

## Updated Output

```text
-rw-rw-r-- 1 ubuntu ubuntu 0 example.txt
```

---

# Task 3 - Numeric Permissions

## Apply Numeric Permissions

```bash
chmod 764 example.txt
```

## Verify

```bash
ls -l
```

## Output

```text
-rwxrw-r-- 1 ubuntu ubuntu 0 example.txt
```

---

# Permission Breakdown

| Number | Meaning |
|---|---|
| 7 | rwx |
| 6 | rw- |
| 4 | r-- |

---

# Screenshots

## Permissions Before chmod
```text
screenshots/01-before-chmod.png
```

## Permissions After chmod g+w
```text
screenshots/02-after-symbolic-permission.png
```

## Permissions After chmod 764
```text
screenshots/03-after-numeric-permission.png
```

---

# Outcome
Successfully learned:
- Linux file permissions
- chmod command
- Symbolic permissions
- Numeric permissions
