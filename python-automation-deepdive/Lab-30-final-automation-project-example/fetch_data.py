import requests
import csv
import logging
import argparse

# 📊 Logging setup
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# 🎯 CLI ARGUMENT SETUP
parser = argparse.ArgumentParser(description='Fetch and process API data')
parser.add_argument('--user_id', type=int, default=1, help='User ID to filter posts by')
args = parser.parse_args()

try:
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    response.raise_for_status()

    logging.info("Data fetched successfully")

    data = response.json()
    print(f"Fetched {len(data)} records")

    processed_data = [
        {"userId": post["userId"], "title": post["title"]}
        for post in data
    ]

    # 🎯 Dynamic filter using CLI input
    user_posts = [
        post for post in processed_data
        if post["userId"] == args.user_id
    ]

    print(f"User {args.user_id} has {len(user_posts)} posts")

    # 📁 Write CSV
    with open('user_posts.csv', 'w', newline='') as csvfile:
        fieldnames = ["userId", "title"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for post in user_posts:
            writer.writerow(post)

    logging.info(f"CSV file created for user {args.user_id}")
    print("CSV file created: user_posts.csv")

except requests.exceptions.RequestException as e:
    logging.error(f"Error fetching data: {e}")
    print("Failed to fetch data")
    exit(1)
