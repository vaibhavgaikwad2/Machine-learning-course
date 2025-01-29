'''
Real world example: Multiprocessing for cpu bound tasks
scenario: Factorial calculations
factorial calculation especially for large numbers requires lots of 
computational work. 
multiprocessing can be used to distribute the workload across multiple
cpu cores, improving performance

'''

import multiprocessing
import math
import sys
import time
# Increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

# function to compute factorials of a given number

def compute_factorial(number):
    print(f"computing factorial of {number}")
    result=math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__=="__main__":
    numbers=[5000,6000,7000,8000]


    start_time=time.time()

    ## Create a pool of worker processes

    with multiprocessing.Pool() as pool:
        results=pool.map(compute_factorial,numbers)
    
    end_time=time.time()
    print(f"results: {results}")
    print(f"time taken: {end_time - start_time} seconds")
    
