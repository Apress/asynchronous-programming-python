"""
A simple example of using threads

5 long processes are run concurrently rather than one after the other
"""

import threading
import random
import time


# A function which simulates a typical I/O call,
# mostly waiting for the computer/hardware/Internet to process the I/O request
def random_slow_function(name):
    duration = random.uniform(2, 4)
    print(f'Start of {name}, sleeping for {duration:.2} seconds')
    time.sleep(duration)
    print(f'End of {name}')


start_time = time.time()

# Keep a list of the threads
threads = []

# Create 5 threads
for i in range(5):

	# Create a thread. Parameters are:
	#	target: the function to run in the new thread
	# 	args: the arguments to pass to the function
    thread = threading.Thread(target=random_slow_function, args=(i,))

    # Start the thread and add to the list
    thread.start()
    threads.append(thread)

# Wait for each thread to finish, to 're-join' the main thread
for thread in threads:
    thread.join()

lapsed_time = time.time() - start_time
print(f'Lapsed time {lapsed_time:.3}')
