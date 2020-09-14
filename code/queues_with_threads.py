"""
The same as queues_with_processes

apart from using the threading and queue libraries
instead of the multiprocessing library
"""

import math
import time
import threading
import queue

task_queue = queue.Queue()
result_queue = queue.Queue()

def worker():
    while True:
        x = task_queue.get()
        print(x)
        result = math.factorial(x)
        result_queue.put((x, str(result)[:10]))
        task_queue.task_done()

start_time = time.time()
large_number = 100_000
for x in range(large_number - 5, large_number + 5):
    task_queue.put(x)

for _ in range(5):
    thread = threading.Thread(target=worker, daemon=True)
    thread.start()

task_queue.join()

while not result_queue.empty():
    print(result_queue.get())
print(f'Duration {time.time() - start_time:0.3} seconds')
