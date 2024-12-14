# Advent of code Year 2024 Day 7 solution
# Author = Drew Blocki
# Date = December 2024

with open((__file__.rstrip("main.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

# Returns true if pair of numbers in list can add or multiply to the number
# If the list has more than 2 elements, recurse on the rest of the list twice (assuming addition and multiplication)
def canFormValue(value, list):
    if len(list) < 2:
        raise RuntimeError(f'RECURSED TOO FAR TO ({value}, {list})')
    if len(list) == 2:
        first = list[0]
        second = list[1]
        if first + second == value or first * second == value:
            return True
        else:
            return False
    else:
        last = list[-1]
        addRes = canFormValue(value - last, list[:-1])
        multRes = False
        if value % last == 0:
            multRes = canFormValue(int(value / last), list[:-1])
        return addRes or multRes

def compatibleConcatRecurse(value, tail):
    valStr = str(value)
    tailStr = str(tail)
    for index in range(len(tailStr)):
        if valStr[-(index+1)] != tailStr[-(index+1)]:
            return False
    return True

def canFormValueWithConcat(value, list):
    if len(list) < 2:
        raise RuntimeError(f'RECURSED TOO FAR TO ({value}, {list})')
    if len(list) == 2:
        first = list[0]
        second = list[1]
        firstStr = str(first)
        secondStr = str(second)
        if int(firstStr + secondStr) == value:
            return True
        elif first + second == value or first * second == value:
            return True
        else:
            return False
    else:
        last = list[-1]
        addRes = canFormValueWithConcat(value - last, list[:-1])
        multRes = False
        concatRes = False
        if value % last == 0:
            multRes = canFormValueWithConcat(int(value / last), list[:-1])
        if compatibleConcatRecurse(value, last) and value >= 0:
            tailLen = len(str(last))
            newValStr = str(value)[:-tailLen]
            if len(newValStr) > 0:
                concatRes = canFormValueWithConcat(int(str(value)[:-tailLen]), list[:-1])
        return addRes or multRes or concatRes

# PART 1
# print('PART 1')
sum = 0
sumWithConcat = 0
for line in input.splitlines():
    # print(f'TESTING {line}')
    parts = line.split(': ')
    testVal = int(parts[0])
    candidateNumStr = parts[1]
    candidateNums = [int(num) for num in candidateNumStr.split(' ')]
    # if canFormValue(testVal, candidateNums):
    #     sum += testVal
    if canFormValueWithConcat(testVal, candidateNums):
        # print(f'\tADDING {testVal}')
        sumWithConcat += testVal

# print(f'SUM: {sum}')

# PART 2
print('PART 2')
print(f'SUM W/ CONCAT: {sumWithConcat}')
