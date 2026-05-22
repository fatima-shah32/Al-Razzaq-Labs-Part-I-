# 📘 Lab 51: Basic Regex with grep

## 🎯 Objective
Learn basic Regular Expressions (Regex) using the `grep` command in Linux.

---

## 📂 Task 1: Search Lines Starting with a Pattern

### Create file
```bash
nano example.txt
Add content
apple
banana
cherry
apricot
grapefruit
Command
grep '^a' example.txt
Explanation
^ → matches start of line
Output
apple
apricot
📂 Task 2: Search Lines Ending with a Pattern
Command
grep 'y$' example.txt
Explanation
$ → matches end of line
Output
cherry
📂 Task 3: Optional Character Matching
Create file
nano colourExample.txt
Add content
color
colour
colr
Command
grep 'colou?r' colourExample.txt
Explanation
? → optional character (u)
Output
color
colour
🧠 Key Learning
^ start of line
$ end of line
? optional character
grep text filtering tool
🚀 Result

You successfully practiced basic regex patterns using grep in Linux.
