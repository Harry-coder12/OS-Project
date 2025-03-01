import threading
import time

mutex = threading.Lock()

def low_priority_task():
    with mutex:
        print("Low priority task is running.")
        time.sleep(5)

def high_priority_task():
    with mutex:
        print("High priority task is running.")

def priority_inversion_example():
    low_thread = threading.Thread(target=low_priority_task)
    high_thread = threading.Thread(target=high_priority_task)

    low_thread.start()
    time.sleep(1)
    high_thread.start()

    low_thread.join()
    high_thread.join()
