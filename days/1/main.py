# Advent of code Year 2024 Day 1 solution
# Author = Drew Blocki
# Date = December 2024

with open((__file__.rstrip("main.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

def extractTwoNumbers(line):
    num1, num2 = map(int, line.split()[:2])
    return num1, num2

list1 = []
list2 = []
lines = input.splitlines()
for line in lines:
    num1, num2 = extractTwoNumbers(line)
    list1.append(num1)
    list2.append(num2)

# Part 1
print('PART 1')
sortedList1 = list1.copy()
sortedList2 = list2.copy()
sortedList1.sort()
sortedList2.sort()

# lengths should be the same
assert len(list1) == len(list2)

size = len(list1)
distance = 0
for i in range(size):
    distance += abs(list1[i] - list2[i])
    
print(f'\tTOTAL DISTANCE: {distance}\n')

# Part 2
print('PART 2')
countDict = {}
for i in range(size):
    num = list2[i]
    if countDict.get(num) is None:
        countDict[num] = 1
    else:
        countDict[num] += 1

similarityScore = 0
for i in range(size):
    num = list1[i]
    count = countDict.get(num, 0)
    similarityScore += num * count
    
print(f'\tSIMILARITY SCORE: {similarityScore}')
