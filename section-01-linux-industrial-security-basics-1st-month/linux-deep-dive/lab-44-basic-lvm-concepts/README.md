# Lab 44: Basic LVM Concepts

## Objective

Learn the fundamentals of Linux Logical Volume Manager (LVM), including Physical Volumes, Volume Groups, and Logical Volumes.

---

## Prerequisites

* Linux Operating System
* Terminal Access
* Sudo Privileges
* Additional Disk for LVM Testing

---

## Task 1: Check Existing LVM Configuration

### Display Logical Volumes

```bash
sudo lvdisplay
```

### Display Volume Groups

```bash
sudo vgdisplay
```

### Display Physical Volumes

```bash
sudo pvdisplay
```

---

## Task 2: Create LVM Storage (Theory)

### Create Physical Volume

```bash
sudo pvcreate /dev/sdb
```

### Create Volume Group

```bash
sudo vgcreate myvg /dev/sdb
```

### Create Logical Volume

```bash
sudo lvcreate -L 1G -n mylv myvg
```

---

## Task 3: Format and Mount

### Create Filesystem

```bash
sudo mkfs.ext4 /dev/myvg/mylv
```

### Create Mount Point

```bash
sudo mkdir /mnt/mylv
```

### Mount Logical Volume

```bash
sudo mount /dev/myvg/mylv /mnt/mylv
```

### Verify

```bash
df -h
```

---

## Task 4: Remove LVM Configuration

### Unmount

```bash
sudo umount /mnt/mylv
```

### Remove Logical Volume

```bash
sudo lvremove /dev/myvg/mylv
```

### Remove Volume Group

```bash
sudo vgremove myvg
```

### Remove Physical Volume

```bash
sudo pvremove /dev/sdb
```

---

## Summary

| Command   | Purpose                |
| --------- | ---------------------- |
| pvcreate  | Create physical volume |
| vgcreate  | Create volume group    |
| lvcreate  | Create logical volume  |
| lvdisplay | View logical volumes   |
| vgdisplay | View volume groups     |
| pvdisplay | View physical volumes  |

---

## Conclusion

In this lab, I learned the basic architecture of LVM and how physical volumes, volume groups, and logical volumes work together to provide flexible storage management.
