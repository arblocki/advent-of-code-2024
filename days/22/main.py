# Advent of code Year 2024 Day 22 solution
# Author = Drew Blocki
# Date = December 2024

# import sys

# if len(sys.argv) < 2:
#     print("Usage: python main.py <input_file>")
#     sys.exit(1)

filename = 'input.txt' # sys.argv[1]

with open((__file__.rstrip("main.py")+filename), 'r') as input_file:
    input = input_file.read()

def calculateSecretNum(num):
    secret = (num ^ (num << 6)) % 16777216
    secret = (secret ^ (secret >> 5)) % 16777216
    secret = (secret ^ (secret << 11)) % 16777216
    return secret

# sum = 0
maxBananas = 0
sequenceBananaCount = {}
for next in input.splitlines():
    num = int(next)
    secret = num
    tail = secret % 10
    sequence = []
    usedSequences = set()
    for i in range(2000):
        secret = calculateSecretNum(secret)
        newTail = secret % 10
        diff = newTail - tail
        sequence.append(diff)
        if len(sequence) > 4:
            sequence.pop(0)
        sequenceStr = ','.join(map(str, sequence))
        if len(sequence) == 4 and sequenceStr not in usedSequences:
            usedSequences.add(sequenceStr)
            if sequenceStr in sequenceBananaCount:     
                sequenceBananaCount[sequenceStr] += newTail
            else:
                sequenceBananaCount[sequenceStr] = newTail
            if sequenceBananaCount[sequenceStr] > maxBananas:
                maxBananas = sequenceBananaCount[sequenceStr]
        tail = newTail
    # sum += secret
    print(f'\t{num}\t\t: {secret}')
print(f'MAX BANANAS: {maxBananas}')   
