# Lab 34: Working with DateTime Data in Python

## Objective

Learn how to parse dates, extract date components, and calculate time differences using Python's datetime module.

## Tools Used

- Python
- datetime module

## Tasks Performed

### Task 1: Parse Dates

Converted a date string into a datetime object using:

```python
datetime.datetime.strptime()
Obtained the current date and time using:

datetime.datetime.now()
Task 2: Extract Components

Extracted:

Year
Month
Day
Hour
Minute
Second

from datetime objects.

Task 3: Compute Time Differences

Calculated:

Difference between two dates
Number of days remaining until a holiday

using timedelta objects.

Main Code
parsed_date = datetime.datetime.strptime(
    "2023-10-03",
    "%Y-%m-%d"
)

current_datetime = datetime.datetime.now()
Output

The program displays:

Parsed date
Current date and time
Date components
Time components
Difference between dates
Holiday countdown
Final Structure
lab-34-datetime-python/
├── README.md
├── datetime_operations.py
└── ml-env/
Conclusion

In this lab, I learned how to work with Python's datetime module. I parsed date strings, extracted date and time components, and calculated time differences. These skills are useful for scheduling systems, reminders, event countdowns, and other time-sensitive applications.
