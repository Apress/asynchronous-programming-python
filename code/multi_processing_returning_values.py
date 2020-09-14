"""
Do NOT do this
This is to show that you cannot use subclassing
to return values from a process
This only works with threads, not with multiprocessing,
as shown in thread_returning_values.py
"""

import multiprocessing
import random
import time

# A class which runs the slow function
class RandomSlowFunction(multiprocessing.Process):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.duration = -1

    def run(self):
        self.duration = random.uniform(2, 4)
        print(f'Start of {self.name}, sleeping for {self.duration:.3} seconds')
        time.sleep(self.duration)
        print(f'End of {self.name}')

start_time = time.time()

processes = []
for i in range(5):
    # Create 5 processes - each running in their own memory space
    process = RandomSlowFunction(str(i))
    process.start()
    processes.append(process)

for process in processes:
    process.join()

total_duration = time.time() - start_time
print(f'Lapsed time {total_duration:.3}')
for process in processes:
    print(f'Duration: {process.duration}')
