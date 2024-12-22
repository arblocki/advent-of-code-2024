# # Advent of code Year 2024 Day 21 solution
# # Author = Drew Blocki
# # Date = December 2024

# import sys
# import random

# with open((__file__.rstrip("main.py")+"input.txt"), 'r') as input_file:
#     input = input_file.read()

# NUM_MAP = {
#     '7': 0,
#     '8': 1j,
#     '9': 2j,
#     '4': 1,
#     '5': 1 + 1j,
#     '6': 1 + 2j,
#     '1': 2,
#     '2': 2 + 1j,
#     '3': 2 + 2j,
#     '0': 3 + 1j,
#     'A': 3 + 2j, 
#     'E': 3,
# }

# DIREC_MAP = {
#     '^': 1j,
#     'A': 2j,
#     '<': 1,
#     'v': 1 + 1j,
#     '>': 1 + 2j,
#     'E': 0,
# }

# def trimInputsByLen(inputs):
#     finalInputs = set()
#     minLen = sys.maxsize
#     for input in inputs:
#         minLen = min(minLen, len(input))
#     for input in inputs:
#         if len(input) > minLen:
#             continue
#         finalInputs.add(input)
#     return finalInputs, minLen

# def getInputsForNumbers(string):
#     currentInputs = set([''])
#     point = NUM_MAP['A']
#     for ch in string:
#         dist = NUM_MAP[ch] - point
#         xStr = ('<' if dist.imag < 0 else '>') * abs(int(dist.imag))
#         yStr = ('^' if dist.real < 0 else 'v') * abs(int(dist.real))
#         skipXFirstMovement, skipYFirstMovement = False, False
#         if point + (int(dist.imag) * 1j) == NUM_MAP['E']:
#             skipXFirstMovement = True
#         if point + int(dist.real) == NUM_MAP['E']:
#             skipYFirstMovement = True
#         nextInputs = set()
#         if not skipXFirstMovement:
#             for input in currentInputs:
#                 nextInputs.add(f'{input}{xStr}{yStr}A')
#         if not skipYFirstMovement:
#             for input in currentInputs:
#                 nextInputs.add(f'{input}{yStr}{xStr}A')
#         currentInputs = nextInputs
#         point = NUM_MAP[ch]
#     return trimInputsByLen(currentInputs)[0]

# segmentInputMap = {}

# def getInputsForDirections(inputs):
#     global segmentInputMap
    
#     minLen = sys.maxsize
#     finalInputs = set()
    
#     def getSegmentInputs(segment):
#         if not segment:
#             return set([''])
            
#         if segment in segmentInputMap:
#             return segmentInputMap[segment]
            
#         point = DIREC_MAP['A']
#         segmentInputs = set([''])
        
#         for ch in segment:
#             dist = DIREC_MAP[ch] - point
#             xStr = ('<' if dist.imag < 0 else '>') * abs(int(dist.imag))
#             yStr = ('^' if dist.real < 0 else 'v') * abs(int(dist.real))
            
#             skipXFirstMovement = point + (int(dist.imag) * 1j) == DIREC_MAP['E']
#             skipYFirstMovement = point + int(dist.real) == DIREC_MAP['E']
            
#             nextInputs = set()
#             if not skipXFirstMovement:
#                 for nextInput in segmentInputs:
#                     nextInputs.add(f'{nextInput}{xStr}{yStr}A')
#             if not skipYFirstMovement:
#                 for nextInput in segmentInputs:
#                     nextInputs.add(f'{nextInput}{yStr}{xStr}A')
                    
#             segmentInputs = nextInputs
#             point = DIREC_MAP[ch]
            
#         segmentInputMap[segment] = segmentInputs
#         return segmentInputs
    
#     for input in inputs:
#         currentInputs = set([''])
#         segments = [seg + 'A' for seg in input.split('A')[:-1]]
        
#         for segment in segments:
#             newCurrentInputs = set()
#             segment_results = getSegmentInputs(segment)
            
#             for current in currentInputs:
#                 for segment_result in segment_results:
#                     newCurrentInputs.add(f'{current}{segment_result}')
                    
#             currentInputs = newCurrentInputs
            
#         currentInputs, minLenNew = trimInputsByLen(currentInputs)
#         if minLenNew < minLen:
#             minLen = minLenNew
#             finalInputs = currentInputs
#         elif minLenNew == minLen:
#             finalInputs.update(currentInputs)
            
#     finalInputs, minLen = trimInputsByLen(finalInputs)
#     return finalInputs, minLen

# sum = 0
# for string in input.splitlines():
#     direcInputs = getInputsForNumbers(string)
#     minLen = sys.maxsize
#     for i in range(10):
#         print(f'{i+1}')
#         direcInputs, minLen = getInputsForDirections(direcInputs)
#     complexity = minLen * int(string[:-1])
#     sum += complexity
#     print(f'{string}: {minLen} * {int(string[:-1])} = {complexity}')

# print(sum)

# :(

import functools

with open((__file__.rstrip("main.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

n = [ "789", "456", "123", " 0A" ]
d = [ " ^A", "<v>" ]

def path( p, f, t ):
    fx, fy = next( ( x, y ) for y, r in enumerate( p ) for x, c in enumerate( r ) if c == f )
    tx, ty = next( ( x, y ) for y, r in enumerate( p ) for x, c in enumerate( r ) if c == t )
    def g( x, y, s ):
        if ( x, y ) == ( tx, ty ):             yield s + 'A'
        if tx < x and p[ y ][ x - 1 ] != ' ': yield from g( x - 1, y, s + '<' )
        if ty < y and p[ y - 1 ][ x ] != ' ': yield from g( x, y - 1, s + '^' )
        if ty > y and p[ y + 1 ][ x ] != ' ': yield from g( x, y + 1, s + 'v' )
        if tx > x and p[ y ][ x + 1 ] != ' ': yield from g( x + 1, y, s + '>' )
    return min( g( fx, fy, "" ),
                key = lambda p: sum( a != b for a, b in zip( p, p[ 1 : ] ) ) )

@functools.cache
def solve( s, l ):
    if l > 25: return len( s )
    return sum( solve( path( d if l else n, f, t ), l + 1 ) for f, t in zip( 'A' + s, s ) )

print( sum( solve( s.strip(), 0 ) * int( s[ : 3 ] ) for s in input.splitlines() ) )

