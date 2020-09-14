"""
A deadlock example
"""

import threading, time, random

fork = threading.Lock()
spoon = threading.Lock()

# The first eater (wether fork_first or spoon_first)
# gets both locks in the brief delay whilst the next threads are started


def fork_first():
    # After that, a fork_first eater will pick up a fork and wait for a spoon
    with fork, spoon:
            print('Picked up cutlery, eating')
            time.sleep(0.1)
            print('Done eating')

def spoon_first():
    # And a spoon_first eater will pick up a spoon and wait for a fork
    with spoon, fork:
            print('Picked up cutlery, eating')
            time.sleep(0.1)
            print('Done eating')

threads = []
for _ in range(10):
    eater = random.choice((fork_first, spoon_first))
    threads.append(threading.Thread(target=eater))
print('Everyone arrived')

for thread in threads:
    thread.start()
print('Everyone has started their meal')

for thread in threads:
    # Only the first thread will finish
    # The others are stuck (deadlock) waiting for each other
    thread.join()

print(f'All done eating')
