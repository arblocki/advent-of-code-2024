# Advent of code Year 2024 Day 17 solution
# Author = Drew Blocki
# Date = December 2024

import math
import re

with open((__file__.rstrip("main.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

pattern = r"Register A: (\d+)\s*Register B: (\d+)\s*Register C: (\d+)\s*Program: ([\d,]+)"

match = re.search(pattern, input)

aInit = int(match.group(1))
bInit = int(match.group(2))
cInit = int(match.group(3))
program = list(map(int, match.group(4).split(',')))

def comboOp(a, b, c, op):
    if op == 4:
        return a
    elif op == 5:
        return b
    elif op == 6:
        return c
    return op

def simulateProgram(a, b, c, program):
    out = []
    index = 0
    while index < len(program):
        proceed = True
        instr = program[index]
        if index + 1 == len(program):
            print(f'\tRUNNING INSTR AT FINAL INSTRUCTION WITH NO OPERAND')
            break
        operand = program[index + 1]
        if instr == 0:
            a = int(a // math.exp2(comboOp(a, b, c, operand)))
        elif instr == 1:
            b = int(b ^ operand)
        elif instr == 2:
            b = int(comboOp(a, b, c, operand) % 8)
        elif instr == 3:
            if a != 0:
                index = operand
                proceed = False
        elif instr == 4:
            b = int(b ^ c)
        elif instr == 5:
            out.append(int(comboOp(a, b, c, operand) % 8))
        elif instr == 6:
            b = int(a // math.exp2(comboOp(a, b, c, operand)))
        elif instr == 7:
            c = int(a // math.exp2(comboOp(a, b, c, operand)))
        if proceed:
            index += 2
    return out

# a = aInit
b = bInit
c = cInit

aFinal = 0
out = []
def solve(index, currentA):
    if index < 0:
        print(f'A: {currentA}')
        return True
    for a in range(8):
        aTest = (currentA << 3) | a
        out = simulateProgram(aTest, b, c, program)
        if out == program[index:] and solve(index - 1, aTest):
            return True
    return False
            

solve(len(program) - 1, 0)
