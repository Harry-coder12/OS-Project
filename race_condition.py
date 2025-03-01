import threading

counter = 0
mutex = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with mutex:
            counter += 1

def race_condition_example():
    threads = []
    for _ in range(5):
        thread = threading.Thread(target=increment)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Counter Value: {counter}")
