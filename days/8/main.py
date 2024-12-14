# Advent of code Year 2024 Day 8 solution
# Author = Drew Blocki
# Date = December 2024

with open((__file__.rstrip("main.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

# Return set of antenna characters, and map from character to list of coords
def processInput(input):
    antennaCharSet = set()
    antennaMap = {}
    for rowIndex, line in enumerate(input.splitlines()):
        for colIndex, char in enumerate(line):
            if char == '.':
                continue
            if char in antennaCharSet:
                antennaMap[char].append((rowIndex, colIndex))
            else:
                antennaCharSet.add(char)
                antennaMap[char] = [(rowIndex, colIndex)]
    return antennaCharSet, antennaMap

def onMap(candidate, rows, cols):
    if candidate[0] >= 0 and candidate[0] < rows and candidate[1] >= 0 and candidate[1] < cols:
        return True
    else:
        return False

# PART 1
print('PART 1')
rows = len(input.splitlines())
cols = len(input.splitlines()[0])
antennaCharSet, antennaMap = processInput(input)

# Part 1
antinodeLocSet = set()
count = 0

# Part 2
antinodeLocSetWithResonance = set()
countWithResonance = 0

for char in antennaCharSet:
    locList = antennaMap[char]
    if len(locList) < 2:
        continue
    for index in range(len(locList) - 1):
        firstLoc = locList[index]
        for secondLoc in locList[index+1:]:
            if firstLoc not in antinodeLocSetWithResonance:
                antinodeLocSetWithResonance.add(firstLoc)
                countWithResonance += 1
            if secondLoc not in antinodeLocSetWithResonance:
                antinodeLocSetWithResonance.add(secondLoc)
                countWithResonance += 1 
            
            rowDiff = secondLoc[0] - firstLoc[0]
            colDiff = secondLoc[1] - firstLoc[1]
            
            firstAntinodeCandidate = (firstLoc[0] - rowDiff, firstLoc[1] - colDiff)
            if onMap(firstAntinodeCandidate, rows, cols) and firstAntinodeCandidate not in antinodeLocSet:
                antinodeLocSet.add(firstAntinodeCandidate)
                count += 1

            resonantCandidate = firstAntinodeCandidate
            while onMap(resonantCandidate, rows, cols):
                if resonantCandidate not in antinodeLocSetWithResonance:
                    antinodeLocSetWithResonance.add(resonantCandidate)
                    countWithResonance += 1
                resonantCandidate = (resonantCandidate[0] - rowDiff, resonantCandidate[1] - colDiff)
                
            secondAntinodeCandidate = (secondLoc[0] + rowDiff, secondLoc[1] + colDiff)
            if onMap(secondAntinodeCandidate, rows, cols) and secondAntinodeCandidate not in antinodeLocSet:
                antinodeLocSet.add(secondAntinodeCandidate)
                count += 1
                
            resonantCandidate = secondAntinodeCandidate
            while onMap(resonantCandidate, rows, cols):
                if resonantCandidate not in antinodeLocSetWithResonance:
                    antinodeLocSetWithResonance.add(resonantCandidate)
                    countWithResonance += 1
                resonantCandidate = (resonantCandidate[0] + rowDiff, resonantCandidate[1] + colDiff)

print(f'COUNT: {count}')
print()

# PART 2
print('PART 2')
print(f'COUNT WITH RESONANCE: {countWithResonance}')
