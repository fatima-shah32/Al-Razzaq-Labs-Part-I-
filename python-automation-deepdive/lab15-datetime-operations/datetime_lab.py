from datetime import datetime, timedelta

# Task 1: Get current date and time
current_datetime = datetime.now()
print("📅 Current date and time:", current_datetime)

# Task 2: Date calculations
yesterday = current_datetime - timedelta(days=1)
next_week = current_datetime + timedelta(weeks=1)

print("\n📆 Date Calculations:")
print("Yesterday's date:", yesterday)
print("Next week's date:", next_week)

# Task 3: Formatting date and time
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

print("\n🕒 Formatted Date and Time:")
print("Formatted:", formatted_datetime)
