# Advent of code Year 2024 Day 9 solution
# Author = Drew Blocki
# Date = December 2024

with open((__file__.rstrip("main.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

def readInputAsDisk(input):
    disk = []
    emptyDiskBlocks = []
    fileId = 0
    for index, blockStr in enumerate(input):
        blockNum = int(blockStr)
        if index % 2 == 0:
            for i in range(blockNum):
                disk.append(str(fileId))
            fileId += 1
        else:
            emptyDiskBlocks.append((len(disk), blockNum))
            for i in range(blockNum):
                disk.append('.')
    return disk, emptyDiskBlocks

def swapOpenBlocks(disk):
    searchPointer = 0
    for index in range(len(disk) - 1, 0, -1):
        if disk[index] != '.':
            for searchIndex in range(searchPointer, index):
                if disk[searchIndex] == '.':
                    disk[searchIndex], disk[index] = disk[index], disk[searchIndex]
                    searchPointer = searchIndex + 1
                    break
    return disk

def calculateChecksum(disk):
    checksum = 0
    for index, fileIdStr in enumerate(disk):
        if fileIdStr != '.':
            checksum += (index * int(fileIdStr))
    return checksum

# PART 1
print('PART 1')

disk, emptyDiskBlocks = readInputAsDisk(input)
disk = swapOpenBlocks(disk)
checksum = calculateChecksum(disk)
print(f'CHECKSUM: {checksum}\n')


def swapRange(disk, periodStartIndex, fileEndIndex, size):
    for i in range(size):
        periodIndex = periodStartIndex + i
        fileBlockIndex = fileEndIndex - i
        disk[periodIndex], disk[fileBlockIndex] = disk[fileBlockIndex], disk[periodIndex]
    return disk

def swapOpenFilespace(disk, emptyDiskBlocks):
    index = len(disk) - 1
    while index >= 0:
        if disk[index] != '.':
            fileId = disk[index]
            fileSearchIndex = index - 1
            while fileSearchIndex >= 0 and disk[fileSearchIndex] == fileId:
                fileSearchIndex -= 1
            fileLength = index - fileSearchIndex
            for blockIndex, emptyBlock in enumerate(emptyDiskBlocks):
                emptyBlockStartIndex = emptyBlock[0]
                emptyBlockSize = emptyBlock[1]
                if emptyBlockStartIndex > index:
                    break
                if emptyBlockSize >= fileLength:
                    swapped = True
                    disk = swapRange(disk, emptyBlockStartIndex, index, fileLength)
                    if fileLength == emptyBlockSize:
                        del emptyDiskBlocks[blockIndex]
                    else:
                        emptyDiskBlocks[blockIndex] = (emptyBlockStartIndex + fileLength, emptyBlockSize - fileLength)
                    break
            index -= fileLength
        else:
            index -= 1
    return disk

# PART 2
print('PART 2')

disk, emptyDiskBlocks = readInputAsDisk(input)
disk = swapOpenFilespace(disk, emptyDiskBlocks)
checksum = calculateChecksum(disk)
print(f'CHECKSUM: {checksum}\n')
