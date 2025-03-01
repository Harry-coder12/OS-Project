import threading

mutex_a = threading.Lock()
mutex_b = threading.Lock()

def task_1():
    with mutex_a:
        print("Task 1 acquired mutex_a")
        with mutex_b:
            print("Task 1 acquired mutex_b")

def task_2():
    with mutex_a:#Solution Yahan Hai
        print("Task 2 acquired mutex_b")
        with mutex_b:
            print("Task 2 acquired mutex_a")

def deadlock_example():
    thread_1 = threading.Thread(target=task_1)
    thread_2 = threading.Thread(target=task_2)
    
    thread_1.start()
    thread_2.start()
    
    thread_1.join()
    thread_2.join()
