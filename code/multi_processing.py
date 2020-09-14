"""
A simple multiprocessing example

5 processes all wait in parallel
Threads would be more appropriate here
This version is here so you can compare it with threads.py
"""
import multiprocessing
import random
import time

def random_slow_function(name):
    duration = random.uniform(2, 4)
    print(f'Start of {name}, sleeping for {duration:.2} seconds')
    time.sleep(duration)
    print(f'End of {name}')

start_time = time.time()

processes = []
# Create 5 processes (5 more copies of Python)
# Each running a copy of the random_slow_function
for i in range(5):
    process = multiprocessing.Process(target=random_slow_function, args=(i,))
    process.start()
    processes.append(process)

for process in processes:
    process.join()

lapsed_time = time.time() - start_time
print(f'Lapsed time {lapsed_time:.3}')
