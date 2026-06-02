import os
import time
import logging

# Logging setup
logging.basicConfig(
    filename='cleanup_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def cleanup_old_files(directory, days_threshold):
    seconds_threshold = days_threshold * 24 * 60 * 60
    current_time = time.time()

    deleted_files_count = 0

    if not os.path.exists(directory):
        print("Directory does not exist!")
        return 0

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            file_mod_time = os.path.getmtime(file_path)
            file_age = current_time - file_mod_time

            if file_age > seconds_threshold:
                os.remove(file_path)
                logging.info(f"Deleted: {file_path}")
                print(f"Deleted: {file_path}")
                deleted_files_count += 1
            else:
                logging.info(f"Kept: {file_path}")

    return deleted_files_count


if __name__ == "__main__":
    directory_to_cleanup = "./test_directory"
    days_to_keep = 30

    deleted_count = cleanup_old_files(directory_to_cleanup, days_to_keep)

    print(f"\nTotal files deleted: {deleted_count}")
    print("Log saved to cleanup_log.txt")
