# Advent of code Year 2024 Day 5 solution
# Author = Drew Blocki
# Date = December 2024

with open((__file__.rstrip("main.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

# PART 1
print('PART 1')
# Build map from second number to list of numbers that must come first
precedingNumMap = {}
updates = []
updateMode = False
for line in input.splitlines():
    if updateMode:
        updatePageNums = [int(numStr) for numStr in line.split(',')]
        updates.append(updatePageNums)
    elif line.find('|') == -1:
        updateMode = True
    else:
        pageRules = [int(numStr) for numStr in line.split('|')]
        firstNum = pageRules[1]
        secondNum = pageRules[0]
        if precedingNumMap.get(pageRules[1]) is None:
            precedingNumMap[firstNum] = [secondNum]
        else:
            precedingNumMap[firstNum].append(secondNum)

def isUpdateValid(update, precedingNumMap):
    #   Build set of every number in the list: remainingSet
    remainingSet = set(update)
    valid = True
    #   Traverse the list:
    for num in update:
        # For the current number: 
        #   check if any of the numbers that need to come first are in remainingSet
        for precedingNum in precedingNumMap.get(num, []):
            if precedingNum in remainingSet:
                valid = False
                break
        if not valid:
            break
        # Remove the current num from the remainingSet
        remainingSet.remove(num)
    return valid

sum = 0
invalidUpdates = []
# For each list,
for update in updates:
    valid = isUpdateValid(update, precedingNumMap)
    if valid:
        middleIndex = int((len(update) - 1) / 2)
        sum += update[middleIndex]
    else:
        invalidUpdates.append(update)

print(f'SUM: {sum}\n')

# PART 2
print('PART 2')
part2Sum = 0
for update in invalidUpdates:
    # print(f'FIXING {update}')
    valid = isUpdateValid(update, precedingNumMap)
    while not valid:
        remainingSet = set(update)
        for index, num in enumerate(update):
            updateMade = False
            for precedingNum in precedingNumMap.get(num, []):
                if precedingNum in remainingSet:
                    # print(f'FOUND {precedingNum} AFTER {num}; MOVING {precedingNum} TO {index}')
                    update.remove(precedingNum)
                    update.insert(index, precedingNum)
                    # print(f'NEW UPDATE: {update}')
                    updateMade = True
                    break
            if updateMade:
                valid = isUpdateValid(update, precedingNumMap)
                break
            else: 
                remainingSet.remove(num)
    middleIndex = int((len(update) - 1) / 2)
    part2Sum += update[middleIndex]
    
print(f'SUM: {part2Sum}\n')
