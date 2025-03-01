import threading
import queue


buffer = queue.Queue(10)


mutex = threading.Lock()

items_to_produce = 10

def producer():
    for i in range(items_to_produce):
        item = f"item-{i}"
        
        with mutex:
            if buffer.full():
                print("Buffer is full. Producer is waiting.")
            else:
                buffer.put(item)
                print(f"Produced {item}")
        
def consumer():
    for i in range(items_to_produce):
        with mutex:
            if buffer.empty():
                print("Buffer is empty. Consumer is waiting.")
            else:
                item = buffer.get()
                print(f"Consumed {item}")

def producer_consumer_example():
    
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

   
    producer_thread.start()
    consumer_thread.start()

    
    producer_thread.join()
    consumer_thread.join()

if __name__ == "__main__":
    producer_consumer_example()
