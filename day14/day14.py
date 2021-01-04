
'''

Advent of Code 2020 - Day 14

'''

from itertools import product

# Part 1

memory = {}
with open('day14.txt', 'r') as file:
    mask = ''
    for line in file:
        if line.strip()[:3] == 'mem': # guaranteed to have a mask
            num = int(line.strip().split('=')[1].strip())
            space = int(line[line.index('[') + 1:line.index(']')])
            b = bin(num).split('b')[1]
            b = '0' * (36 - len(b)) + b
            b = [char for char in b]
            for i, char in enumerate(b):
                if mask[i] == '1':
                    b[i] = '1'
                elif mask[i] == '0':
                    b[i] = '0'
            b = ''.join(b)
            memory[space] = int(b, 2)
        elif line.strip()[:4] == 'mask': # 36 characters long
            mask = line.strip().split('=')[1].strip()

memory_values = 0
for key, value in memory.items():
    memory_values += value

print('Advent of Code Day 14 Answer Part 1:', memory_values)

# Part 2 - different rules

memory = {}
with open('day14.txt', 'r') as file:
    mask = ''
    for line in file:
        if line.strip()[:3] == 'mem': # guaranteed to have a mask
            num = int(line.strip().split('=')[1].strip())
            space = int(line[line.index('[') + 1:line.index(']')])
            b = bin(space).split('b')[1]
            b = '0' * (36 - len(b)) + b
            b = [char for char in b]
            addresses = product([0, 1], repeat=mask.count('X'))
            for i, char in enumerate(b):
                if mask[i] == '1':
                    b[i] = '1'
                elif mask[i] == '0':
                    continue
                elif mask[i] == 'X': # floating
                    b[i] = 'X'
            b = ''.join(b)
            for address in addresses:
                address = list(address)
                floating_b = [char for char in b]
                for i, char in enumerate(floating_b):
                    if char == 'X':
                        floating_b[i] = str(address.pop())
                memory[int(''.join(floating_b), 2)] = num
        elif line.strip()[:4] == 'mask': # 36 characters long
            mask = line.strip().split('=')[1].strip()

memory_values = 0
for key, value in memory.items():
    memory_values += value

print('Advent of Code Day 14 Answer Part 2:', memory_values)