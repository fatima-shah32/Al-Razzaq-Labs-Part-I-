# Lab 27: Password Policies

## Objective

Understand password policies, password expiry settings, and password complexity requirements in Linux.

---

## Prerequisites

* Linux Operating System
* Terminal Access
* Sudo Privileges

---

## Task 1: Check Current Password Policy

### Command

```bash
chage -l ubuntu
```

### Purpose

Displays password aging and expiry information for a user.

---

## Task 2: Modify Password Expiry Policy

### Command

```bash
sudo chage -M 60 -W 7 ubuntu
```

### Explanation

* M 60 = Password expires after 60 days
* W 7 = Warning displayed 7 days before expiry

### Verify Changes

```bash
chage -l ubuntu
```

---

## Task 3: Configure Password Policy

### Open Configuration File

```bash
sudo nano /etc/login.defs
```

### Recommended Settings

```text
PASS_MIN_LEN 8
PASS_MAX_DAYS 90
```

### Purpose

* PASS_MIN_LEN = Minimum password length
* PASS_MAX_DAYS = Maximum password age

---

## Optional PAM Configuration

File:

```bash
sudo nano /etc/pam.d/common-password
```

Example:

```text
password requisite pam_pwquality.so retry=3 minlen=8
```

Purpose:

Enforces password complexity requirements.

---

## Summary

| Command                              | Purpose                       |
| ------------------------------------ | ----------------------------- |
| chage -l username                    | View password policy          |
| sudo chage -M 60 -W 7 username       | Set password expiry           |
| sudo nano /etc/login.defs            | Configure password rules      |
| sudo nano /etc/pam.d/common-password | Configure password complexity |

---

## Conclusion

In this lab, I learned how to view and modify password expiry settings and understand password complexity requirements. These controls help improve Linux system security and protect user accounts from unauthorized access.
