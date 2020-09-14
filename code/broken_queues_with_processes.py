"""
An example of how NOT to use queues with multiprocessing
"""

import math
import time
import multiprocessing
import queue

# DO NOT DO THIS
# The queue library does not support processes
# it only works with threads
# With processes, each process will get its own copy of the queues
# and there will be no coordination between the threads
task_queue = queue.Queue()
result_queue = queue.Queue()

def worker():
    while True:
        # Get each of the 10 numbers of this process/worker's copy of the task_queue
        x = task_queue.get()
        print(x)
        result = math.factorial(x)

        # Write the result back to this process/worker's copy of the results queue
        # (not shared with the main Python process)
        result_queue.put((x, str(result)[:10]))
        task_queue.task_done()

start_time = time.time()
large_number = 100_000
for x in range(large_number - 5, large_number + 5):
    task_queue.put(x)

for _ in range(5):
    process = multiprocessing.Process(target=worker, daemon=True)
    process.start()

# The workers update their own copies of the task queue
# not the main process'
# The main process gets stuck here, waiting for its copy of the task queue 
# to be done
task_queue.join()

print(f'Duration {time.time() - start_time:0.3} seconds')
while not result_queue.empty():
    x, result = result_queue.get()
    print(x, result)
