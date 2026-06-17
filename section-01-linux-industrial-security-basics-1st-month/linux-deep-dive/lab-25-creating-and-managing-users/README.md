# Lab 25: Creating and Managing Users

## Objective

Learn how to create, manage, and delete user accounts in Linux using user management commands.

---

## Prerequisites

* Linux Operating System
* Terminal Access
* Sudo Privileges

---

## Task 1: Create a New User

### Command

```bash
sudo useradd newuser
```

### Verify User Creation

```bash
id newuser
```

### Purpose

Creates a new user account and adds an entry to the system user database.

---

## Task 2: Set a Password

### Command

```bash
sudo passwd newuser
```

### Purpose

Assigns a password to the newly created user.

---

## Task 3: Delete a User

### Remove User Only

```bash
sudo userdel newuser
```

### Remove User and Home Directory

```bash
sudo userdel -r newuser
```

### Purpose

Removes the user account from the system.

---

## Summary

| Command                 | Purpose                        |
| ----------------------- | ------------------------------ |
| sudo useradd newuser    | Create user                    |
| id newuser              | Verify user                    |
| sudo passwd newuser     | Set password                   |
| sudo userdel newuser    | Delete user                    |
| sudo userdel -r newuser | Delete user and home directory |

---

## Conclusion

In this lab, I learned how to create user accounts, assign passwords, verify user information, and remove users from a Linux system. These skills are essential for Linux system administration and user management.
