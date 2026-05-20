# Lab 19: Compressing with gzip and bzip2

## Objective
Learn file compression and decompression using gzip and bzip2 in Linux.

---

## Tasks Completed

### Task 1: gzip Compression
```bash
echo "This is gzip file content" > example.txt
gzip example.txt
ls -lh example.txt.gz
#Task 2: gunzip Decompression
gunzip example.txt.gz
ls -lh example.txt
#Task 3: bzip2 Compression
echo "This is bzip2 file content" > sample.txt
bzip2 sample.txt
ls -lh sample.txt.bz2
#Task 4: bunzip2 Decompression
bunzip2 sample.txt.bz2
ls -lh sample.txt
