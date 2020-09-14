"""
Using a ThreadPoolExecutor 
to create a pool of workers, each running in their own thread
and distribute some work between them

Results are put in a result_queue
Note that the Executor can gather the results for you
For a better example see threads_current_futures_no_queue.py

A simplified version of queue_with_threads.py
"""

import math
import time
import queue
import concurrent.futures

result_queue = queue.Queue()

def calculate_factorial(x):
    print(x)
    result = math.factorial(x)
    result_queue.put((x, str(result)[:10]))

start_time = time.time()
large_number = 100_000
futures = []

# Create an Executor with (up to) 5 workers in 5 separate threads
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:

	# Submit 10 requests to the executor 
	# to run calculate_factorial
	# with values from 99,995 to 100,004
    for x in range(large_number - 5, large_number + 5):
        futures.append(executor.submit(calculate_factorial, x))

# Wait for all threads to cmoplete
concurrent.futures.wait(futures)

# Print the results from the result_queue
while not result_queue.empty():
    x, result = result_queue.get()
    print(x, result)
    
print(f'Duration {time.time() - start_time:0.3} seconds')
