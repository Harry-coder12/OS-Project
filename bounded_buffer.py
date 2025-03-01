import threading
import queue

buffer = queue.Queue(5)
mutex=threading.Lock()
def producer(a):
        item = f"item-{a}"
        buffer.put(item)
        print(f"Produced {item}")
        print(" ")

def consumer():
        item = buffer.get()
        print(f"Consumed {item}")
        print(" ")

def bounded_buffer_example():
    global a
    
    while True:
      
        x=input("Do You Want To Produce Or Consume : ")
        if buffer.full():
                print("Buffer is full. Producer is waiting.")
        else:
          if(x=="p"):
            a=input("Enter Item : ")
            producer(a)
        
          if buffer.empty():
                print("Buffer is empty. Consumer is waiting.")
          else:
           if(x=="c"):
             consumer()




if __name__ == "__main__":
    bounded_buffer_example()