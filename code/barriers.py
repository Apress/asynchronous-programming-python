"""
A simple barrier example
"""

import threading
import time

# Create a barrier which will need 5 threads requesting it 
# at once before they can all continue
wall = threading.Barrier(5)

def worker(name):
    print(f'{name} is here')
    wall.wait()
    print(f'{name} is pushing')

workers = [
    # Use a timer to start each working at a different time
    threading.Timer(delay, function=worker, args=(name, ))
    for delay, name in [
        (2, 'John'),
        (3, 'Sue'),
        (1, 'Sam'),
        (8, 'Alex'),
        (2.5, 'Angela'),
        (10, 'Sage')
    ]
]

for worker in workers:
    worker.start()

# Show the time since the start in seconds
# (more or less)
for i in range(1, 12):
    time.sleep(1)
    print(i)

# This code never stop - the last thread ('Sage') is stuck
# waiting for four more before it can continue
