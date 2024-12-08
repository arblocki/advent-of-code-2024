# Advent of code Year 2024 Day 4 solution
# Author = Drew Blocki
# Date = December 2024

with open((__file__.rstrip("main.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

def getChar(map, row, col):
    if row < 0 or row >= len(map):
        return '.'
    if col < 0 or col >= len(map[0]):
        return '.'
    return map[row][col]

# PART 1
print('PART 1')

# Can be multiple in different directions, so return an int
def checkForXmas(map, row, col):
    sum = 0
    # Up
    if getChar(map, row-1, col) == 'M' \
    and getChar(map, row-2, col) == 'A' \
    and getChar(map, row-3, col) == 'S':
        sum += 1
    # Down
    if getChar(map, row+1, col) == 'M' \
    and getChar(map, row+2, col) == 'A' \
    and getChar(map, row+3, col) == 'S':
        sum += 1
    # Left
    if getChar(map, row, col-1) == 'M' \
    and getChar(map, row, col-2) == 'A' \
    and getChar(map, row, col-3) == 'S':
        sum += 1
    # Right
    if getChar(map, row, col+1) == 'M' \
    and getChar(map, row, col+2) == 'A' \
    and getChar(map, row, col+3) == 'S':
        sum += 1
    # UpRight
    if getChar(map, row-1, col+1) == 'M' \
    and getChar(map, row-2, col+2) == 'A' \
    and getChar(map, row-3, col+3) == 'S':
        sum += 1
    # DownRight
    if getChar(map, row+1, col+1) == 'M' \
    and getChar(map, row+2, col+2) == 'A' \
    and getChar(map, row+3, col+3) == 'S':
        sum += 1
    # UpLeft
    if getChar(map, row-1, col-1) == 'M' \
    and getChar(map, row-2, col-2) == 'A' \
    and getChar(map, row-3, col-3) == 'S':
        sum += 1
    # DownLeft
    if getChar(map, row+1, col-1) == 'M' \
    and getChar(map, row+2, col-2) == 'A' \
    and getChar(map, row+3, col-3) == 'S':
        sum += 1
    return sum

searchMap = []
for line in input.splitlines():
    searchMap.append(line)

xCoords = []
for rowIndex, line in enumerate(searchMap):
    for colIndex, char in enumerate(line):
        if char == 'X':
            xCoords.append((rowIndex, colIndex))

totalSum = 0
for x, y in xCoords:
    totalSum += checkForXmas(searchMap, x, y)

print(f'  TOTAL XMAS: {totalSum}')

# PART 2
print('PART 2')

def checkForMASX(map, row, col):
    # Up
    if getChar(map, row-1, col-1) == 'M' \
    and getChar(map, row-1, col+1) == 'M' \
    and getChar(map, row+1, col-1) == 'S' \
    and getChar(map, row+1, col+1) == 'S':
        return 1
    # Down
    if getChar(map, row-1, col-1) == 'S' \
    and getChar(map, row-1, col+1) == 'S' \
    and getChar(map, row+1, col-1) == 'M' \
    and getChar(map, row+1, col+1) == 'M':
        return 1
    # Left
    if getChar(map, row-1, col-1) == 'M' \
    and getChar(map, row-1, col+1) == 'S' \
    and getChar(map, row+1, col-1) == 'M' \
    and getChar(map, row+1, col+1) == 'S':
        return 1
    # Right
    if getChar(map, row-1, col-1) == 'S' \
    and getChar(map, row-1, col+1) == 'M' \
    and getChar(map, row+1, col-1) == 'S' \
    and getChar(map, row+1, col+1) == 'M':
        return 1
    return 0

aCoords = []
for rowIndex, line in enumerate(searchMap):
    for colIndex, char in enumerate(line):
        if char == 'A':
            aCoords.append((rowIndex, colIndex))

totalSum = 0
for x, y in aCoords:
    totalSum += checkForMASX(searchMap, x, y)

print(f'  TOTAL X-MAS: {totalSum}')
