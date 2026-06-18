# Lab 35: awk for Data Processing

## Objective

Learn how to use awk for extracting columns and filtering rows from structured text files.

---

## Prerequisites

* Linux Operating System
* Terminal Access
* Basic Command Line Knowledge

---

## Task 1: Print Specific Columns

### Create Sample Data File

```bash
cat > data.txt << EOF
Name Age Gender
John 28 Male
Emma 22 Female
Mike 32 Male
Lucy 29 Female
EOF
```

### Display File

```bash
cat data.txt
```

### Print First and Third Columns

```bash
awk '{print $1, $3}' data.txt
```

### Expected Output

```text
Name Gender
John Male
Emma Female
Mike Male
Lucy Female
```

---

## Task 2: Filter Rows Based on Condition

### Display Records with Age Greater Than 25

```bash
awk '$2 > 25 {print $0}' data.txt
```

### Expected Output

```text
John 28 Male
Mike 32 Male
Lucy 29 Female
```

### Explanation

* $2 represents the second column (Age).
* > 25 filters rows where age is greater than 25.
* $0 prints the entire matching row.

---

## Summary

| Command                       | Purpose                |
| ----------------------------- | ---------------------- |
| awk '{print $1}' file         | Print first column     |
| awk '{print $1,$3}' file      | Print selected columns |
| awk '$2 > 25 {print $0}' file | Filter rows            |
| awk '{print NF}' file         | Count fields           |

---

## Conclusion

In this lab, I learned how to use awk to extract specific columns and filter records based on conditions. awk is a powerful Linux text-processing tool widely used in automation, reporting, and log analysis.
