
'''

Advent of Code 2020 - Day 6

'''

# Part 1 - Union

groups = []
with open('day6.txt', 'r') as file:
    group = ''
    for line in file:
        line = line.strip('\n').split(' ')
        if len(line) == 1 and line[0] == '':
            groups.append(group)
            group = ''
            continue

        for line_item in line:
            group += line_item

    groups.append(group)

groups_size = [len(''.join(set(group))) for group in groups]

print('Advent of Code Day 6 Answer Part 1:', sum(groups_size))

# Part 2 - Intersection

groups = []
with open('day6.txt', 'r') as file:
    group = ''
    count = 0
    for line in file:
        line = line.strip('\n').split(' ')
        if len(line) == 1 and line[0] == '':
            chars = ''.join(set(group))
            question_count = 0
            for char in chars:
                if group.count(char) == count: # every individual in a group answered yes
                    question_count += 1
            groups.append(question_count)
            group = ''
            count = 0
            continue

        for line_item in line:
            group += line_item
            count += 1 # number of individuals in a group

    chars = ''.join(set(group))
    question_count = 0
    for char in chars:
        if group.count(char) == count:  # every individual in a group answered yes
            question_count += 1
    groups.append(question_count)

print('Advent of Code Day 6 Answer Part 2:', sum(groups))

