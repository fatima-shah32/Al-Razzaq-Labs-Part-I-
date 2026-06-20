from bs4 import BeautifulSoup
import requests

print("Libraries imported successfully!")

# Target webpage
url = "https://example.com"

# Fetch webpage content
response = requests.get(url)

if response.status_code == 200:
    print("Successfully fetched the webpage content!")
else:
    print("Failed to fetch the webpage content.")

# Parse HTML content
soup = BeautifulSoup(response.content, "html.parser")

print("\nFirst 500 characters of webpage:")
print(soup.prettify()[:500])

# Extract h1 headers
headers = soup.find_all("h1")

print("\nExtracted Headers:")
for header in headers:
    print(header.get_text())

# Clean extracted data
cleaned_data = [
    header.get_text().strip()
    for header in headers
]

print("\nCleaned Data:")
print(cleaned_data)
