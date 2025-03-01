import threading
import time


forks = [threading.Semaphore(1) for _ in range(5)]

eating_limit = threading.Semaphore(2) 

def philosopher(i):
    left_fork = forks[i]
    right_fork = forks[(i + 1) % 5]
    
    while True:
        print(f"Philosopher {i} is thinking.")
        time.sleep(3)  
        
       
        eating_limit.acquire()  
        
        with left_fork:  
            with right_fork:  
                print(f"Philosopher {i} is eating.")
                time.sleep(2)  

       
        eating_limit.release() 

def dining_philosophers_example():
    threads = [threading.Thread(target=philosopher, args=(i,)) for i in range(5)]
    
    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    dining_philosophers_example()
