##multithreading with Thread pool executor


from concurrent.futures import ThreadPoolExecutor  # -->This module provides a high-level API for parallel task execution using threads.
import time

def print_number(number):
    time.sleep(1)
    return f"Number :{number}"

numbers=[1,2,3,4,5]

with ThreadPoolExecutor (max_workers=3) as executor:   #Creates a thread pool with 3 worker threads. This means that at most 3 tasks will run concurrently.
    results=executor.map(print_number,numbers)

for result in results:
    print(result)


#ThreadPoolExecutor helps in parallel execution using multiple threads.
#max_workers=3 ensures up to 3 tasks run in parallel.
#executor.map() preserves the input order in the output.
#Using time.sleep() simulates real-world time-consuming tasks like API calls, file processing, etc.
#Execution time reduces significantly due to parallelism.