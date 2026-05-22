# Lab 54 - Using df and du

## Objectives
- Learn disk usage monitoring
- Use df and du commands
- Analyze filesystem storage
- Identify large files and folders

---

# Task 1 - Check Disk Space with df

## Command

```bash
df -h
```

## Explanation

| Option | Meaning |
|---|---|
| df | Disk free space |
| -h | Human-readable format |

## Example Output

```text
Filesystem      Size  Used Avail Use% Mounted on
/dev/root        20G  8.5G   11G  45% /
```

---

# Task 2 - Check Directory Usage with du

## Create Test Directory

```bash
mkdir test-directory
```

## Create Sample Files

```bash
fallocate -l 5M test-directory/file1.img
fallocate -l 10M test-directory/file2.img
```

## Check Usage

```bash
du -sh test-directory
```

## Example Output

```text
15M test-directory
```

---

# Task 3 - Identify Large Files

## Command

```bash
du -ah test-directory | sort -rh | head -n 10
```

## Example Output

```text
15M test-directory
10M test-directory/file2.img
5.0M test-directory/file1.img
```

---

# Screenshots

## df Command Output
```text
screenshots/01-df-command.png
```

## du Summary Output
```text
screenshots/02-du-summary.png
```

## Largest Files Output
```text
screenshots/03-largest-files.png
```

---

# Outcome
Successfully learned:
- Disk space monitoring
- Filesystem analysis
- Directory usage checking
- Finding large files in Linux
