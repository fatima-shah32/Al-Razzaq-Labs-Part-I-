# Lab 42: Mounting and Unmounting

## Objective

Learn how to create mount points, mount filesystems, and unmount them safely in Linux.

---

## Prerequisites

* Linux Operating System
* Terminal Access
* Sudo Privileges

---

## Task 1: Create a Mount Point

### Create Directory

```bash
sudo mkdir /mnt/my_mount
```

### Verify

```bash
ls -ld /mnt/my_mount
```

---

## Task 2: Identify Available Devices

### List Block Devices

```bash
lsblk
```

### Detailed Information

```bash
sudo fdisk -l
```

---

## Task 3: Mount a Filesystem

### Example Command

```bash
sudo mount /dev/sdb1 /mnt/my_mount
```

### Verify Mount

```bash
mount | grep my_mount
```

or

```bash
df -h
```

---

## Task 4: Unmount Filesystem

### Unmount

```bash
sudo umount /mnt/my_mount
```

### Verify

```bash
mount | grep my_mount
```

---

## Summary

| Command | Purpose            |
| ------- | ------------------ |
| mkdir   | Create mount point |
| lsblk   | View disks         |
| mount   | Attach filesystem  |
| umount  | Detach filesystem  |
| df -h   | Verify mount       |

---

## Conclusion

In this lab, I learned how Linux mounts filesystems to directories and how to safely unmount them when no longer needed.
