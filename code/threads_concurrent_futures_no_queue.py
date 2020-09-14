"""
Using a ThreadPoolExecutor 
to create a pool of workers, each running in their own thread
and distribute some work between them

A simplified version of threads_concurrent_futures_with_queue.py
itself a simplified version of queue_with_threads.py
"""

import math
import time
import concurrent.futures

def calculate_factorial(x):
    print(f'Calculating {x}!')
    return x, str(math.factorial(x))[:10]

start_time = time.time()
large_number = 100_000

# Create an Executor with (up to) 5 workers in 5 separate threads
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:

	# Submit 10 requests to the executor 
	# to run calculate_factorial
	# with values from 99,995 to 100,004
    futures = [
        executor.submit(calculate_factorial, x)
        for x in range(large_number - 5, large_number + 5)
    ]

for future in futures:
	# Each future has a result method
	# which returns either the result or re-raise an error
    x, result = future.result()
    print(f'{x}! = {result}.....')
print(f'Duration {time.time() - start_time:0.3} seconds')
