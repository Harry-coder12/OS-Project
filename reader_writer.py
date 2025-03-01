import threading

read_count = 0
mutex = threading.Lock()
write_mutex = threading.Lock()

def reader():
    global read_count
    with mutex:
        read_count += 1
        if read_count == 1:
            write_mutex.acquire()
    print("User Is Reading data")
    with mutex:
        read_count -= 1
        if read_count == 0:
            write_mutex.release()

def writer():
    write_mutex.acquire()
    print("User Is Writing data")
    write_mutex.release()

def reader_writer_example():
    readers = [threading.Thread(target=reader) for _ in range(5)]
    writer_thread = threading.Thread(target=writer)

    for r in readers:
        r.start()
    
    writer_thread.start()

    for r in readers:
        r.join()

    writer_thread.join()
