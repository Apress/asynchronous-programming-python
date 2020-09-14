"""
An example of subclassing threading.Thread
to wrap a function in a thread

Within the thread, the function sets attributes
which can be read outside of the thread
"""

import threading
import random
import time

# Subclass threading.Thread
class RandomSlowFunction(threading.Thread):
    def __init__(self, name):
        # You MUST init the Thread superclass
        super().__init__()

        # The rest of the __init__ method can set attributes or do any other work
        self.name = name

    # Put the main code in a 'run' method
    # threading.Thread.start() will create a thread 
    # and run the .run() method in the new thread
    def run(self):
        self.duration = random.uniform(2, 4)
        print(f'Start of {self.name}, sleeping for {self.duration:.3} seconds')
        time.sleep(self.duration)
        print(f'End of {self.name}')

start_time = time.time()

threads = []
for i in range(5):
    thread = RandomSlowFunction(i)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

total_duration = time.time() - start_time
print(f'Lapsed time {total_duration:.3}')

# It is now possible to access the .duration value set inside the threads
print(f'Total durations {sum(thread.duration for thread in threads):.3}')
print(f'Longest time {max(thread.duration for thread in threads):.3}')
