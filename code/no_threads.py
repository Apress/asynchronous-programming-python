"""
Some sample slow code
to show this can be speeded up by running the functions in parallel
"""
import random
import time


# A function which sleeps for 2 - 4 seconds
def random_slow_function(name):
    duration = random.uniform(2, 4)
    print(f'Start of {name}, sleeping for {duration:.2} seconds')
    time.sleep(duration)
    print(f'End of {name}')


start_time = time.time()
for i in range(5):
    random_slow_function(f'function {i}')
total_duration = time.time() - start_time
print(f'Total duration {total_duration:.3}')
