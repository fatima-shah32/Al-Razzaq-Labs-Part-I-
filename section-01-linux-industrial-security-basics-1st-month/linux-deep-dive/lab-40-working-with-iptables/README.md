# Lab 40: Working with iptables

## Objective

Learn how to list firewall rules, add rules to allow or block ports, and save iptables configurations.

---

## Prerequisites

* Linux Operating System
* Terminal Access
* Sudo Privileges
* iptables Installed

---

## Task 1: List Existing Rules

### Command

```bash
sudo iptables -L
```

### Purpose

Displays all active firewall rules.

---

## Task 2: Allow a Port

### Allow HTTP Port 80

```bash
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
```

### Purpose

Allows incoming HTTP traffic.

---

## Task 3: Block a Port

### Block HTTP Port 80

```bash
sudo iptables -A INPUT -p tcp --dport 80 -j DROP
```

### Purpose

Blocks incoming HTTP traffic.

---

## Task 4: Save Rules

### Save Configuration

```bash
sudo iptables-save > rules.v4
```

### View Saved Rules

```bash
cat rules.v4
```

---

## Summary

| Command                                            | Purpose    |
| -------------------------------------------------- | ---------- |
| sudo iptables -L                                   | List rules |
| sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT | Allow port |
| sudo iptables -A INPUT -p tcp --dport 80 -j DROP   | Block port |
| sudo iptables-save                                 | Save rules |

---

## Conclusion

In this lab, I learned how to inspect firewall rules, allow and block ports, and save iptables configurations for future use.
