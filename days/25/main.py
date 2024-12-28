# Advent of code Year 2024 Day 25 solution
# Author = Drew Blocki
# Date = December 2024

with open((__file__.rstrip("main.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

segments = input.strip().split("\n\n")

locks = []
keys = []

for segment in segments:
    lock = True
    if segment[0] == '.':
        lock = False
    val = [0] * 5
    for row, line in enumerate(segment.splitlines()[1:]):
        for col, char in enumerate(line):
            if lock and char == '#':
                val[col] += 1
            elif not lock and char == '#' and val[col] == 0:
                val[col] = 5 - row
    if lock:
        locks.append(val)
    else:
        keys.append(val)

sum = 0
for lock in locks:
    for key in keys:
        valid = True
        for i in range(5):
            if lock[i] + key[i] > 5:
                valid = False
                break
        if valid:
            sum += 1

print(f'SUM: {sum}')
