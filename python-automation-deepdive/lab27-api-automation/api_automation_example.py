import requests

# Task 1: Local data dictionary
user_data = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "age": 30
}

# Task 2: API endpoint
url = "https://httpbin.org/post"

# Send POST request
response = requests.post(url, json=user_data)

# Task 3: Check response status
if response.status_code == 200:
    print("Request was successful!")
else:
    print(f"Request failed with status code: {response.status_code}")

# Task 4: Parse JSON response
response_data = response.json()

print("\n📦 Full Response Data:\n")
print(response_data)

print("\n🎯 Extracted JSON Data:\n")
print(response_data["json"])
