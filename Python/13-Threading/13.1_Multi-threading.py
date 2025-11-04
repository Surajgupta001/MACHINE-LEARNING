### Multithreading
### When to Use Multithreading
### I/O-Bound tasks : Tasks that spend more time waiting for I/O operations (like file reading/writing, network requests) than using the CPU.
### Concurrent execution : When you want to improve the throughput of your application by performing multiple operations simultaneously.

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number: {i}")
        
def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        time.sleep(2)
        print(f"Letter: {letter}")

# Using threading
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t = time.time()
# Start the threads
t1.start()
t2.start()

# Wait for the threads to complete
t1.join()
t2.join()

finished_time = time.time()-t
print(f"Time taken without threading: {finished_time}")