"""
A multi processing version of race_conditions.py

Because each process works in their own space,
there is no race condition,
but neither is the counter[0] in the main Python process' memory increased
"""
import multiprocessing

counter = {x: 0 for x in range(10)}

def plus_many():
    # Each process has it's own copy of counter,
    # which is {0:0, 1:0, etc} at the time the copy is made
    start = counter[0]
    for _ in range(100_000):
        counter[0] += 1

    # This prints out 
    # from 0 to 100000
    # for all 10 processes
    print(f'from {start} to {counter[0]}')

processes = []
for _ in range(10):
    process = multiprocessing.Process(target=plus_many)
    process.start()
    processes.append(process)

for process in processes:
    process.join()

# This prints out 0
print(f'Result: {counter[0]}')
