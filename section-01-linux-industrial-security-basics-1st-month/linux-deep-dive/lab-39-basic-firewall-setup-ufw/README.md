# Lab 39: Basic Firewall Setup (UFW)

## Objective

Learn how to install, configure, and manage a firewall using UFW (Uncomplicated Firewall).

---

## Prerequisites

* Ubuntu Linux System
* Sudo Privileges
* Terminal Access

---

## Task 1: Install UFW

### Update Packages

```bash
sudo apt update
```

### Install UFW

```bash
sudo apt install ufw -y
```

### Verify Installation

```bash
ufw version
```

---

## Task 2: Enable UFW

### Allow SSH First

```bash
sudo ufw allow ssh
```

### Enable Firewall

```bash
sudo ufw enable
```

### Verify Status

```bash
sudo ufw status
```

---

## Task 3: Configure Firewall Rules

### Allow SSH

```bash
sudo ufw allow ssh
```

### Allow HTTP

```bash
sudo ufw allow http
```

### Allow HTTPS

```bash
sudo ufw allow https
```

---

## Task 4: Check Firewall Rules

### Basic Status

```bash
sudo ufw status
```

### Detailed Status

```bash
sudo ufw status verbose
```

---

## Task 5: Test Rules

### Temporarily Block SSH

```bash
sudo ufw deny ssh
```

### Re-Allow SSH

```bash
sudo ufw allow ssh
```

---

## Summary

| Command                 | Purpose             |
| ----------------------- | ------------------- |
| sudo apt install ufw    | Install UFW         |
| sudo ufw enable         | Enable firewall     |
| sudo ufw allow ssh      | Allow SSH           |
| sudo ufw allow http     | Allow HTTP          |
| sudo ufw allow https    | Allow HTTPS         |
| sudo ufw status         | Show firewall rules |
| sudo ufw status verbose | Detailed status     |

---

## Conclusion

In this lab, I learned how to install, enable, and configure UFW firewall rules. Proper firewall configuration is critical for protecting Linux servers from unauthorized access.
