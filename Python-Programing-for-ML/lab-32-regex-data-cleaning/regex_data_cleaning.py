import re

print("=== Task 1: Match Phone Number ===")

text = "My phone number is 123-456-7890."
pattern = r"\d{3}-\d{3}-\d{4}"

match = re.search(pattern, text)

if match:
    print("Matched text:", match.group())
else:
    print("No match found")


print("\n=== Task 2: Find Email Addresses ===")

text = "Contact us at info@example.com or support@example.org."
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

emails = re.findall(email_pattern, text)

print("Found emails:", emails)


print("\n=== Task 3: Remove Punctuation ===")

text = "Hello! This, is a sample text. It's meant for cleaning."
clean_pattern = r"[^\w\s]"

cleaned_text = re.sub(clean_pattern, "", text)

print("Original text:", text)
print("Cleaned text:", cleaned_text)


print("\n=== Task 4: Normalize Phone Numbers ===")

numbers = [
    "1234567890",
    "123-456-7890",
    "(123) 456-7890"
]

standardized_numbers = []

for number in numbers:
    digits = re.sub(r"\D", "", number)

    if len(digits) == 10:
        formatted_number = re.sub(
            r"(\d{3})(\d{3})(\d{4})",
            r"\1-\2-\3",
            digits
        )
        standardized_numbers.append(formatted_number)

print("Standardized phone numbers:")

for num in standardized_numbers:
    print(num)
