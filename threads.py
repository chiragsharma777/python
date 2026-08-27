import threading
import time

def task1():
    for i in range(5):
        print("Task 1:", i)
        time.sleep(1)

def task2():
    for i in range(5):
        print("Task 2:", i)
        time.sleep(1)

# Create threads
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

# Start threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

print("All tasks completed!")