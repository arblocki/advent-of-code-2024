# Advent of code Year 2024 Day 3 solution
# Author = Drew Blocki
# Date = December 2024

import re

with open((__file__.rstrip("main.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

# PART 1
print('PART 1')
mulPattern = r"mul\((\d+),(\d+)\)"
matches = re.findall(mulPattern, input)
mulPairs = [(int(x), int(y)) for x, y in matches]

sum = 0
for x, y in mulPairs:
    sum += x * y

print(f'  SUM: {sum}')


# PART 2
print('PART 2')
doPattern = r"do\(\)"
dontPattern = r"don\'t\(\)"

doIndices = []
dontIndices = []
for match in re.finditer(doPattern, input):
    doIndices.append(match.start(0))
for match in re.finditer(dontPattern, input):
    dontIndices.append(match.start(0))
    
# Pair up don't indices with following do's to create disabled ranges
disabledPairs = []
for dontIndex in dontIndices:
    nextDoIndex = -1
    for doIndex in doIndices:
        if doIndex > dontIndex:
            nextDoIndex = doIndex
            break
    disabledPairs.append((dontIndex, nextDoIndex))

# Only add mul's to sum if they are not in a disabled range
matches = re.finditer(mulPattern, input)
sum = 0
for match in matches:
    start = match.start(0)
    disabled = False
    for pair in disabledPairs:
        if start > pair[0]:
            if start < pair[1] or pair[1] == -1:
                disabled = True
                break
    if disabled:
        continue       
    x = match.group(1)
    y = match.group(2)
    sum += int(x) * int(y)

print(f'  SUM: {sum}')
