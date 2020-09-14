"""
Convoluted example to show how the Executor's map method handles errors in the called functions
"""


import time
import concurrent.futures

def calculate_factorial(x):
    print(f'Calculating {x}!')
    time.sleep(0.01)
    raise ValueError

start_time = time.time()
large_number = 100_000
results = concurrent.futures.ProcessPoolExecutor(max_workers=5).map(
    calculate_factorial,
    range(large_number - 5, large_number + 5)
)

# A manual version of a for loop
# to show that the ValueError is raised when (a for loop) calls next()
results_iterator = iter(results)
while True:
    try:
        x, result = next(results_iterator)
    except ValueError:
        # Even though all calculate_factorial functions raise a ValueError
        # Once the first one has raised an error
        # subsequent calls to next() return a StopIteration error
        print('Value error was raised')
    except StopIteration:
        print('End of iterator')
        break
    else:
        print(f'{x}! = {result}.....')

print(f'Duration {time.time() - start_time:0.3} seconds')
