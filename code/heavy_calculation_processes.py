"""
A multiprocessing version of heavy_calculation.py
"""

import math
import time
import multiprocessing

def calculate(x):
    result = math.factorial(x)
    print('. ', end='')

start_time = time.time()
large_number = 100_000
processes = []

# Create one process per calculation
for x in range(large_number - 5, large_number + 5):
    process = multiprocessing.Process(target=calculate, args=(x, ))
    process.start()
    processes.append(process)

# Wait for all processes to finish
for process in processes:
    process.join()

print(f'Duration {time.time() - start_time:0.3} seconds')
