### Multiprocessing : It allows to us processes to run in parallel
### CPU-Bound tasks : Tasks that are heavy on cpu usage (like complex calculations, data processing).
### Parallel execution : When you want to fully utilize multiple CPU cores for computationally intensive tasks.

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i*i*i}")
        
if __name__ == "__main__":
    
    ## Create 2 processes
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    t = time.time()

    # Start the processes
    p1.start()
    p2.start()

    # Wait for the processes to complete
    p1.join()
    p2.join()

    # Measure the time taken
    finished_time = time.time()-t
    print(f"Time taken with multiprocessing: {finished_time}")