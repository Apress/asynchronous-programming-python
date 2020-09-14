"""
Exactly the same code as queues_with_processes.py
other than that the workers are not created as daemon processes
This code will never finish (unless manually aborted)
because the main Python process will wait for the worker processes to finish,
which never happens
"""
import math, time
import multiprocessing

task_queue = multiprocessing.JoinableQueue()
result_queue = multiprocessing.Queue()

def worker():
    while True:
        x = task_queue.get()
        print(x)
        result = math.factorial(x)
        result_queue.put((x, str(result)[:10]))
        task_queue.task_done()

start_time = time.time()
large_number = 100_000
processes = []
for x in range(large_number - 5, large_number + 5):
    task_queue.put(x)

for _ in range(5):
    process = multiprocessing.Process(target=worker, daemon=False)
    process.start()
    processes.append(process)

task_queue.join()

while not result_queue.empty():
    x, result = result_queue.get()
    print(x, result)
print(f'Duration {time.time() - start_time:0.3} seconds')
