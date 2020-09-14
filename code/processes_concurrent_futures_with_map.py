"""
An example of using the ProcessPoolExecutor's map method
to run the same function across different sets of arguments
in parallel
"""
import math
import time
import concurrent.futures

def calculate_factorial(x):
    print(f'Calculating {x}!')
    return x, str(math.factorial(x))[:10]

start_time = time.time()
large_number = 100_000

# Ask the Executor to run calculate_factorial for the numbers 99,995 .. 100,004
results = concurrent.futures.ProcessPoolExecutor(max_workers=5).map(
    calculate_factorial,
    range(large_number - 5, large_number + 5)
)

# The value returned by the map method is iterable,
# returning one result at a time,
# or re-raising any error raised in the called function
for x, result in results:
    print(f'{x}! = {result}.....')
print(f'Duration {time.time() - start_time:0.3} seconds')
