# Lab 30: SSH Basics

## Objective

Learn how to generate SSH keys, copy public keys to a remote server, and configure passwordless SSH authentication.

---

## Prerequisites

* Linux Operating System
* Terminal Access
* SSH Installed
* Access to a Remote Server

---

## Task 1: Generate SSH Keys

### Generate RSA Key Pair

```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

### Explanation

* t rsa = RSA key type
* b 4096 = 4096-bit key length
* C = Comment for identification

### Default Location

```text
~/.ssh/id_rsa
~/.ssh/id_rsa.pub
```

---

## Task 2: Copy Public Key to Remote Host

### Method 1: Using ssh-copy-id

```bash
ssh-copy-id username@remote_host
```

### Method 2: Manual Copy

Display public key:

```bash
cat ~/.ssh/id_rsa.pub
```

Connect to remote host:

```bash
ssh username@remote_host
```

Create SSH directory:

```bash
mkdir -p ~/.ssh
```

Add public key:

```bash
echo "public_key_contents" >> ~/.ssh/authorized_keys
```

---

## Task 3: Verify Passwordless SSH

Connect using SSH:

```bash
ssh username@remote_host
```

List files:

```bash
ls -la
```

Successful login without password confirms SSH key authentication is working.

---

## Summary

| Command               | Purpose            |
| --------------------- | ------------------ |
| ssh-keygen            | Generate SSH keys  |
| ssh-copy-id           | Copy key to server |
| cat ~/.ssh/id_rsa.pub | View public key    |
| ssh user@host         | Connect to server  |
| ls -la                | Verify access      |

---

## Conclusion

In this lab, I learned how to generate SSH key pairs, transfer public keys to remote systems, and configure passwordless authentication using SSH. This improves security and simplifies server administration.
