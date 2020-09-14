"""
A lock which is always released
even if an error is raise
"""

import threading

counter = {0: 0}
counter_lock = threading.Lock()

def plus_many():
    for _ in range(100_000):
        counter_lock.acquire()
        try:
            # All critical code is within a try block
            counter[0] += 1

            # Raise an error once the counter reaches 200,000
            if counter[0] > 200_000:
                assert False
        except:
            raise
        finally:
            # The code to release the lock MUST be in the finally block
            # to ensure the lock is always released
            counter_lock.release()

threads = []
for _ in range(10):
    thread = threading.Thread(target=plus_many)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(f'Result: {counter[0]}')
