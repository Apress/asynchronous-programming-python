"""
An example of a race condition
"""

import threading

counter = {x: 0 for x in range(10)}

def plus_many():
    # The first thread will have a start value of 0,
    # because no (other) thread has increased it
    # Subsequent threads will start with a higher value
    start = counter[0]
    for _ in range(100_000):

        """
        This statement consists of multiple byte codes
        and can be interrupted by another thread

        1. Put (shared) old value of counter[0] on the (thread's) stack
        2. Put 1 on the stack
        3. Remove the top two values from the stack and replace it with their sum
            (i.e. old value + 1)
        4. Move the top of the stack (old value + 1) back to the (shared) counter[0]

        Because multiple threads run this in parallel
        from time to time thread A and B both get the same old value, 
        store it locally, add 1 to it and write the result back
        The net result is in increase of 1 despite two threads seemingly having increased the value
        """
        counter[0] += 1
    print(f'from {start} to {counter[0]}')

threads = []
for _ in range(10):
    # 10 threads, each increaseing counter[0] by 100,000
    thread = threading.Thread(target=plus_many)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

# This should print out 1,000,000 but typically prints out significantly less
# If you've got a very fast processor, and get 1,000,000
# you may need to increase the number of threads from 10 to 50, 100 or more, so you can see the race condition
print(f'Result: {counter[0]}')
