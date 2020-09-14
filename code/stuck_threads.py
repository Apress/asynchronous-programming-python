"""
The main thread finishes
whilst the sub threads never finish

Note how Python continues to wait until all threads are done
which in this case never happens

You'll need to abort it manually
"""

import threading
import time

def stuck_function():
    print('Started')
    while True:
        time.sleep(0.1)
    print('Thread done')

def main():
    for _ in range(5):
        threading.Thread(target=stuck_function).start()
    print('Main done')

def test_main():
    main()
    time.sleep(60)

main()
