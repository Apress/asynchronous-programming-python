"""
A simple example of using threading.Timer
"""

import threading
import time

# Create 4 timers, each starting at a different time
# The first arguments is the number of seconds to wait
# between calling timer.start and running the function
# Otherwise, timers work the same as threads
timer_1 = threading.Timer(7, function=print, args=('Breakfast is ready', ))
timer_2 = threading.Timer(5, function=print, args=('Time to get up', ))
timer_3 = threading.Timer(10, function=print, args=('You are running late now', ))
timer_4 = threading.Timer(8, function=print, args=('It is getting cold', ))
timers = [timer_1, timer_2, timer_3, timer_4]

# Start all timers
for timer in timers:
    timer.start()
print('Timers started')

# Print a counter from 1 to 14
# one per second
for i in range(1, 15):
    time.sleep(1)

    # After 6 seconds cancel timer_2 and timer_4
    if i == 6:

    	# timer_2 started after 5 seconds, so can't be cancelled any more
        timer_2.cancel()

        # timer_4 was due to start at 8 seconds, so is cancelled successfully
        timer_4.cancel()
    print(i)

for timer in timers:
    timer.join()

print('All done')
