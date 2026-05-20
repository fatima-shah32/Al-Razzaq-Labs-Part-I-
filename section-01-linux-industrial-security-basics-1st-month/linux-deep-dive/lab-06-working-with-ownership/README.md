# Lab 06 - Working with Ownership

## Objectives
- Learn file ownership in Linux
- Change ownership using chown
- Change group ownership using chgrp

---

# Task 1 - Check Ownership

## Create File

```bash
touch example.txt
```

## View Ownership

```bash
ls -l
```

## Example Output

```text
-rw-r--r-- 1 ubuntu ubuntu 0 example.txt
```

---

# Task 2 - Change File Owner

## Create User

```bash
sudo adduser newuser
```

## Change Ownership

```bash
sudo chown newuser example.txt
```

## Verify

```bash
ls -l
```

---

# Task 3 - Change Group Ownership

## Create Group

```bash
sudo groupadd newgroup
```

## Change Group

```bash
sudo chgrp newgroup example.txt
```

## Verify

```bash
ls -l
```

---

# Screenshots

## Initial Ownership
```text
screenshots/01-initial-ownership.png
```

## After chown
```text
screenshots/02-after-chown.png
```

## After chgrp
```text
screenshots/03-after-chgrp.png
```

---

# Outcome
Successfully learned:
- File ownership
- Group ownership
- chown command
- chgrp command
- Linux permission management

