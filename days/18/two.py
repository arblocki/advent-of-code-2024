# Advent of code Year 2024 Day 18 solution part 2
# Author = Drew Blocki
# Date = December 2024

suffix = ''

with open((__file__.rstrip("two.py")+f'input{suffix}.txt'), 'r') as input_file:
    input = input_file.read()

SIZE = 70 if suffix == '' else 6
NUM_BYTES = 1024 if suffix == '' else 12

NUM_TOTAL_BYTES = len(input.splitlines())

def corruptBytes(num):
    corrupted = set()
    for line in input.splitlines()[:num]:
        coordinates = line.split(',')
        x, y = int(coordinates[0]), int(coordinates[1])
        corrupted.add(x + y * 1j)
    return corrupted

def expandSearch(curr, corrupted, visited, searchList):
    global SIZE
    if curr == SIZE + SIZE * 1j:
        return True
    if curr in visited:
        return
    visited.add(curr)
    d = 1
    for _ in range(4):
        next = curr + d
        if not (next.real < 0 or next.real > SIZE or next.imag < 0 or next.imag > SIZE) \
        and next not in visited and next not in corrupted:
            searchList.append(next)
        d *= -1j

def searchForPath(corrupted, visited):
    searchList = [0]
    while len(searchList) != 0:
        next = searchList.pop(0)
        pathFound = expandSearch(next, corrupted, visited, searchList)
        if pathFound:
            return True
    return False
    

front = 0
back = NUM_TOTAL_BYTES
index = NUM_TOTAL_BYTES // 2
firstPathExists = searchForPath(corruptBytes(index+1), set())
secondPathExists = searchForPath(corruptBytes(index+2), set())
while firstPathExists == secondPathExists:
    if firstPathExists:
        front = index
        index += (back - index) // 2
    else:
        back = index
        index = (index - front) // 2
        
    firstPathExists = searchForPath(corruptBytes(index+1), set())
    secondPathExists = searchForPath(corruptBytes(index+2), set()) 
    
print(f'FIRST BYTE TO BLOCK PATH: {input.splitlines()[index+1]}')
    
