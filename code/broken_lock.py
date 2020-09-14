"""
An example of a lock which is acquired but never released
"""

import threading

counter = {0: 0}
counter_lock = threading.Lock()

def plus_many():
    for _ in range(100_000):
        counter_lock.acquire()
        counter[0] += 1

        # Once the counter reaches 200 000, this raises an error
        # and the thread holds on to the lock
        # all other threads waiting for this lock are now stuck
        if counter[0] > 200_000:
            assert False
        counter_lock.release()

threads = []
for _ in range(10):
    thread = threading.Thread(target=plus_many)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(f'Result: {counter[0]}')
