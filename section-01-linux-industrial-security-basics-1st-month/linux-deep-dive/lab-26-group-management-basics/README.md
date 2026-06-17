# Lab 26: Group Management Basics

## Objective

Understand the basics of Linux group management, including creating groups, adding users to groups, and removing users from groups.

---

## Task 1: Create a New Group

### Create Group

```bash
sudo groupadd developers
Verify Group Creation
grep developers /etc/group

Example Output:

developers:x:1002:
Task 2: Add a User to a Group
Add User to Group
sudo usermod -aG developers alice
Verify Group Membership
groups alice

Example Output:

alice : alice developers
Task 3: Remove User from Group
Remove User
sudo gpasswd -d alice developers
Verify Removal
groups alice

Example Output:

alice : alice
Summary
Command	Purpose
sudo groupadd developers	Create group
grep developers /etc/group	Verify group
sudo usermod -aG developers alice	Add user to group
groups alice	Check membership
sudo gpasswd -d alice developers	Remove user from group
Conclusion

In this lab, I learned how to create Linux groups, add users to groups, verify group membership, and remove users from groups. Proper group management is essential for controlling access to system resources and maintaining security.
