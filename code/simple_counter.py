"""
A simple counting example
Works fine as a single thread and single process
but gives strange results with multiple threads or processes
See race_conditions.py and race_conditions_with_processes.py
"""

counter = {x: 0 for x in range(10)}

def plus_many():
    for _ in range(100_000):
        counter[0] += 1

for _ in range(10):
    plus_many()

print(f'Result: {counter[0]}')
