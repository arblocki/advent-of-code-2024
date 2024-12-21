# Advent of code Year 2024 Day 19 solution
# Author = Drew Blocki
# Date = December 2024

with open((__file__.rstrip("main.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

towels = set()
towelPermutations = {}

maxLen = 0

for towel in input.splitlines()[0].split(', '):
    towels.add(towel)
    if len(towel) > maxLen:
        maxLen = len(towel)

def checkNumPossible(string):
    global towels
    sum = 0
    if string in towelPermutations:
        return towelPermutations[string]
    for searchLen in range(1, maxLen + 1):
        if searchLen > len(string):
            break
        substr = string[:searchLen]
        if substr in towels:
            if substr == string:
                sum += 1
            else:
                sum += checkNumPossible(string[searchLen:])
    towelPermutations[string] = sum
    return sum

sumPossible = 0
for index, string in enumerate(input.splitlines()[2:]):
    num = checkNumPossible(string)
    print(f'{string} ({index+1}): {num}')
    sumPossible += num

print(f'SUM POSSIBLE: {sumPossible}')
