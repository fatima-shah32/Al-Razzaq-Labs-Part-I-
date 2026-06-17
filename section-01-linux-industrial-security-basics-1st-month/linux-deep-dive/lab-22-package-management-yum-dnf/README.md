# Lab 22: Package Management - YUM/DNF

## Objective

Learn basic package management using YUM and DNF on RPM-based Linux distributions.

---

## Task 1: Update Package Lists

### Update Packages

Using YUM:

```bash
sudo yum update
```

Using DNF:

```bash
sudo dnf update
```

Purpose:

Updates package information from repositories.

---

### Upgrade Packages

Using YUM:

```bash
sudo yum upgrade
```

Using DNF:

```bash
sudo dnf upgrade
```

Purpose:

Installs available package updates.

---

## Task 2: Search for a Package

Using YUM:

```bash
yum search vim
```

Using DNF:

```bash
dnf search vim
```

Example Output:

```text
vim-enhanced
vim-common
vim-filesystem
```

Purpose:

Searches repositories for packages matching the keyword.

---

## Task 3: Install a Package

Using YUM:

```bash
sudo yum install vim
```

Using DNF:

```bash
sudo dnf install vim
```

Verify Installation:

```bash
vim --version
```

Purpose:

Installs and verifies Vim editor.

---

## Task 4: Remove a Package

Using YUM:

```bash
sudo yum remove vim
```

Using DNF:

```bash
sudo dnf remove vim
```

Purpose:

Removes Vim package from the system.

---

## Summary

| Command | Purpose |
|----------|----------|
| yum update | Update package lists |
| dnf update | Update package lists |
| yum search vim | Search package |
| dnf search vim | Search package |
| yum install vim | Install package |
| dnf install vim | Install package |
| yum remove vim | Remove package |
| dnf remove vim | Remove package |

---

## Conclusion

In this lab, I learned how to update package repositories, search for software, install packages, and remove packages using YUM and DNF package managers on RPM-based Linux distributions.
um-dnf$ 
## Note

This lab requires an RPM-based Linux distribution such as CentOS, Fedora, or RHEL.

The current environment is Ubuntu, which uses APT package management instead of YUM/DNF.

Therefore, the commands below are documented for learning purposes and were not executed in this Ubuntu environment.

### Check Operating System

```bash
cat /etc/os-release
```

Output:

```text
NAME="Ubuntu"
VERSION="24.04 LTS"
ID=ubuntu
```
