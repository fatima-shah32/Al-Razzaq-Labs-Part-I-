# Lab 18: Archiving with tar

## Objective
Learn to create, list, and extract compressed tar archives in Linux.

---

## Tasks Completed

### 1. Create Sample Folder
```bash
mkdir project
echo "File 1" > project/file1.txt
echo "File 2" > project/file2.txt
#2. Create Compressed Archive
tar -czf project_archive.tar.gz project
33. List Archive Contents
tar -tzf project_archive.tar.gz
#4. Extract Archive
tar -xzf project_archive.tar.gz
