# Lab 45: Introduction to /etc/fstab

## Objective

Learn how Linux automatically mounts filesystems using the /etc/fstab file.

---

## Prerequisites

* Linux Operating System
* Terminal Access
* Sudo Privileges

---

## Task 1: View Existing fstab Entries

### Open fstab

```bash
sudo nano /etc/fstab
```

### Alternative View

```bash
cat /etc/fstab
```

### Purpose

Displays filesystems mounted during boot.

---

## Task 2: Understand fstab Syntax

### Example Entry

```text
/dev/sdb1 /media/usb ext4 defaults 0 2
```

### Fields

1. Device
2. Mount Point
3. Filesystem Type
4. Mount Options
5. Dump Value
6. fsck Order

---

## Task 3: Identify Available Devices

### List Block Devices

```bash
lsblk
```

### Detailed Information

```bash
sudo fdisk -l
```

---

## Task 4: Backup fstab

### Backup File

```bash
sudo cp /etc/fstab /etc/fstab.bak
```

### Verify

```bash
ls -l /etc/fstab*
```

---

## Task 5: Create Mount Point

```bash
sudo mkdir -p /media/usb
```

---

## Task 6: Example fstab Entry

```text
/dev/sdb1 /media/usb ext4 defaults 0 2
```

### Test Configuration

```bash
sudo mount -a
```

### Verify

```bash
df -h
```

---

## Summary

| Command        | Purpose            |
| -------------- | ------------------ |
| cat /etc/fstab | View fstab         |
| lsblk          | View disks         |
| fdisk -l       | Disk details       |
| cp             | Backup fstab       |
| mount -a       | Test configuration |
| df -h          | Verify mounts      |

---

## Conclusion

In this lab, I learned how Linux uses /etc/fstab to automate filesystem mounting and how to safely back up and test fstab configurations.
