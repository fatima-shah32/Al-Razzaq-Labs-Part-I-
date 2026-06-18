# Lab 41: Basic Disk Partitioning

## Objective

Learn how to inspect disks and partitions and understand the process of creating and deleting partitions using Linux partitioning tools.

---

## Prerequisites

* Linux Operating System
* Terminal Access
* Sudo Privileges

---

## Task 1: List Available Disks and Partitions

### List Block Devices

```bash
lsblk
```

### Detailed Disk Information

```bash
sudo fdisk -l
```

### Purpose

Displays disks, partitions, filesystem types, and storage sizes.

---

## Task 2: Create a Partition (Theory)

### Open cfdisk

```bash
sudo cfdisk /dev/sda
```

### Steps

1. Select Free Space
2. Choose New
3. Enter Size (500M)
4. Select Linux Partition Type
5. Write Changes
6. Exit

---

## Task 3: Delete a Partition (Theory)

### Open cfdisk

```bash
sudo cfdisk /dev/sda
```

### Steps

1. Select Existing Partition
2. Choose Delete
3. Write Changes
4. Exit

---

## Summary

| Command              | Purpose                        |
| -------------------- | ------------------------------ |
| lsblk                | View disks and partitions      |
| sudo fdisk -l        | Detailed partition information |
| sudo cfdisk /dev/sda | Partition editor               |

---

## Conclusion

In this lab, I learned how Linux disks and partitions are organized and how tools such as lsblk, fdisk, and cfdisk can be used to inspect and manage storage devices.
