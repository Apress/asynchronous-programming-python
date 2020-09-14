"""
An example of starvation

The determined eater will continue waiting for the shared resource
The impatient eater alternates between waiting for the resource and sleeping

All determined eaters eat first, then the others

"""

import threading
import time

progress = dict(impatient=0, determined=0)
spoon = threading.Lock()

def determined_eater():
    # Wait for the shared resource
    with spoon:
        # Track how many determined eaters have eaten
        progress['determined'] += 1
        time.sleep(0.2)

def impatient_eater():
    # Wait for the shared resource of a short while
    # If not available, sleep, then try again
    while True:
        if spoon.acquire(timeout=0.02):
            break
        time.sleep(0.1)

    # Track how many impatient eaters have eaten
    progress['impatient'] += 1
    time.sleep(0.2)
    spoon.release()

threads = []

# Create 10 of both types of eaters
for _ in range(10):
    threads.append(threading.Thread(target=determined_eater))
    threads.append(threading.Thread(target=impatient_eater))

for thread in threads:
    thread.start()

# Stop once all threads are done
while any(thread.is_alive() for thread in threads):
    # Track how many impatient eaters have eaten
    # Every 0.2 seconds show the current state
    print(progress)
    time.sleep(0.2)
