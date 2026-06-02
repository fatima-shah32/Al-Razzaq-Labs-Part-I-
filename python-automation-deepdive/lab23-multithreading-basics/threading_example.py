import threading
import time

# Task 2.1: Thread function
def print_numbers(thread_name):
    for i in range(1, 6):
        print(f"{thread_name} count: {i}")
        time.sleep(1)  # Simulates delay

# Task 2.2: Create threads
thread1 = threading.Thread(target=print_numbers, args=("Thread 1",))
thread2 = threading.Thread(target=print_numbers, args=("Thread 2",))

# Start threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

print("\n✅ Both threads have completed execution.")
