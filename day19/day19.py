
'''

Advent of Code 2020 - Day 19

'''

# context-free grammar

from itertools import product

rules = {}
messages = []
flip = False
with open('day19.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if line == '':
            flip = True
            continue
        if not flip:
            key, value = line.split(': ')
            rules[key] = value
        else:
            messages.append(line)

# Part 1 - contains no infinite loops

def matching(rule):
    # use sets because lookup is faster on sets than it is on lists, sets uses a hash table

    if '"' in rule:
        return set(rule[1])

    elif '|' in rule: # list of sub-rules
        return set(match for sub_rule in rule.split(' | ') for match in matching(sub_rule))

    elif ' ' in rule: # sub-rule
        left, right = rule.split(' ', maxsplit=1) # handle the rule length > 2
        return set(l + r for l, r in product(matching(left), matching(right)))

    return matching(rules[rule])

match = matching(rules['0'])

print('Advent of Code Day 19 Answer Part 1:', sum(1 for message in messages if message in match))

# Part 2 - contains infinite loops

'''
0: 8 11
rules['8'] = '42 | 42 8'
rules['11'] = '42 31 | 42 11 31'
'''

rule_back = matching(rules['31'])
rule_front = matching(rules['42'])

count_infinite = 0
for message in messages:
    count_back = 0
    count_front = 0
    flip = False
    for i in range(len(message), 7, -8):
        message_slice = message[i - 8:i]
        if message_slice in rule_back and not flip:
            count_back += 1
        elif message_slice in rule_front and flip:
            count_front += 1
        elif message_slice not in rule_back and message_slice in rule_front:
            flip = True
            count_front += 1

    if (count_back + count_front) * 8 == len(message) and count_back > 0 and count_front > count_back:
        count_infinite += 1

print('Advent of Code Day 19 Answer Part 2:', count_infinite)
