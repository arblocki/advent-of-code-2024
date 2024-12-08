# Advent of code Year 2024 Day 2 solution
# Author = Drew Blocki
# Date = December 2024

with open((__file__.rstrip("main.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

# SOLUTIONS
# Part 1
# Small: 2
# Full: 252

# Part 2
# Small: 4 -- 8 w/ custom cases
# Full: 324


# PART 1
def areLevelsSafe(level1, level2, increasing):
    diff = level2 - level1
    if increasing and (diff < 1 or diff > 3):
        return False
    elif not increasing and (diff < -3 or diff > -1):
        return False  
    return True

# Report is safe if it increases or decreases the whole way by 1-3 each step
def isReportSafe(report):
    increasing = report[1] - report[0] > 0
    for i in range(len(report) - 1):
        if not areLevelsSafe(report[i], report[i + 1], increasing):
            return i
    return -1

def isTrimmedReportSafe(report, index):
    if index < 0 or index >= len(report):
        return False
    newReport = report.copy()
    del newReport[index]
    return isReportSafe(newReport)

print('PART 1')
lines = input.splitlines()
safeReportCount = 0
for line in lines:
    reportNums = [int(num) for num in line.split()]
    if isReportSafe(reportNums) == -1:
        safeReportCount += 1

print(f'    SAFE REPORTS: {safeReportCount}\n')


# PART 2
print('PART 2')
lines = input.splitlines()
safeReportCount = 0
for line in lines:
    reportNums = [int(num) for num in line.split()]
    unsafeIndex = isReportSafe(reportNums)
    if unsafeIndex == -1:
        safeReportCount += 1
    else: 
        if isTrimmedReportSafe(reportNums, unsafeIndex) == -1:
            safeReportCount += 1
        elif isTrimmedReportSafe(reportNums, unsafeIndex+1) == -1:
            safeReportCount += 1
        elif isTrimmedReportSafe(reportNums, unsafeIndex-1) == -1:
            safeReportCount += 1

print(f'    SAFE REPORTS: {safeReportCount}\n')

