"""
Same code as the barriers example
Only difference is that workers are started as daemons
"""

import threading
import time

wall = threading.Barrier(5)

def worker(name):
    print(f'{name} is here')
    wall.wait()
    print(f'{name} is pushing')

workers = [
    # The Iimer's __init__ method doesn't have a 'daemon' argument
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
    # In lieu of a daemon argument during creation,
    # set it as an attribute instead
    worker.daemon = True
    worker.start()

for i in range(1, 12):
    time.sleep(1)
    print(i)

# The non-daemon barrier example got stuck here
# waiting for the final worker to finish

# As the workers have been created as daemons
# Python doesn't wait for them, and closes down
# at the end of the 12 second countdown,
# regardless whether all workers are finished or not
