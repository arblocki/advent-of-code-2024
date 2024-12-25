# Advent of code Year 2024 Day 24 solution
# Author = Drew Blocki
# Date = December 2024

import functools
import math
import sys
from copy import copy, deepcopy
from itertools import combinations

with open((__file__.rstrip("main.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

rounds = input.strip().split("\n\n")
inits, gateStr = rounds[:2]

initVals = {}

for init in inits.splitlines():
    key, val = init.split(': ')
    initVals[key] = int(val)

initGates = []
initGatesMap = {}
for gate in gateStr.splitlines():
    first, op, second, _, dest = gate.strip().split(' ')[:5]
    initGates.append([first, op, second, dest])
    initGatesMap[dest] = [first, op, second]

def processGates(initGates):
    global initVals
    vals = copy(initVals)
    gatesRemaining = deepcopy(initGates)
    prevLen = sys.maxsize
    newLen = len(gatesRemaining)
    while len(gatesRemaining) > 0 and prevLen != newLen:
        prevLen = newLen
        for index, gate in enumerate(gatesRemaining):
            first, op, second, dest = gate[:4]
            if first not in vals or second not in vals:
                continue
            gatesRemaining.pop(index)
            match op:
                case 'AND':
                    vals[dest] = vals[first] & vals[second]
                case 'OR':
                    vals[dest] = vals[first] | vals[second]
                case 'XOR':
                    vals[dest] = vals[first] ^ vals[second]
        newLen = len(gatesRemaining)
        
    return vals

def getVal(vals, prefix):
    sum = 0
    for i in range(1000):
        key = f'{prefix}{str(i) if i >= 10 else '0' + str(i)}'
        if key not in vals:
            break
        sum += int(vals[key] * math.exp2(i))
    return sum

def getAndZVal(vals):
    sum = 0
    for i in range(1000):
        xKey = f'x{str(i) if i >= 10 else '0' + str(i)}'
        yKey = f'y{str(i) if i >= 10 else '0' + str(i)}'
        if xKey not in vals or yKey not in vals:
            break
        sum += int((vals[xKey] & vals[yKey]) * math.exp2(i))
    return sum

def swapGateOuts(gates, indices):
    first, second = indices[:2]
    temp = gates[first][3]
    gates[first][3] = gates[second][3]
    gates[second][3] = temp
    
def getGateOuts(gates, pair):
    return [gates[pair[0]][3], gates[pair[1]][3]]
    
wantedZVal = getVal(initVals, 'x') + getVal(initVals, 'y')

finalVals = processGates(initGates)
# z = getVal(finalVals, 'z') 

# print(f'SUM: {sum}')

# badBits = []
# for i in range(1000):
#     if math.exp2(i) > wantedZVal:
#         break
#     key = f'z{str(i) if i >= 10 else '0' + str(i)}'
#     if key not in finalVals:
#         break
#     bit = 1 if wantedZVal & math.exp2(i) > 0 else 0
#     if finalVals[key] != bit:
#         badBits.append(i)

tried = set()
def getTriedTuple(gates, pairs):
    indexList = []
    for pair in pairs:
        indexList.append(pair[0])
        indexList.append(pair[1])
    indexList.sort()
    triedList = [0] * (2 * len(indexList))
    for i, index in enumerate(indexList):
        triedList[2 * i] = index
        triedList[2 * i + 1] = gates[index][3]
    return tuple(triedList)

finalVals = {}
pairs = []
for pair1 in combinations(range(len(initGates)), 2):
    used = set(pair1[:])
    for pair2 in combinations(range(len(initGates)), 2):
        if pair2[0] in used or pair2[1] in used:
            continue
        used.update(pair2[:])
        for pair3 in combinations(range(len(initGates)), 2):
            if pair3[0] in used or pair3[1] in used:
                continue
            used.update(pair3[:])
            for pair4 in combinations(range(len(initGates)), 2):
                if pair4[0] in used or pair4[1] in used:
                    continue
                print(f'{pair1}, {pair2}, {pair3}, {pair4}')
                gates = deepcopy(initGates)
                swapGateOuts(gates, pair1)
                swapGateOuts(gates, pair2)
                swapGateOuts(gates, pair3)
                swapGateOuts(gates, pair4)
                nextTuple = getTriedTuple(gates, [pair1, pair2, pair3, pair4])
                if nextTuple in tried:
                    continue
                tried.add(nextTuple)
                finalVals = processGates(gates)
                if getVal(finalVals, 'z') == wantedZVal:
                    pairs.extend(getGateOuts(initGates, pair1))
                    pairs.extend(getGateOuts(initGates, pair2))
                    pairs.extend(getGateOuts(initGates, pair3))
                    pairs.extend(getGateOuts(initGates, pair4))
                    break
    if len(pairs) > 0:
        break

pairs.sort()
print(f'SWAP: {','.join(pairs)}')
