"""
A simple semaphore example
"""

import threading
import queue
import time

number_of_eaters = 10

# There are two forks and two knives
forks = threading.Semaphore(2)
spoons = threading.Semaphore(2)

# Track how many people are currently eating
eater_count_queue = queue.Queue()

# Track how many people are done eating
# This queue limits the number of items to 10
# Once it reaches 10 it is .full()
done_queue = queue.Queue(maxsize=number_of_eaters)

def eater():
    # Request a spoon, wait if none available
    with spoons:

        # Request a fork, wait if none available
        with forks:
            # Start eating
            # Increase the number of eaters by 1
            eater_count_queue.put(1)
            time.sleep(1)

    # Done eating
    # Decrease number of active eaters by 1
    eater_count_queue.put(-1)

    # Increase number of finished eaters by 1
    done_queue.put(1)

threads = []
for _ in range(number_of_eaters):
    threads.append(threading.Thread(target=eater))

for thread in threads:
    thread.start()

number_of_eaters = 0

# The queue is limited to 10 items, which is when it becomes full()
while not done_queue.full():
    # Wait for an update to the number of active eaters (+1 or -1)
    # then print the current number
    number_of_eaters += eater_count_queue.get()
    print(number_of_eaters)
