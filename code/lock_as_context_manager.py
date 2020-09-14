"""
Use a lock as a context manager
This ensures that the lock will always be released
even if there an error is raised
"""

import threading

counter = {0: 0}
counter_lock = threading.Lock()

def plus_many():
    for _ in range(100_000):

    	# Request the lock
        with counter_lock:
            counter[0] += 1
            if counter[0] > 200_000:
                raise Exception
        	# The lock is automatically released
        	# as soon as we leave this code block

threads = []
for _ in range(10):
    thread = threading.Thread(target=plus_many)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(f'Result: {counter[0]}')
