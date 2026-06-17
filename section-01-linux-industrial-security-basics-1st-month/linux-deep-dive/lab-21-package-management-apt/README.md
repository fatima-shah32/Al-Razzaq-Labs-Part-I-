# Lab 21: Package Management - APT

## Objective
Learn how to manage packages on Ubuntu/Debian using APT.

---

## Step 1: Update Package Lists

Command:

```bash
sudo apt-get update
This command updates the local package list from Ubuntu repositories.

Expected output:

Reading package lists... Done
Step 2: Search for a Package

Command:

apt-cache search editor

This command searches for packages related to editors.

Example output:

vim - Vi IMproved text editor
nano - small, friendly text editor
Step 3: Install a Package

Command:

sudo apt-get install vim -y

This installs the Vim text editor.

Verify installation:

vim --version
Step 4: Remove a Package

Command:

sudo apt-get remove vim -y

This removes Vim from the system.

Verify removal:

vim

Expected output:

Command 'vim' not found
Summary
Command	Purpose
sudo apt-get update	Update package lists
apt-cache search editor	Search for packages
sudo apt-get install vim -y	Install Vim
sudo apt-get remove vim -y	Remove Vim
Conclusion

In this lab, I learned how to update package lists, search for packages, install software, and remove software using APT on a Debian-based Linux system.
