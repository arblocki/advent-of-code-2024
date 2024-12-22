# Advent of code Year 2024 Day 21 solution
# Author = Drew Blocki
# Date = December 2024

import sys

with open((__file__.rstrip("main.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

NUM_MAP = {
    '7': 0,
    '8': 1j,
    '9': 2j,
    '4': 1,
    '5': 1 + 1j,
    '6': 1 + 2j,
    '1': 2,
    '2': 2 + 1j,
    '3': 2 + 2j,
    '0': 3 + 1j,
    'A': 3 + 2j, 
    'E': 3,
}

DIREC_MAP = {
    '^': 1j,
    'A': 2j,
    '<': 1,
    'v': 1 + 1j,
    '>': 1 + 2j,
    'E': 0,
}

def trimInputsByLen(inputs):
    finalInputs = set()
    minLen = sys.maxsize
    for input in inputs:
        minLen = min(minLen, len(input))
    for input in inputs:
        if len(input) > minLen:
            continue
        finalInputs.add(input)
    return finalInputs, minLen

def getInputsForNumbers(string):
    currentInputs = set([''])
    point = NUM_MAP['A']
    for ch in string:
        dist = NUM_MAP[ch] - point
        xStr = ('<' if dist.imag < 0 else '>') * abs(int(dist.imag))
        yStr = ('^' if dist.real < 0 else 'v') * abs(int(dist.real))
        skipXFirstMovement, skipYFirstMovement = False, False
        if point + (int(dist.imag) * 1j) == NUM_MAP['E']:
            skipXFirstMovement = True
        if point + int(dist.real) == NUM_MAP['E']:
            skipYFirstMovement = True
        nextInputs = set()
        if not skipXFirstMovement:
            for input in currentInputs:
                nextInputs.add(f'{input}{xStr}{yStr}A')
        if not skipYFirstMovement:
            for input in currentInputs:
                nextInputs.add(f'{input}{yStr}{xStr}A')
        currentInputs = nextInputs
        point = NUM_MAP[ch]
    return trimInputsByLen(currentInputs)[0]

def getInputsForDirections(inputs):
    minLen = sys.maxsize
    finalInputs = set()
    for input in inputs:
        currentInputs = set([''])
        point = DIREC_MAP['A']
        for ch in input:
            dist = DIREC_MAP[ch] - point
            xStr = ('<' if dist.imag < 0 else '>') * abs(int(dist.imag))
            yStr = ('^' if dist.real < 0 else 'v') * abs(int(dist.real))
            skipXFirstMovement, skipYFirstMovement = False, False
            if point + (int(dist.imag) * 1j) == DIREC_MAP['E']:
                skipXFirstMovement = True
            if point + int(dist.real) == DIREC_MAP['E']:
                skipYFirstMovement = True
            nextInputs = set()
            if not skipXFirstMovement:
                for nextInput in currentInputs:
                    nextInputs.add(f'{nextInput}{xStr}{yStr}A')
            if not skipYFirstMovement:
                for nextInput in currentInputs:
                    nextInputs.add(f'{nextInput}{yStr}{xStr}A')
            currentInputs = nextInputs
            point = DIREC_MAP[ch]
        currentInputs, minLenNew = trimInputsByLen(currentInputs)
        if minLenNew < minLen:
            minLen = minLenNew
            finalInputs = currentInputs
        elif minLenNew == minLen:
            finalInputs.update(currentInputs)
    finalInputs, minLen = trimInputsByLen(finalInputs)
    return finalInputs, minLen

sum = 0
for string in input.splitlines():
    direcInputs = getInputsForNumbers(string)
    minLen = sys.maxsize
    for i in range(25):
        print(f'{i+1}')
        direcInputs, minLen = getInputsForDirections(direcInputs)
    complexity = minLen * int(string[:-1])
    sum += complexity
    print(f'{string}: {minLen} * {int(string[:-1])} = {complexity}')

print(sum)
