# Advent of code Year 2024 Day 15 solution
# Author = Drew Blocki
# Date = December 2024

with open((__file__.rstrip("one.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

rounds = input.strip().split("\n\n")
map, moves = rounds[:2]

directionMap = {
    '^': -1,
    'v': 1,
    '<': -1j,
    '>': 1j,
}

def printMap(height, width, boxes, walls):
    for i in range(height):
        line = ''
        for j in range(width):
            loc = i + j * 1j
            if robot == loc:
                line += '@'
            elif loc in walls:
                line += '#'
            elif loc in boxes:
                line += 'O'
            else:
                line += '.'
        print(line)
    print()

def readInput(map):
    boxes, walls = set(), set()
    for rowIndex, line in enumerate(map.splitlines()):
        for colIndex, char in enumerate(line):
            loc = rowIndex + colIndex * 1j
            if char == '@':
                robot = loc
            elif char == '#':
                walls.add(loc)
            elif char == 'O':
                boxes.add(loc)
    return boxes, walls, robot

boxes, walls, robot = readInput(map)
height, width = len(map.splitlines()), len(map.splitlines()[0])

for line in moves.splitlines():
    for instr in line:
        delta = directionMap[instr]
        searchVec = robot + delta
        while searchVec in boxes:
            searchVec += delta
        if searchVec not in walls:
            if robot + delta in boxes:
                boxes.add(searchVec)
                boxes.remove(robot + delta)
            robot = robot + delta
        # printMap(height, width, boxes, walls)

sum = 0
for box in boxes:
    sum += int(100 * box.real + box.imag)

print(f'SUM: {sum}')
