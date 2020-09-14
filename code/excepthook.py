"""
An example of using threading.excepthook
to process (e.g. log) errors in threads
"""

import threading

def broken_function():
    raise ValueError('Something is wrong')

def log_missed_thread_exception(args):
    """ When called, print out the (error) arguments"""
    exc_type, exc_value, exc_traceback, thread = args
    print('An error was detected in thread', thread.name)
    print('Type: ', exc_type)
    print('Value: ', exc_value)

def main():
    # When exception is raised in a thread
    # (and it is not handled, e.g. in an except: block)
    # pass it to the log_missed_thread_exception function
    threading.excepthook = log_missed_thread_exception

    # Start the thread, which will raise an error
    threading.Thread(target=broken_function).start()

main()
