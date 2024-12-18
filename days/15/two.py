# Advent of code Year 2024 Day 15 solution Part 2
# Author = Drew Blocki
# Date = December 2024

with open((__file__.rstrip("two.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

rounds = input.strip().split("\n\n")
map, moves = rounds[:2]

directionMap = {
    '^': -1,
    'v': 1,
    '<': -1j,
    '>': 1j,
}

def printMap(height, width, boxes, uniqueBoxes, walls):
    for i in range(height):
        line = ''
        for j in range(width):
            loc = i + j * 1j
            if robot == loc:
                line += '@'
            elif loc in walls:
                line += '#'
            elif loc in boxes:
                left = uniqueBoxes[loc][0] == loc
                if left:
                    line += '['
                else:
                    line += ']'
            else:
                line += '.'
        print(line)
    print()

def readInput(map):
    boxes, walls = set(), set()
    uniqueBoxes = {}
    for rowIndex, line in enumerate(map.splitlines()):
        for colIndex, char in enumerate(line):
            loc = rowIndex + colIndex * 2j
            if char == '@':
                robot = loc
            elif char == '#':
                walls.add(loc)
                walls.add(loc + 1j)
            elif char == 'O':
                leftIndex = loc
                rightIndex = loc + 1j
                boxes.update([leftIndex, rightIndex])
                fullBox = (leftIndex, rightIndex)
                uniqueBoxes[leftIndex] = fullBox
                uniqueBoxes[rightIndex] = fullBox
    return boxes, uniqueBoxes, walls, robot

def getBoxGroup(boxes, uniqueBoxes, delta, start):
    if start + delta not in boxes:
        if start + delta in walls:
            return None
        else: 
            return set()
    
    boxGroup = set()
    # Left/right move
    if delta.real == 0:
        searchVec = start + delta
        while searchVec in boxes:
            boxGroup.add(uniqueBoxes[searchVec])
            searchVec += delta
        if searchVec in walls:
            return None
    else:
        fullBox = uniqueBoxes[start + delta]
        boxGroup.add(fullBox)
        leftBoxes = getBoxGroup(boxes, uniqueBoxes, delta, fullBox[0])
        rightBoxes = getBoxGroup(boxes, uniqueBoxes, delta, fullBox[1])
        if leftBoxes is None or rightBoxes is None:
            return None
        boxGroup.update(leftBoxes)
        boxGroup.update(rightBoxes)
    return boxGroup

boxes, uniqueBoxes, walls, robot = readInput(map)
height, width = len(map.splitlines()), len(map.splitlines()[0]) * 2

# printMap(height, width, boxes, uniqueBoxes, walls)

for line in moves.splitlines():
    for instr in line:
        delta = directionMap[instr]
        searchVec = robot + delta
        if searchVec not in walls:
            if searchVec not in boxes:
                robot += delta
            else:
                boxesToMove = getBoxGroup(boxes, uniqueBoxes, delta, robot)
                if boxesToMove is None:
                    continue
                for fullBox in boxesToMove:
                    uniqueBoxes.pop(fullBox[0], None)
                    uniqueBoxes.pop(fullBox[1], None)
                    boxes.remove(fullBox[0])
                    boxes.remove(fullBox[1])
                for fullBox in boxesToMove:
                    newBoxLeft = fullBox[0] + delta
                    newBoxRight = fullBox[1] + delta
                    newBox = (newBoxLeft, newBoxRight)
                    uniqueBoxes[newBoxLeft] = newBox
                    uniqueBoxes[newBoxRight] = newBox
                    boxes.add(newBoxLeft)
                    boxes.add(newBoxRight)
                robot += delta
        # printMap(height, width, boxes, uniqueBoxes, walls)

sum = 0
countedBoxes = set()
for index, box in uniqueBoxes.items():
    if box not in countedBoxes:
        sum += int(100 * box[0].real + box[0].imag)
        countedBoxes.add(box)

print(f'SUM: {sum}')
