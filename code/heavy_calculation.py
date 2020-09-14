"""
A CPU-intensive process
"""

import math
import time

def calculate(x):
	# factorial(100,000) has about 456,574 digits
    result = math.factorial(x)
    print('. ', end='')

    # This function doesn't return any values
    # It just needs to spend some time keeping the CPU busy

start_time = time.time()
large_number = 100_000

# Calculate the factorial for 99,995 .. 100,004
for x in range(large_number - 5, large_number + 5):
    calculate(large_number)

print()
print(f'Duration {time.time() - start_time:0.3} seconds')
