# Lab 23: System Hardware Information

## Objective

Learn how to retrieve and interpret basic system hardware information using Linux commands.

---

## Prerequisites

- Linux Operating System
- Terminal Access
- Basic Linux Command Knowledge

---

## Task 1: Display CPU Information

### Command

```bash
lscpu
```

### Purpose

Displays detailed information about CPU architecture, cores, threads, cache, and vendor.

### Example Output

```text
Architecture:        x86_64
CPU(s):              2
Vendor ID:           GenuineIntel
```

### Key Concepts

- Architecture: Processor architecture.
- CPU(s): Number of available CPUs.
- Vendor ID: CPU manufacturer.

---

## Task 2: Check Memory Usage

### Command

```bash
free -h
```

### Purpose

Displays RAM and swap memory usage in human-readable format.

### Example Output

```text
               total        used        free
Mem:           3.8Gi       1.2Gi       1.8Gi
Swap:          0B          0B          0B
```

### Key Concepts

- Total: Installed memory.
- Used: Memory currently in use.
- Available: Memory available for applications.

---

## Task 3: View Disk Usage

### Command

```bash
df -h
```

### Purpose

Displays filesystem disk usage information.

### Example Output

```text
Filesystem      Size  Used Avail Use% Mounted on
/dev/root        20G  7.2G   13G  36% /
```

### Key Concepts

- Size: Total filesystem size.
- Used: Space currently used.
- Avail: Available space.
- Mounted on: Mount point.

---

## Conclusion

In this lab, I learned how to inspect CPU information, memory utilization, and disk usage using Linux commands. These commands are essential for system administration, troubleshooting, and performance monitoring.
