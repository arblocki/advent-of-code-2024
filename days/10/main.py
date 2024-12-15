# Advent of code Year 2024 Day 10 solution
# Author = Drew Blocki
# Date = December 2024

with open((__file__.rstrip("main.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

def readInput(input):
    map = []
    trailHeads = []
    for rowIndex, line in enumerate(input.splitlines()):
        nextRow = []
        for colIndex, numStr in enumerate(line):
            num = int(numStr)
            nextRow.append(num)
            if num == 0:
                trailHeads.append((rowIndex, colIndex))
        map.append(nextRow)
    return map, trailHeads

class HikingPathFinder:
    def __init__(self, map):
        self.map = map
        self.peaks = set()
        self.distinctTrails = 0
    
    def searchForPeaks(self, coord):
        row = coord[0]
        col = coord[1]
        value = self.map[row][col]
        # Recurse on each direction if they are inbounds and greater by 1
        # UP
        if row-1 >= 0 and self.map[row-1][col] - value == 1:
            if self.map[row-1][col] == 9:
                if (row-1, col) not in self.peaks:
                    self.peaks.add((row-1, col))
                self.distinctTrails += 1
            else:
                self.searchForPeaks((row-1, col))
        # DOWN
        if row+1 < len(self.map) and self.map[row+1][col] - value == 1:
            if self.map[row+1][col] == 9:
                if (row+1, col) not in self.peaks:
                    self.peaks.add((row+1, col))
                self.distinctTrails += 1
            else:
                self.searchForPeaks((row+1, col))
        # RIGHT
        if col+1 < len(self.map[0]) and self.map[row][col+1] - value == 1:
            if self.map[row][col+1] == 9:
                if (row, col+1) not in self.peaks:
                    self.peaks.add((row, col+1))
                self.distinctTrails += 1
            else:
                self.searchForPeaks((row, col+1))
        # LEFT
        if col-1 >= 0 and self.map[row][col-1] - value == 1:
            if self.map[row][col-1] == 9:
                if (row, col-1) not in self.peaks:
                    self.peaks.add((row, col-1))
                self.distinctTrails += 1
            else:
                self.searchForPeaks((row, col-1))
    
    def getPeakScore(self):
        return len(self.peaks)
    
    def getDistinctTrails(self):
        return self.distinctTrails


# PART 1
print('PART 1')
map, trailHeads = readInput(input)
totalScore = 0
totalDistinctTrails = 0
for trailhead in trailHeads:
    finder = HikingPathFinder(map)
    finder.searchForPeaks(trailhead)
    totalScore += finder.getPeakScore()
    totalDistinctTrails += finder.getDistinctTrails()
print(f'TOTAL SCORE: {totalScore}')

# PART 2
print('PART 2')
print(f'TOTAL DISTINCT TRAILS: {totalDistinctTrails}')
