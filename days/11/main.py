# Advent of code Year 2024 Day 11 solution
# Author = Drew Blocki
# Date = December 2024

from copy import copy

with open((__file__.rstrip("main.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

def parseInput(input):
    nums = [int(numStr) for numStr in input.split(' ')]
    return nums

def addStoneCount(newStoneCount, stone, amount):
    if stone in newStoneCount:
        newStoneCount[stone] += amount
    else:
        newStoneCount[stone] = amount

class EvolvingStones:
    def __init__(self, stones):
        self.stoneCount = {}
        for stone in stones:
            if stone in self.stoneCount:
                self.stoneCount[stone] += 1
            else:
                self.stoneCount[stone] = 1

    def blink(self):
        newStoneCount = {}
        for stone, count in self.stoneCount.items():
            if stone == 0:
                addStoneCount(newStoneCount, 1, count)
            elif len(str(stone)) % 2 == 0:
                stoneStr = str(stone)
                midCutIndex = int(len(stoneStr) / 2)
                firstHalf = int(stoneStr[:midCutIndex])
                addStoneCount(newStoneCount, firstHalf, count)
                secondHalf = int(stoneStr[midCutIndex:])
                addStoneCount(newStoneCount, secondHalf, count)
            else:
                addStoneCount(newStoneCount, stone * 2024, count)
        self.stoneCount = newStoneCount
    
    def getStoneCount(self):
        sum = 0
        for _, count in self.stoneCount.items():
            sum += count
        return sum
    
    def printStoneCounts(self):
        for stone, count in self.stoneCount.items():
            print(f'\t\t{stone}: {count}')

# PART 1
print('PART 1')
stones = EvolvingStones(parseInput(input))
for i in range(25):
    stones.blink()
print(f'STONES: {stones.getStoneCount()}')

# PART 2
print('PART 2')
stones = EvolvingStones(parseInput(input))
for i in range(75):
    stones.blink()
print(f'STONES: {stones.getStoneCount()}')
