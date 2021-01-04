
'''

Advent of Code 2020 - Day 8

'''

from copy import deepcopy

instructions = []
with open('day8.txt', 'r') as file:
    for line in file:
        instruction = line.strip().split(' ')
        sign = 0
        if instruction[1][0] == '+':
            sign = 1
        else:
            sign = -1
        instructions.append({instruction[0]: sign * int(instruction[1][1:])})

# Part 1

visited = []
accumulator = 0
count = 0
duplicate = False
while not duplicate or count == len(instructions) - 1:
    instruction = instructions[count]
    if list(instruction.keys())[0] == 'acc':
        visited.append(count)
        count += 1
        accumulator += sum(instruction.values())
    elif list(instruction.keys())[0] == 'nop':
        visited.append(count)
        count += 1
        continue
    elif list(instruction.keys())[0] == 'jmp':
        visited.append(count)
        count += list(instruction.values())[0]
        if count in visited:
            duplicate = True

print('Advent of Code Day 8 Answer Part 1:', accumulator)

# Part 2

visited = []
accumulator = 0
count = 0
duplicate = False
nops = []
jmps = []
for i in range(len(instructions)):
    if list(instructions[i].keys())[0] == 'nop':
        nops.append(i)
    elif list(instructions[i].keys())[0] == 'jmp':
        jmps.append(i)
fix_instruction = {'nop': nops, 'jmp': jmps}

for k, v in fix_instruction.items():
    for potential_fix in v: # indexes of
        new_instructions = deepcopy(instructions)
        key, value = list(new_instructions[potential_fix].items())[0]
        if k == 'nop':
            new_instructions[potential_fix] = {'jmp': value}
        else: # 'jmp'
            new_instructions[potential_fix] = {'nop': value}
        visited = []
        accumulator = 0
        count = 0
        duplicate = False
        while not duplicate:
            if count > len(new_instructions) - 1:
                break

            instruction = new_instructions[count]
            if list(instruction.keys())[0] == 'acc':
                visited.append(count)
                count += 1
                accumulator += sum(instruction.values())
            elif list(instruction.keys())[0] == 'nop':
                visited.append(count)
                count += 1
                continue
            elif list(instruction.keys())[0] == 'jmp':
                visited.append(count)
                count += list(instruction.values())[0]
                if count in visited:
                    duplicate = True

        if duplicate == False:
            print('Advent of Code Day 8 Answer Part 2:', accumulator)
            break
