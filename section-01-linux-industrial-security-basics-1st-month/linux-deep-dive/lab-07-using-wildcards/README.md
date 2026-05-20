# Lab 07 - Using Wildcards

## Objectives
- Learn wildcard usage in Linux
- Practice pattern matching
- Use cp and rm with wildcards

---

# Task 1 - Copy Files Using *

## Create Files

```bash
touch file1.txt file2.txt report1.txt report2.txt
```

## Create Backup Directory

```bash
mkdir backup
```

## Copy All Text Files

```bash
cp *.txt backup/
```

## Verify Backup

```bash
cd backup
ls
```

## Output

```text
file1.txt
file2.txt
report1.txt
report2.txt
```

---

# Task 2 - Remove Files Using ?

## Return to Main Directory

```bash
cd ..
```

## Remove Selected Files

```bash
rm file?.txt
```

## Verify Remaining Files

```bash
ls
```

## Output

```text
backup
report1.txt
report2.txt
```

---

# Wildcard Explanation

| Wildcard | Meaning |
|---|---|
| * | Any number of characters |
| ? | Exactly one character |

---

# Screenshots

## Files Before Copy
```text
screenshots/01-files-created.png
```

## Backup Directory Content
```text
screenshots/02-backup-files.png
```

## Remaining Files After rm
```text
screenshots/03-after-removal.png
```

---

# Outcome
Successfully learned:
- Wildcard usage
- Pattern matching
- File copy using *
- File deletion using ?
