# Advent of code Year 2024 Day 6 solution
# Author = Drew Blocki
# Date = December 2024

from copy import deepcopy

with open((__file__.rstrip("main.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

# PART 1
print('PART 1')
# def oldCode():
#     map = []
#     index = 0
#     for line in input.splitlines():
#         map.append([])
#         for char in line:
#             map[index].append(char)
#         index += 1

#     guard = '^'
#     obstacle = '#'
#     orientation = 'U'
#     orientationMap = {
#         'U': 'R',
#         'R': 'D',
#         'D': 'L',
#         'L': 'U'
#     }
#     marker = 'X'

#     guardRow = -1
#     guardCol = -1
#     for rowIndex, row in enumerate(map):
#         try:
#             guardCol = row.index(guard)
#             guardRow = rowIndex
#             break
#         except ValueError:
#             continue
#     map[guardRow][guardCol] = marker

#     def isOOB(row, col):
#         if row < 0 or row >= len(map) or col < 0 or col >= len(map[0]):
#             return True
#         return False

#     def getSpace(row, col):
#         if isOOB(row, col):
#             return 'OOB'
#         if map[row][col] == obstacle:
#             return '#'

#     def move(map, guardRow, guardCol, orientation):
#         nextRow = guardRow
#         nextCol = guardCol
#         if orientation == 'U':
#             nextRow = guardRow - 1
#         elif orientation == 'D':
#             nextRow = guardRow + 1
#         elif orientation == 'R':
#             nextCol = guardCol + 1
#         elif orientation == 'L':
#             nextCol = guardCol - 1
        
#         nextSpace = getSpace(nextRow, nextCol)
#         if nextSpace == '#':
#             orientation = orientationMap[orientation]
#         else:
#             guardCol = nextCol
#             guardRow = nextRow
            
#         if nextSpace != 'OOB':
#             map[nextRow][nextCol] = marker

#         return map, guardRow, guardCol, orientation

#     onMap = True
#     while onMap:
#         map, guardRow, guardCol, orientation = move(map, guardRow, guardCol, orientation)
#         onMap = isOOB(guardRow, guardCol)

class GuardSimulation:
    def __init__(self, input):
        self.map = [list(line) for line in input.splitlines()]
        self.orientation = 'U'
        self.orientation_map = {
            'U': 'R',
            'R': 'D',
            'D': 'L',
            'L': 'U'
        }
        self.marker = 'X'
        self.obstacle = '#'
        self.guard = '^'
        self.guard_row, self.guard_col = self._find_guard()
        self.map[self.guard_row][self.guard_col] = self.marker
        self.rotationPositions = set()

    def _find_guard(self):
        for row_index, row in enumerate(self.map):
            try:
                col_index = row.index(self.guard)
                return row_index, col_index
            except ValueError:
                continue
        raise ValueError("Guard not found in map.")

    def is_oob(self, row, col):
        return row < 0 or row >= len(self.map) or col < 0 or col >= len(self.map[0])

    def get_space(self, row, col):
        if self.is_oob(row, col):
            return 'OOB'
        return self.map[row][col]

    def move(self, checkForLoops):
        next_row, next_col = self.guard_row, self.guard_col

        if self.orientation == 'U':
            next_row -= 1
        elif self.orientation == 'D':
            next_row += 1
        elif self.orientation == 'R':
            next_col += 1
        elif self.orientation == 'L':
            next_col -= 1

        next_space = self.get_space(next_row, next_col)

        if next_space == self.obstacle:
            self.orientation = self.orientation_map[self.orientation]
            if checkForLoops:
                rotationPosition = f'{self.guard_row}-{self.guard_col}-{self.orientation}'
                if rotationPosition in self.rotationPositions:
                    return True
                else:
                    self.rotationPositions.add(rotationPosition)
        else:
            self.guard_row, self.guard_col = next_row, next_col
            if next_space != 'OOB':
                self.map[next_row][next_col] = self.marker

    def run_simulation(self):
        while not self.is_oob(self.guard_row, self.guard_col):
            self.move(False)
            
    def run_loop_simulation(self):
        initialPosition = f'{self.guard_row}-{self.guard_col}-{self.orientation}'
        self.rotationPositions.add(initialPosition)
        while not self.is_oob(self.guard_row, self.guard_col):
            loopEncountered = self.move(True)
            if loopEncountered:
                return True

simulation = GuardSimulation(input)
init_simulation = deepcopy(simulation)
simulation.run_simulation()
sum = 0
xSpots = []
for rowIndex, row in enumerate(simulation.map):
    line = ''
    for colIndex, col in enumerate(row):
        line += col
        if col == 'X':
            xSpots.append((rowIndex, colIndex))
            sum += 1
    print(line)
print(f'SUM: {sum}\n')

# PART 2
print('PART 2')
totalLoopScenarios = 0
for xSpot in xSpots:
    row = xSpot[0]
    col = xSpot[1]
    print(f'ADDING OBSTACLE AT ({row}, {col})')
    simulationCopy = deepcopy(init_simulation)
    simulationCopy.map[row][col] = '#'
    loopEncountered = simulationCopy.run_loop_simulation()
    if loopEncountered:
        # print(f'LOOP ENCOUNTERED AT ({row}, {col})')
        totalLoopScenarios += 1
print(f'TOTAL LOOP SCENARIOS: {totalLoopScenarios}')
