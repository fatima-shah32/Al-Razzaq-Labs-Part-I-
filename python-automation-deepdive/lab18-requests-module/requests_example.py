import requests

# Task 2: Send GET request to public API
url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

# Task 3: Check response status
if response.status_code == 200:
    print("✅ Request was successful!")

    # Parse JSON response
    data = response.json()

    print("\n📦 JSON Response Data:\n")
    print(data)

    # Print specific fields
    print("\n🎯 Extracted Fields:")
    print(f"Title: {data['title']}")
    print(f"Body: {data['body']}")

else:
    print("❌ Request failed with status code:", response.status_code)
