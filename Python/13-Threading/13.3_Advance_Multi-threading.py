### Advanced Multi-threading with Pool Executor

from concurrent.futures import ThreadPoolExecutor
import time

def worker(number):
    time.sleep(1)
    return f"Number: {number}"


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Run with a small pool; map returns results in input order
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(worker, numbers)
for msg in results:
    print(msg)