"""
How to add error handling when using concurrent.futures.ProcessPoolExecutor(...).map(...)
"""
import time
import concurrent.futures

def calculate_factorial(x):
    time.sleep(0.1)
    print(f'Calculating {x}!')
    raise ValueError

start_time = time.time()
large_number = 100_000
results = concurrent.futures.ProcessPoolExecutor(max_workers=5).map(
    calculate_factorial,
    range(large_number - 5, large_number + 5)
)

# When iterating of the return value of the map method
# if the called function (in this case calculate_factorial) raised an error
try:
    for x, result in results:
        print(f'{x}! = {result}.....')
except ValueError:
    print('Value error was raised')
print(f'Duration {time.time() - start_time:0.3} seconds')
