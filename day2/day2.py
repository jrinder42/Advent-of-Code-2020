
'''

Advent of Code 2020 - Day 2

'''

# Part 1

correct = []
with open('day2.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        rule, s = line.split(':')
        s = s.strip()
        freq, value = rule.split(' ')
        lower, upper = freq.split('-') # lower and upper frequency bound
        lower = int(lower)
        upper = int(upper)
        c = s.count(value)
        if (lower <= c and c <= upper):
            correct.append(line)

print('Advent of Code Day 2 Answer Part 1:', len(correct))

# Part 2

valid = []
with open('day2.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        rule, s = line.split(':')
        s = s.strip() # should not do s.strip() as it is not inplace
        freq, value = rule.split(' ')
        lower, upper = freq.split('-') # lower and upper frequency bound
        lower = int(lower)
        upper = int(upper)

        lower_condition = s[lower - 1] == value
        upper_condition = s[upper - 1] == value
        if (lower_condition and not upper_condition) or (not lower_condition and upper_condition):
            valid.append(line)

print('Advent of Code Day 2 Answer Part 2:', len(valid)) # 426 is too low, # 441 is wrong
