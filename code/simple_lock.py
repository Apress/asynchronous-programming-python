"""
A 'fixed' version of race_condition.py

Uses a lock to protect the shared resource
"""

import threading

# A shared resource plus its lock
counter = {0: 0}
counter_lock = threading.Lock()

def plus_many():
    for _ in range(100_000):

    	# Acquire lock, change resource, release lock
        counter_lock.acquire()
        counter[0] += 1
        counter_lock.release()

threads = []
for _ in range(10):
    thread = threading.Thread(target=plus_many)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(f'Result: {counter[0]}')
