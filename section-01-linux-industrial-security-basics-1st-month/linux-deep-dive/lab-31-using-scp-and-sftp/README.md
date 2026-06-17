# Lab 31: Using SCP and SFTP

## Objective

Learn how to securely transfer files using SCP and SFTP and verify file integrity using SHA-256 hashes.

---

## Prerequisites

* Linux Operating System
* SSH Installed
* Access to a Remote Server
* Terminal Access

---

## Task 1: Securely Copy Files with SCP

### Copy Local File to Remote Server

```bash
scp example.txt username@remote_host:/remote/directory/
```

### Copy Remote File to Local System

```bash
scp username@remote_host:/remote/directory/example.txt /local/directory/
```

### Purpose

Securely transfer files using SSH encryption.

---

## Task 2: Transfer Files Using SFTP

### Connect to Remote Server

```bash
sftp username@remote_host
```

### Upload File

```bash
put example.txt
```

### Download File

```bash
get example.txt
```

### Exit Session

```bash
exit
```

### Purpose

Securely upload and download files using an interactive session.

---

## Task 3: Verify File Integrity

### Generate Original File Hash

```bash
sha256sum example.txt
```

### Generate Hash of Copied File

```bash
sha256sum copied_example.txt
```

### Compare Hashes

Matching hashes confirm file integrity after transfer.

---

## Summary

| Command                 | Purpose                |
| ----------------------- | ---------------------- |
| scp file user@host:path | Upload file            |
| scp user@host:file path | Download file          |
| sftp user@host          | Start SFTP session     |
| put file                | Upload file via SFTP   |
| get file                | Download file via SFTP |
| sha256sum file          | Verify integrity       |

---

## Conclusion

In this lab, I learned how to transfer files securely using SCP and SFTP and verify file integrity using SHA-256 hashing. These tools are essential for secure system administration and file management.
