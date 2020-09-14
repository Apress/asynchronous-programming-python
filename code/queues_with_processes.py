"""
An example of using queues with multiprocessing
"""
import math, time
import multiprocessing

# A JoinableQueue has a task_done method to mark work as completed
# and a join method to wait until there are no not-yet-done tasks on the queue
task_queue = multiprocessing.JoinableQueue()

# A Queue does not have task_done or join method
result_queue = multiprocessing.Queue()

def worker():
    while True:
        # Get the next task off the task queue
        x = task_queue.get()
        print(x)

        # Do the work
        result = math.factorial(x)

        # Store the result back on the queue
        # 100,000! (factorial) has over 450,000 digits
        # Moving this between different instances of the Python interpreter
        # is quite slow
        # For this example, just return the last 10 digits
        result_queue.put((x, str(result)[:10]))

        # Mark this task as done
        # For production code this has to be done in a 'finally:' block
        # otherwise one failed worker will block the task_queue.join() for ever
        task_queue.task_done()

start_time = time.time()
large_number = 100_000
processes = []
# Put the numbers 99,995 .. 100,004 on the task queue
# these are the numbers that need to be calculated
for x in range(large_number - 5, large_number + 5):
    task_queue.put(x)

# Start 5 workers
# as daemons, so the main Python process knows it is safe to shutdown at any time
for _ in range(5):
    process = multiprocessing.Process(target=worker, daemon=True)
    process.start()
    processes.append(process)

# Wait for all tasks on the task_queue to be marked as task_done
task_queue.join()

# Print the results off the result_queue
while not result_queue.empty():
    x, result = result_queue.get()
    print(x, result)
print(f'Duration {time.time() - start_time:0.3} seconds')
