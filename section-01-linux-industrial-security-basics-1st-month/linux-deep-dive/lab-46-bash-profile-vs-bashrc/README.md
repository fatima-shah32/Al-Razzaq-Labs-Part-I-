# Lab 46: Bash Profile vs. Bashrc

## Objective

Understand the differences between .bash_profile and .bashrc and learn how to customize the Linux shell using aliases and environment variables.

---

## Prerequisites

* Linux Operating System
* Terminal Access
* Text Editor (nano/vim)

---

## Task 1: Examine .bash_profile and .bashrc

### Go to Home Directory

```bash
cd ~
```

### List Hidden Files

```bash
ls -a
```

### View .bash_profile

```bash
cat ~/.bash_profile
```

### View .bashrc

```bash
cat ~/.bashrc
```

### Purpose

* `.bash_profile` runs for login shells.
* `.bashrc` runs for interactive non-login shells.

---

## Task 2: Backup Configuration Files

### Backup .bashrc

```bash
cp ~/.bashrc ~/.bashrc.backup
```

### Backup .bash_profile

```bash
cp ~/.bash_profile ~/.bash_profile.backup
```

---

## Task 3: Add Alias

### Edit .bashrc

```bash
nano ~/.bashrc
```

### Add

```bash
alias ll='ls -la'
```

---

## Task 4: Add Environment Variable

### Add Below Alias

```bash
export MY_VAR="Hello World!"
```

---

## Task 5: Reload Configuration

```bash
source ~/.bashrc
```

### Verify Alias

```bash
ll
```

### Verify Variable

```bash
echo $MY_VAR
```

Expected:

```text
Hello World!
```

---

## Summary

| Command           | Purpose           |
| ----------------- | ----------------- |
| ls -a             | Show hidden files |
| source ~/.bashrc  | Reload bashrc     |
| alias ll='ls -la' | Create alias      |
| export VAR=value  | Create variable   |
| echo $VAR         | Display variable  |

---

## Conclusion

In this lab, I learned the difference between .bash_profile and .bashrc and how to customize my shell environment using aliases and environment variables.
