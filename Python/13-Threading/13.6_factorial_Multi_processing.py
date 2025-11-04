'''
Real-World Example: Multi-processing for CPU-Bound Tasks
Scenario: Factorial Calculation
Calculating the factorial of a number is a CPU-bound task, as it requires significant computation. Using multi-processing can help distribute the workload across multiple CPU cores, speeding up the calculation for large numbers.
'''

import multiprocessing
import math
import time
import sys

# Increase the maximum numbers of digits for integers conversion
sys.set_int_max_str_digits(1000000)

# Function to compute factorial to a given number

def compute_factorial(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}.")
    return result

if __name__ == "__main__":
    numbers = [50000, 60000, 70000, 80000]  # Large numbers for factorial calculation

    start_time = time.time()

    # Create a pool of processes
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial, numbers)

    finished_time = time.time()
    
    print(f'Results: {results}')
    print(f"Time taken with multiprocessing: {finished_time - start_time} seconds")