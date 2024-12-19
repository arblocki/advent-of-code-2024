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

def comboOp(op):
    global a, b, c
    if op == 4:
        return a
    elif op == 5:
        return b
    elif op == 6:
        return c
    return op

# a = aInit
aNext = 1
b = bInit
c = cInit

out = []
while out != program:
    a = aNext
    if a % 100000 == 0:
        print(a)
    # test = (((a % 8) ^ 5) ^ 6) ^ int(a / (int(math.exp2(a % 8)) ^ 5))
    # if test % 8 != 2:
    #     aNext += 1
    #     continue
    b = bInit
    c = cInit

    out = []
    instrList = []
    index = 0
    while index < len(program):
        proceed = True
        instr = program[index]
        if index + 1 == len(program):
            print(f'\tRUNNING INSTR AT FINAL INSTRUCTION WITH NO OPERAND')
            break
        operand = program[index + 1]
        if instr == 0:
            a = int(a // math.exp2(comboOp(operand)))
            instrList.append(f'\tSETTING A TO A / 2^{comboOp(operand)} (comboOp of {operand}) : {a}')
        elif instr == 1:
            b = int(b ^ operand)
            instrList.append(f'\tSETTING B TO B XOR {operand} : {b}')
        elif instr == 2:
            b = int(comboOp(operand) % 8)
            instrList.append(f'\tSETTING B TO {comboOp(operand)} (comboOp of {operand}) mod 8 : {b}')
        elif instr == 3:
            if a != 0:
                index = operand
                instrList.append(f'\tJUMPING TO {operand}')
                proceed = False
        elif instr == 4:
            b = int(b ^ c)
            instrList.append(f'\tSETTING B TO B XOR C : {b}')
        elif instr == 5:
            last = len(out)
            out.append(int(comboOp(operand) % 8))
            instrList.append(f'\tOUTPUTTING {comboOp(operand)} (comboOp of {operand}) mod 8 : {int(comboOp(operand) % 8)}')
            # if out[last] != program[last]:
            #     break
        elif instr == 6:
            b = int(a // math.exp2(comboOp(operand)))
            instrList.append(f'\tSETTING B TO A / 2^{comboOp(operand)} (comboOp of {operand}) : {b}')
        elif instr == 7:
            c = int(a // math.exp2(comboOp(operand)))
            instrList.append(f'\tSETTING C TO A / 2^{comboOp(operand)} (comboOp of {operand}) : {c}')
        if proceed:
            index += 2
    aNext <<= 3

print(','.join(map(str, out)))
# for instr in instrList:
#     print(instr)
print(f'a: {aNext-1}')
