# Advent of code Year 2024 Day 23 solution
# Author = Drew Blocki
# Date = December 2024

from itertools import combinations

with open((__file__.rstrip("main.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

part = 2

linkMap = {}
t = set()
largestNetwork = 0

def addLink(first, second):
    global linkMap, largestNetwork
    if first in linkMap:
        linkMap[first].add(second)
        if len(linkMap[first]) > largestNetwork:
            largestNetwork = len(linkMap[first])
    else:
        linkMap[first] = set([second])

for line in input.splitlines():
    first, second = line.split('-')
    if first[0] == 't':
        t.add(first)
    if second[0] == 't':
        t.add(second)
    addLink(first, second)
    addLink(second, first)

# Part 1
if part == 1:
    linkTrios = set()

    def addLinkTrio(trio):
        global linkTrios
        trio.sort()
        tuple = (trio[0], trio[1], trio[2])
        if tuple not in linkTrios:
            linkTrios.add(tuple)

    for key in t:
        links = linkMap[key]
        for link in links:
            for link2 in links:
                if link == link2:
                    continue
                if link2 in linkMap[link]:
                    addLinkTrio([key, link, link2])
                    
    print(f'T SETS: {len(linkTrios)}')

network = []
for i in range(largestNetwork, 1, -1):
    for key, items in linkMap.items():
        if len(items) < i:
            continue
        for combo in combinations(items, i):
            valid = True
            for pair in combinations(combo, 2):
                if pair[1] not in linkMap[pair[0]]:
                    valid = False
                    break
            if valid:
                network.append(key)
                for item in combo:
                    network.append(item)
                break
        if len(network) > 0:
            break
    if len(network) > 0:
        break
    
network.sort()

print(f'NETWORK: {','.join(network)}')    
