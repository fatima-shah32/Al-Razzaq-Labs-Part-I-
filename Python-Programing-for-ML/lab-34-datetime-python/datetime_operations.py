import datetime

print("=== Task 1: Parse Dates ===")

# Parse a date string
date_string = "2023-10-03"
parsed_date = datetime.datetime.strptime(
    date_string,
    "%Y-%m-%d"
)

print("Parsed Date:", parsed_date)

# Current date and time
current_datetime = datetime.datetime.now()

print("Current Date and Time:", current_datetime)

print("\n=== Task 2: Extract Components ===")

# Extract year, month, day
year = parsed_date.year
month = parsed_date.month
day = parsed_date.day

print("Year:", year)
print("Month:", month)
print("Day:", day)

# Extract hour, minute, second
hour = current_datetime.hour
minute = current_datetime.minute
second = current_datetime.second

print("Hour:", hour)
print("Minute:", minute)
print("Second:", second)

print("\n=== Task 3: Compute Time Difference ===")

# Difference between two dates
another_date_string = "2023-10-10"

another_date = datetime.datetime.strptime(
    another_date_string,
    "%Y-%m-%d"
)

date_difference = another_date - parsed_date

print("Difference in Days:", date_difference.days)

print("\n=== Event Countdown Example ===")

holiday_date_string = "2026-12-25"

holiday_date = datetime.datetime.strptime(
    holiday_date_string,
    "%Y-%m-%d"
)

days_until_holiday = holiday_date - current_datetime

print("Days until holiday:", days_until_holiday.days)
