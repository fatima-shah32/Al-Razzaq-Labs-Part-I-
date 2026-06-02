import requests
import json

# Task 1: API URL
api_url = "https://jsonplaceholder.typicode.com/posts/1"

# Send GET request
response = requests.get(api_url)

# Check response
if response.status_code == 200:
    print("✅ Data Retrieved Successfully!")

    # Task 2: Convert JSON to Python dictionary
    data = response.json()

    print("\n📦 Full JSON Data:")
    print(data)

    # Task 3: Extract specific fields
    post_info = {
        "title": data["title"],
        "body": data["body"]
    }

    print("\n🎯 Extracted Data:")
    print(post_info)

    # Save to local JSON file
    with open("post_info.json", "w") as json_file:
        json.dump(post_info, json_file, indent=4)

    print("\n💾 Data saved to post_info.json")

else:
    print("❌ Failed to retrieve data. Status code:", response.status_code)
