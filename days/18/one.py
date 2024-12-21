# Advent of code Year 2024 Day 18 solution part 1
# Author = Drew Blocki
# Date = December 2024

import sys

suffix = ''

with open((__file__.rstrip("main.py")+f'input{suffix}.txt'), 'r') as input_file:
    input = input_file.read()

SIZE = 70 if suffix == '' else 6
NUM_BYTES = 1024 if suffix == '' else 12

corrupted = set()

for line in input.splitlines()[:NUM_BYTES]:
    coordinates = line.split(',')
    x, y = int(coordinates[0]), int(coordinates[1])
    corrupted.add(x + y * 1j)

visited = set()
bestScore = sys.maxsize

searchList = [(0, 0)]

def findBestPath(curr, score):
    global SIZE, corrupted, searchList, bestScore, visited
    if curr == SIZE + SIZE * 1j:
        if score + 1 < bestScore:
            bestScore = score
        return 
    if curr in visited:
        return
    visited.add(curr)
    if score > bestScore:
        return
    d = 1
    for _ in range(4):
        next = curr + d
        if not (next.real < 0 or next.real > SIZE or next.imag < 0 or next.imag > SIZE) \
        and next not in visited and next not in corrupted:
            searchList.append((next, score + 1))
        d *= -1j

while len(searchList) != 0:
    next = searchList.pop(0)
    findBestPath(*next)
    
print(f'BEST SCORE: {bestScore}')
    
