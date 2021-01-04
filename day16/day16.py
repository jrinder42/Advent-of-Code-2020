
'''

Advent of Code 2020 - Day 16

'''

from collections import defaultdict

# Part 1 - ignore my ticket

fields = []
my_ticket = []
nearby_tickets = []
with open('day16.txt', 'r') as file:
    rules = []
    rules_dict = {}
    valids = []
    invalids = []
    ticket = []
    errors = 0
    for line in file:
        if line == '\n' and not fields:
            fields.append(rules)
            continue
        elif line == '\n' and fields and not my_ticket:
            my_ticket = ticket
            continue
        elif line == '\n' and fields and my_ticket and not nearby_tickets:
            nearby_tickets = valids + invalids
            continue

        if line.strip() == 'your ticket:' or line.strip() == 'nearby tickets:':
            continue

        if not fields:
            line = line.strip()
            field, ranges = line.split(':')

            for r in ranges.split('or'):
                val = r.strip()
                lower, upper = val.split('-')
                lower, upper = int(lower), int(upper)
                if field not in rules_dict:
                    rules_dict[field] = list(range(lower, upper + 1)) # for Part 2
                else:
                    rules_dict[field] += list(range(lower, upper + 1)) # for Part 2
                rules += list(range(lower, upper + 1))
                rules = list(set(rules)) # get unique values
        elif fields and not my_ticket:
            ticket = line.strip().split(',')
            ticket = list(map(int, ticket))
        elif fields and my_ticket and not nearby_tickets:
            line = line.strip()
            values = line.split(',')
            values = list(map(int, values))
            bad = False
            for value in values:
                if value not in rules:
                    errors += value
                    bad = True
            if bad:
                invalids.append(values)
            else: # value is in rules
                valids.append(values)

print('Advent of Code Day 16 Answer Part 1:', errors)

# Part 2

rules_map = defaultdict(list)
rules_count = 0
count = 0
new_valids = [ticket] + valids
for key, value in rules_dict.items():
    for i in range(len(new_valids[0])): # which element to check
        for valid in new_valids:
            if valid[i] in value:
                rules_count += 1

        if rules_count == len(new_valids):
            rules_map[key].append(i)

        rules_count = 0

field_map = {}
taken_fields = []
for i in range(1, len(rules_map.keys()) + 1):
    for key, value in rules_map.items():
        if len(value) == i:
            for row in value:
                if row not in taken_fields:
                    field_map[key] = row
                    taken_fields.append(row)
                    break

my_departure = 1
for key, value in field_map.items():
    if 'departure' in key:
        my_departure *= ticket[value]

print('Advent of Code Day 16 Answer Part 2:', my_departure)

