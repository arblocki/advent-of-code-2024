# Advent of code Year 2024 Day 14 solution
# Author = Drew Blocki
# Date = December 2024

import re
import math

with open((__file__.rstrip("main.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

pattern = r"p=(\d+),(\d+)\s+v=(\-?\d+),(\-?\d+)"

def parseRobots(input):
    robots = []
    for index, line in enumerate(input.splitlines()):
        if index == 0:
            dims = line.split()
            xLen = int(dims[0])
            yLen = int(dims[1])
            continue
        match = re.match(pattern, line)
        px, py, vx, vy = map(int, match.groups())
        robots.append((px, py, vx, vy))
    return robots, xLen, yLen

def iterateRobots(robots, xLen, yLen):
    for index, robot in enumerate(robots):
        px, py, vx, vy = robot[:4]
        
        newPx = px + vx
        if newPx < 0:
            newPx += xLen
        elif newPx >= xLen:
            newPx -= xLen
            
        newPy = py + vy
        if newPy < 0:
            newPy += yLen
        elif newPy >= yLen:
            newPy -= yLen
            
        robots[index] = (newPx, newPy, vx, vy)
    return robots

def checkForTree(robots):
    threshold = math.floor(math.sqrt(len(robots)))
    locSet = set()
    for robot in robots:
        locSet.add((robot[0], robot[1]))
    clusteredRobots = 0
    for robot in robots:
        x, y = robot[0], robot[1]
        if (x-1, y) in locSet and (x+1,y) in locSet and (x,y-1) in locSet and (x,y+1) in locSet:
            clusteredRobots += 1
    return clusteredRobots > threshold

def printLocations(robots):
    for robot in robots:
        print(f'\tLOCATION: {robot[0]}, {robot[1]}')
        
def printMap(robots, xLen, yLen):
    locSet = set()
    for robot in robots:
        locSet.add((robot[0], robot[1]))
    for i in range(yLen):
        line = ''
        for j in range(xLen):
            if (j, i) in locSet:
                line += '*'
            else:
                line += '.'
        print(line)

def calculateSafetyFactor(robots, xLen, yLen):
    xMid = xLen // 2
    yMid = yLen // 2
    safety = [0, 0, 0, 0]
    for robot in robots:
        x = robot[0]
        y = robot[1]
        if x < xMid:
            if y < yMid:
                safety[0] += 1
            elif y > yMid:
                safety[2] += 1
        elif x > xMid:
            if y < yMid:
                safety[1] += 1
            elif y > yMid:
                safety[3] += 1
    return math.prod(safety)

print('PART 2')
robots, xLen, yLen = parseRobots(input)
for i in range(8186):
    print(f'\t{i}')
    robots = iterateRobots(robots, xLen, yLen)
    if checkForTree(robots):
        printMap(robots, xLen, yLen)
        print(f'FOUND TREE AFTER {i} SECONDS')
        break
print(f'SAFETY FACTOR: {calculateSafetyFactor(robots, xLen, yLen)}')


