"""
A simple events example
"""

import threading
import time

# Create an event
waiving = threading.Event()

def customer():
    print('customer: starting')
    time.sleep(3)
    print('customer: waiving')

    # Raise the event
    # This will allow any threads which are waiting for it (i.e. the waiter() thread) to continue
    waiving.set()
    time.sleep(2)
    print('customer: done')

def waiter():
    print('waiter: starting')
    print('waiter: waiting for event')

    # Wait for the event
    waiving.wait()

    # The waiter thread will continue here once customer raises the 'waiving' event
    print('waiter: someone is waiving - no more waiting')
    print('waiter: May I take your order')
    time.sleep(1)
    print('waiter: done')

threads = [
    threading.Thread(target=customer),
    threading.Thread(target=waiter),
]
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
