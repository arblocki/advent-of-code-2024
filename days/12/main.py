# Advent of code Year 2024 Day 12 solution
# Author = Drew Blocki
# Date = December 2024

with open((__file__.rstrip("main.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

class Garden:
    def __init__(self, input):
        self.garden = []
        self.checkedPlants = set()
        for line in input.splitlines():
            nextRow = []
            for plant in line:
                nextRow.append(plant)
            self.garden.append(nextRow)
        self.rows = len(self.garden)
        self.cols = len(self.garden[0])
    
    def calculatePerimeter(self, row, col):
        val = self.garden[row][col]
        perimeter = 4
        if row - 1 >= 0 and self.garden[row-1][col] == val:
            perimeter -= 1
        if row + 1 < self.rows and self.garden[row+1][col] == val:
            perimeter -= 1
        if col - 1 >= 0 and self.garden[row][col-1] == val:
            perimeter -= 1
        if col + 1 < self.cols and self.garden[row][col+1] == val:
            perimeter -= 1
        return perimeter
    
    def calculateRegionCost(self, row, col):
        val = self.garden[row][col]
        self.checkedPlants.add((row, col))
        perimeter = self.calculatePerimeter(row, col)
        area = 1
        sides = set()
        # Up
        if row - 1 >= 0:
            if self.garden[row-1][col] == val:
                if (row-1, col) not in self.checkedPlants:
                    nextArea, nextPerim, nextSides = self.calculateRegionCost(row-1, col)
                    area += nextArea
                    perimeter += nextPerim
                    sides.update(nextSides)
            else:
                sides.add((row, col, 'U'))
        else:
            sides.add((row, col, 'U'))
        
        # Down
        if row + 1 < self.rows:
            if self.garden[row+1][col] == val:
                if (row+1, col) not in self.checkedPlants:
                    nextArea, nextPerim, nextSides = self.calculateRegionCost(row+1, col)
                    area += nextArea
                    perimeter += nextPerim
                    sides.update(nextSides)
            else:
                sides.add((row, col, 'D'))
        else:
            sides.add((row, col, 'D'))
            
        # Left
        if col - 1 >= 0:
            if self.garden[row][col-1] == val:
                if (row, col-1) not in self.checkedPlants:
                    nextArea, nextPerim, nextSides = self.calculateRegionCost(row, col-1)
                    area += nextArea
                    perimeter += nextPerim
                    sides.update(nextSides)
            else:
                sides.add((row, col, 'L'))
        else:
            sides.add((row, col, 'L'))
            
        # Right
        if col + 1 < self.cols:
            if self.garden[row][col+1] == val:
                if (row, col+1) not in self.checkedPlants:
                    nextArea, nextPerim, nextSides = self.calculateRegionCost(row, col+1)
                    area += nextArea
                    perimeter += nextPerim
                    sides.update(nextSides)
            else:
                sides.add((row, col, 'R'))
        else:
            sides.add((row, col, 'R'))
        return area, perimeter, sides
        
    
    def calculateTotalCost(self):
        totalCost = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if (row, col) not in self.checkedPlants:
                    area, perim, _ = self.calculateRegionCost(row, col)
                    totalCost += area * perim
        return totalCost
    
    def calculateTotalBulkCost(self):
        totalCost = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if (row, col) not in self.checkedPlants:
                    area, _, sides = self.calculateRegionCost(row, col)
                    dupSet = set()
                    for sideRow, sideCol, direction in sides:
                        if (sideRow, sideCol, direction) in dupSet:
                            continue
                        if direction == 'L' or direction == 'R':
                            searchUpRow = sideRow - 1
                            while (searchUpRow, sideCol, direction) in sides:
                                dupSet.add((searchUpRow, sideCol, direction))
                                searchUpRow -= 1
                            searchDownRow = sideRow + 1
                            while (searchDownRow, sideCol, direction) in sides:
                                dupSet.add((searchDownRow, sideCol, direction))
                                searchDownRow += 1
                        if direction == 'U' or direction == 'D':
                            searchLeftCol = sideCol - 1
                            while (sideRow, searchLeftCol, direction) in sides:
                                dupSet.add((sideRow, searchLeftCol, direction))
                                searchLeftCol -= 1
                            searchRightCol = sideCol + 1
                            while (sideRow, searchRightCol, direction) in sides:
                                dupSet.add((sideRow, searchRightCol, direction))
                                searchRightCol += 1
                    cost = area * len(sides - dupSet)
                    totalCost += cost
        return totalCost

# PART 1
print('PART 1')
garden = Garden(input)
totalCost = garden.calculateTotalCost()
print(f'TOTAL COST: {totalCost}')

# PART 2
print('PART 2')
bulkGarden = Garden(input)
totalBulkCost = bulkGarden.calculateTotalBulkCost()
print(f'TOTAL BULK COST: {totalBulkCost}')
