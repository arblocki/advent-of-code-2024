# Advent of code Year 2024 Day 20 solution
# Author = Drew Blocki
# Date = December 2024

import sys
from copy import copy

with open((__file__.rstrip("main.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

walls = set()
start = 0
end = 0

MAX = sys.maxsize

# cheats = set()

h = len(input.splitlines())
w = len(input.splitlines()[0])
for i, line in enumerate(input.splitlines()):
    for j, char in enumerate(line):
        vec = i + j * 1j
        if char == '#':
            walls.add(i + j * 1j)
        elif char == 'S':
            start = vec
        elif char == 'E':
            end = vec

def findScores(curr, currScore, visited):
    global walls, end, bestMap
    visited.add(curr)
    if curr in bestMap:
        bestMap[curr] = min(currScore, bestMap[curr])
    else:
        bestMap[curr] = currScore
    if curr == end:
        return

    d = 1
    for _ in range(4):
        next = curr + d
        # if next in walls:
        #     if next + d not in walls:
        #         cheats.add((curr, next + d))
        if next not in walls and next not in visited:
            visit_copy = copy(visited)
            searchList.insert(0, [next, currScore + 1, visit_copy])
        d *= -1j

visited = set()
bestMap = {}
searchList = [[start, 0, visited]]
while len(searchList) != 0:
    nextSearch = searchList.pop(0)
    loc = nextSearch[0]
    score = nextSearch[1]
    bestLocScore = bestMap.get(loc, MAX)
    if score > bestLocScore:
        continue
    findScores(*nextSearch)

# cheatCounter = {}
# for cheat in cheats:
#     if cheat[1] not in bestMap or cheat[0] not in bestMap:
#         continue
#     diff = bestMap[cheat[1]] - bestMap[cheat[0]] - 2
#     if diff > 0:
#         if diff in cheatCounter:
#             cheatCounter[diff] += 1
#         else:
#             cheatCounter[diff] = 1

total = 0
for i in range(h):
    for j in range(w):
        for i2 in range(i-20, i+21):
            for j2 in range(j-20, j+21):
                loc1 = i + j * 1j
                loc2 = i2 + j2 * 1j
                dist = abs((loc1 - loc2).real) + abs((loc1 - loc2).imag)
                if dist > 20:
                    continue
                if loc1 not in bestMap or loc2 not in bestMap:
                    continue
                if dist + 100 <= bestMap[loc1] - bestMap[loc2]:
                    total += 1

print(f'TOTAL: {total}')

# sum = 0
# for pico, count in cheatCounter.items():
#     # print(f'There are {cheatCounter[i]} cheats that save {i} picoseconds.')
#     if pico >= 100:
#         sum += count
