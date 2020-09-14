"""
A multithreading version of heavy_calculation.py
"""

import math
import time
import threading

def calculate(x):
    result = math.factorial(x)
    print('. ', end='')

start_time = time.time()
large_number = 100_000
threads = []

# Create one thread per calculation
for x in range(large_number - 5, large_number + 5):
    thread = threading.Thread(target=calculate, args=(x, ))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

print(f'Duration {time.time() - start_time:0.3} seconds')
