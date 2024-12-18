# Advent of code Year 2024 Day 13 solution
# Author = Drew Blocki
# Date = December 2024

with open((__file__.rstrip("main.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

def getMinTokens(round):
    lines = round.split("\n")
    
    buttonA = lines[0].split(":")[1].strip()
    buttonA_X = int(buttonA.split(", ")[0][2:])
    buttonA_Y = int(buttonA.split(", ")[1][2:])

    buttonB = lines[1].split(":")[1].strip()
    buttonB_X = int(buttonB.split(", ")[0][2:])
    buttonB_Y = int(buttonB.split(", ")[1][2:])

    prize = lines[2].split(":")[1].strip()
    prize_X = int(prize.split(", ")[0][2:]) + 10 ** 13
    prize_Y = int(prize.split(", ")[1][2:]) + 10 ** 13
    
    d = buttonA_X * buttonB_Y - buttonA_Y * buttonB_X
    dx = prize_X * buttonB_Y - prize_Y * buttonB_X
    dy = buttonA_X * prize_Y - buttonA_Y * prize_X
    
    if dx % d == 0 and dy % d == 0:
        return (dx // d) * 3 + (dy // d)
    return 0

# same code for both parts
print('PART 2')
rounds = input.strip().split("\n\n")
totalTokens = 0
for index, round in enumerate(rounds):
    print(f'PROCESSING ROUND {index+1} OF {len(rounds)}')
    minTokens = getMinTokens(round)
    totalTokens += minTokens
print(f'TOKENS: {totalTokens}')
