import datetime

def log_time():
    with open("log.txt", "a") as file:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"Current Time: {current_time}\n")

if __name__ == "__main__":
    log_time()
