"""
An example of distributing function calls
across a pool processes (running in paralle)
using a ProcessPoolExecutor's submit method
"""

import math
import time
import concurrent.futures

def calculate_factorial(x):
    print(f'Calculating {x}!')
    return x, str(math.factorial(x))[:10]

start_time = time.time()
large_number = 100_000

# Create an executor with up to 5 Python processes
with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
    futures = [
    	# Ask the executor to run 10 copies of the calculate_factorial
        executor.submit(calculate_factorial, x)
        for x in range(large_number - 5, large_number + 5)
    ]

for future in futures:
	# Each future's result() function returns either the result 
	# or re-raise any error raised in the called function
    x, result = future.result()
    print(f'{x}! = {result}.....')
print(f'Duration {time.time() - start_time:0.3} seconds')
