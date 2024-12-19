# Advent of code Year 2024 Day 16 solution
# Author = Drew Blocki
# Date = December 2024

import math
import sys

from copy import copy

with open((__file__.rstrip("main.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

MAX = sys.maxsize

def printMap(walls, start, end, visited, width, height):
    for i in range(height):
        line = ''
        for j in range(width):
            loc = i + j * 1j
            if loc in walls:
                line += '#'
            elif loc == start:
                line += 'S'
            elif loc == end:
                line += 'E'
            elif loc in visited:
                line += 'O'
            else: 
                line += '.'
        print(line)

bestSet = set()
bestScore = 93436
    
def findBestPathScore(walls, curr, direction, end, currScore, visited):
    global bestSet, bestScore
    if curr == end:
        print(f'\t\tFOUND SCORE: {currScore}')
        if currScore == bestScore:
            bestSet.update(visited)
        elif currScore < bestScore:
            bestSet.clear()
            bestSet.update(visited)
            bestScore = currScore
        return
    visited.add(curr)
    bestMap[(curr, direction)] = currScore

    d = direction
    for _ in range(4):
        next = curr + d
        if next not in walls and next not in visited:
            visit_copy = copy(visited)
            nextScore = currScore + 1
            if d != direction:
                nextScore += 1000
            searchList.insert(0, [walls, next, d, end, nextScore, visit_copy])
        d *= -1j

walls = set()
for rowIndex, line in enumerate(input.splitlines()):
    for colIndex, char in enumerate(line):
        loc = rowIndex + colIndex* 1j
        if char == '#':
            walls.add(loc)
        elif char == 'S':
            start = loc
        elif char == 'E':
            end = loc

visited = set()
bestMap = {}
direction = 1j
searchList = [[walls, start, direction, end, 0, visited]]
index = 1
while len(searchList) != 0:
    index += 1
    nextSearch = searchList.pop(0)
    score = nextSearch[4]
    loc = nextSearch[1]
    direction = nextSearch[2]
    bestLocScore = bestMap.get((loc, direction), MAX)
    if score > bestScore:
        continue
    # Check if score at this loc is greater than the best we've seen at this location before
    elif score > bestLocScore:
        continue
    findBestPathScore(*nextSearch)
    if index % 10000 == 0:
        print(f'\tSEARCHES LEFT: {len(searchList)}')
bestSet.add(start)
bestSet.add(end)

print(f'BEST PATH SCORE: {bestScore}')
print(f'BEST PATH SIZE: {len(bestSet)}')

# printMap(walls, start, end, bestSet, len(input.splitlines()[0]), len(input.splitlines()))
