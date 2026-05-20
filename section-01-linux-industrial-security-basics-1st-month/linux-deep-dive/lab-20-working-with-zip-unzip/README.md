# Lab 20: Working with zip/unzip

## Objective
Learn how to compress and extract files using zip and unzip in Linux.

---

## Task 1: Check zip/unzip Installation

### Check zip
```bash
zip -v
Check unzip
unzip -v
Install zip/unzip (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install zip unzip -y
#Task 2: Create Sample Files
echo "This is file 1" > file1.txt
echo "This is file 2" > file2.txt
#Task 3: Compress Files
zip myarchive.zip file1.txt file2.txt
Verify Archive
unzip -l myarchive.zip
#Task 4: Extract Archive
unzip myarchive.zip
Verify Extraction
ls
