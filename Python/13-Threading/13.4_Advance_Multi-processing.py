### Advanced Multi-processing with Pool Executor

from concurrent.futures import ProcessPoolExecutor
import time

def square(number: int) -> str:
    time.sleep(1)
    return f"Square: {number * number}"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if __name__ == "__main__":

    # Run with a pool of processes; map returns results in input order
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = executor.map(square, numbers)
        
    for msg in results:
        print(msg)