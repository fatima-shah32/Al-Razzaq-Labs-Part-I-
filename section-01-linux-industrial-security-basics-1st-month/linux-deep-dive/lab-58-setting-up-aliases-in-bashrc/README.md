# 🧪 Lab 58: Setting Up Aliases in .bashrc

## 📌 Overview

This lab demonstrates how to create and manage persistent command aliases using the `.bashrc` configuration file in Linux. Aliases improve productivity by simplifying frequently used commands into shorter, reusable shortcuts.

---

# 🎯 Objectives

- Understand Linux aliases and their purpose
- Edit the `.bashrc` configuration file
- Create persistent custom aliases
- Reload shell configuration using `source`
- Verify alias persistence across terminal sessions

---

# 🛠️ Prerequisites

Before starting this lab, ensure you have:

- A Linux-based operating system
- Terminal access
- Basic Linux command-line knowledge
- Access to a text editor such as nano or vim

---

# 📂 Lab Environment

| Component | Details |
|---|---|
| Operating System | Ubuntu Linux |
| Shell | Bash |
| Configuration File | .bashrc |
| Text Editor | nano |

---

# 📋 Lab Tasks

## 🔹 Task 1: Locate the .bashrc File

### Navigate to Home Directory
```bash
cd ~
List Hidden Files
ls -a
Explanation

The .bashrc file is a hidden shell configuration file located in the user's home directory.

🔹 Task 2: Open .bashrc File
Open with nano
nano ~/.bashrc
Explanation

The nano text editor is used to modify the shell configuration file.

🔹 Task 3: Add a New Alias
Add Alias
alias update='sudo apt-get update && sudo apt-get upgrade -y'
Explanation

This alias creates a shortcut command named update to automate system updates and upgrades.

🔹 Task 4: Reload Shell Configuration
Source the .bashrc File
source ~/.bashrc
Explanation

The source command reloads shell configurations without restarting the terminal session.

🔹 Task 5: Verify Alias
Run Alias
update
Check Alias
alias update
Explanation

The alias should successfully execute the system update and upgrade commands.

📊 Key Concepts Learned
Linux aliases
Shell configuration files
Persistent shell customization
Command-line productivity enhancement
Bash shell environment management
📸 Screenshots
Screenshot	Description
screenshot1_bashrc_file.png	Viewing hidden files including .bashrc
screenshot2_alias_added.png	Alias added inside .bashrc
screenshot3_alias_verification.png	Alias verification and execution
✅ Verification

The lab was successfully completed by:

Locating the .bashrc file
Adding a custom alias
Reloading shell configuration
Executing and verifying the alias
Confirming alias persistence across sessions
🧠 Troubleshooting Notes
Issue	Solution
Alias not working	Run source ~/.bashrc
Permission denied	Use proper user permissions
Command not found	Verify alias syntax
.bashrc missing	Create file using touch ~/.bashrc
📚 Commands Summary
Command	Purpose
ls -a	Show hidden files
nano ~/.bashrc	Open .bashrc file
alias	Create or list aliases
source ~/.bashrc	Reload shell configuration
update	Execute custom alias
🏁 Conclusion

This lab provided practical experience with Linux shell aliases and .bashrc configuration management. Persistent aliases improve command-line efficiency by reducing repetitive typing and automating commonly used commands. Understanding shell customization is an important skill for Linux system administration and DevOps workflows.

👩‍💻 Author

Fatima Danyal
Linux & DevOps Labs Repository
