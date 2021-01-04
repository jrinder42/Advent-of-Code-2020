
'''

Advent of Code 2020 - Day 4

'''

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
passports = []
with open('day4.txt', 'r') as file:
    passport = {}
    for line in file:
        line = line.strip('\n').split(' ')
        if len(line) == 1 and line[0] == '':
            passports.append(passport)
            passport = {}
            continue

        for line_item in line:
            info = line_item.split(':')
            passport[info[0]] = info[1]

    passports.append(passport)
    passport = {}

nvalid = 0
for passport in passports:
    keys_len = len(passport.keys())
    if keys_len == len(fields) or ('cid' not in passport.keys() and keys_len == len(fields) - 1):
        nvalid += 1

print('Advent of Code Day 4 Answer Part 1:', nvalid) # 238 is too low, 268 is too high

# Part 2

def rules(field, value):
    if field == 'byr':
        value = int(value)
        if len(str(value)) == 4 and 1920 <= value and value <= 2002:
            return True
    elif field == 'iyr':
        value = int(value)
        if len(str(value)) == 4 and 2010 <= value and value <= 2020:
            return True
    elif field == 'eyr':
        value = int(value)
        if len(str(value)) == 4 and 2020 <= value and value <= 2030:
            return True
    elif field == 'hgt':
        if len(value) > 2:
            val = int(value[:-2], 10)
            if value[-2:] == 'in' and 59 <= val and val <= 76:
                return True
            elif value[-2:] == 'cm' and 150 <= val and val <= 193:
                return True
    elif field == 'hcl':
        char_list = ['a', 'b', 'c', 'd', 'e', 'f']
        num_list = list(range(0, 9 + 1))
        num_list = list(map(str, num_list))
        character_condition = len([char for char in value[1:] if (char in char_list or char in num_list)]) == 6
        if value[0] == '#' and len(value[1:]) == 6 and character_condition:
            return True
    elif field == 'ecl':
        eye_color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if len(value) == 3 and value in eye_color:
            return True
    elif field == 'pid':
        if len(value) == 9 and value.isnumeric():
            return True
    elif field == 'cid':
        return True
    return False

nvalid = 0
for passport in passports:
    count = 0
    for key, value in passport.items():
        if key in fields[:-1] and rules(key, value):
            count += 1

    if count > 6:
        nvalid += 1

print('Advent of Code Day 4 Answer Part 2:', nvalid) # 10 is not correct