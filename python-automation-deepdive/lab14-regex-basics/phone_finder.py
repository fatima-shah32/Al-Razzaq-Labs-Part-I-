import re

# Task 2: Define regex pattern for phone numbers
phone_pattern = re.compile(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}')

def find_phone_numbers(file_name):
    try:
        with open(file_name, "r") as file:
            text = file.read()
            return phone_pattern.findall(text)

    except FileNotFoundError:
        print("❌ File not found!")
        return []

# Main execution
if __name__ == "__main__":
    file_name = "contacts.txt"

    matches = find_phone_numbers(file_name)

    if matches:
        print("📞 Phone numbers found:")
        for match in matches:
            print(match)
    else:
        print("⚠️ No phone numbers found.")
