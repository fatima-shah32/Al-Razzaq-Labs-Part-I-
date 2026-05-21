# 🧪 Lab 59: Monitoring with top and htop

## 📌 Overview
This lab demonstrates how to monitor Linux system processes and resource utilization using the \`top\` and \`htop\` utilities. The lab covers installation, process monitoring, sorting processes by CPU and memory usage, and comparing the interfaces of both tools.

---

# 🎯 Objectives

- Understand the importance of system monitoring tools
- Install and configure \`htop\`
- Monitor active processes using \`top\` and \`htop\`
- Sort processes by CPU and memory usage
- Compare traditional and interactive monitoring interfaces

---

# 🛠️ Prerequisites

Before starting this lab, ensure you have:

- A Linux-based operating system
- Terminal access
- Basic Linux command-line knowledge
- Sudo/root privileges
- Internet connectivity for package installation

---

# 📂 Lab Environment

| Component | Details |
|---|---|
| Operating System | Ubuntu Linux |
| Shell | Bash |
| Monitoring Tools | top, htop |
| User Privileges | sudo/root |

---

# 📋 Lab Tasks

## 🔹 Task 1: Install htop

### Update Package Manager

#### Ubuntu/Debian
\`\`\`bash
sudo apt update
\`\`\`

#### CentOS/RHEL
\`\`\`bash
sudo yum check-update
\`\`\`

---

### Install htop

#### Ubuntu/Debian
\`\`\`bash
sudo apt install htop -y
\`\`\`

#### CentOS/RHEL
\`\`\`bash
sudo yum install htop -y
\`\`\`

### Explanation
The \`htop\` package is installed using the system package manager. \`htop\` provides an interactive and user-friendly interface for monitoring system performance and processes.

---

## 🔹 Task 2: Run top Command

### Execute top
\`\`\`bash
top
\`\`\`

### Key Observations
- CPU usage statistics
- Memory consumption
- Running processes
- System uptime and load average

---

### Sort Processes by CPU Usage
Press:
\`\`\`bash
P
\`\`\`

### Sort Processes by Memory Usage
Press:
\`\`\`bash
M
\`\`\`

### Exit top
Press:
\`\`\`bash
q
\`\`\`

---

## 🔹 Task 3: Run htop Command

### Execute htop
\`\`\`bash
htop
\`\`\`

### Key Features
- Interactive process management
- Color-coded CPU and memory usage
- Easier navigation using arrow keys
- Better readability than top

---

## 🔹 Task 4: Sort Processes in htop

### Sort by CPU Usage
Press:
\`\`\`bash
F6
\`\`\`

Select:
\`\`\`bash
CPU%
\`\`\`

Press:
\`\`\`bash
Enter
\`\`\`

---

### Sort by Memory Usage
Press:
\`\`\`bash
F6
\`\`\`

Select:
\`\`\`bash
MEM%
\`\`\`

Press:
\`\`\`bash
Enter
\`\`\`

---

### Exit htop
Press:
\`\`\`bash
q
\`\`\`

---

# 📊 Key Concepts Learned

- Process monitoring in Linux
- CPU and memory utilization analysis
- Real-time system performance monitoring
- Interactive process management
- Resource troubleshooting techniques

---

# 📸 Screenshots

| Screenshot | Description |
|---|---|
| screenshot1_htop_installation.png | htop installation process |
| screenshot2_top_command.png | top command monitoring interface |
| screenshot3_htop_interface.png | htop interactive monitoring interface |

---

# ✅ Verification

The lab was successfully completed by:

- Installing htop successfully
- Running both top and htop commands
- Sorting processes by CPU and memory usage
- Comparing monitoring interfaces
- Exiting utilities properly

---

# 🧠 Troubleshooting Notes

| Issue | Solution |
|---|---|
| htop command not found | Install using \`sudo apt install htop -y\` |
| Permission denied | Use sudo privileges |
| Unable to exit utility | Press \`q\` |
| Package installation failed | Run \`sudo apt update\` first |

---

# 📚 Commands Summary

| Command | Purpose |
|---|---|
| \`top\` | Display running processes |
| \`htop\` | Interactive process viewer |
| \`P\` | Sort by CPU usage in top |
| \`M\` | Sort by memory usage in top |
| \`F6\` | Change sorting order in htop |
| \`q\` | Exit monitoring utility |

---

# 🏁 Conclusion

This lab provided practical experience using Linux monitoring tools such as \`top\` and \`htop\`. These utilities are essential for system administrators to monitor performance, identify resource-heavy processes, and troubleshoot system-related issues efficiently. The interactive features of \`htop\` make process management significantly easier compared to traditional monitoring tools.

---

# 👩‍💻 Author

**Fatima Danyal**  
Linux & DevOps Labs Repository

