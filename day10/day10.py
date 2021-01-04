
'''

Advent of Code 2020 - Day 10

'''

from collections import Counter
from itertools import combinations
import numpy as np

jolts = []
with open('day10.txt', 'r') as file:
    for line in file:
        jolts.append( int( line.strip() ) )

# Part 1

jolts = sorted(jolts)
joltage = 0
joltage_diff = []
for jolt in jolts:
    joltage_diff.append(jolt - joltage)
    joltage += joltage_diff[-1]

# device's built-in adapter is 3 higher than the highest adapter
joltage_diff.append(3)
joltage += joltage_diff[-1]
joltage_counter = Counter(joltage_diff)

print('Advent of Code Day 10 Answer Part 1:', joltage_counter[1] * joltage_counter[3])

# Part 2

def is_valid_path(path):
    diffs = np.diff(path)
    for diff in diffs:
        if diff > 3:
            return False
    return True

def generate_paths(potential):
    all_combos = []
    for i in range(1, len(potential) + 1):
        for subset in combinations(potential, i):
            all_combos.append(list(subset))
    return all_combos

def create_path(current_path, additions):
    new_sets = [set(additions[-1]) - set(addition) for addition in additions]
    return [list(set(current_path) - new_set) for new_set in new_sets]


start = len(jolts) - 1
attempted = []
possible_combinations = 1
while start > 0:
    num = jolts[start]
    potential = list(range(num - 1, num - 3 - 1, -1))
    potential = [p for p in potential if p > 0 and p in jolts]
    if len(potential) > 1:
        gp = generate_paths(potential) # generated paths
        count = 0
        for path in gp:
            if path in attempted:
                count += 1
            else:
                attempted.append(path)
        if count > 0:
            start -= 1
            continue

        potential_paths = create_path(jolts, gp)
        nvalids = len([pp for pp in potential_paths if is_valid_path(pp)])
        possible_combinations *= nvalids

    start -= 1

print('Advent of Code Day 10 Answer Part 2:', possible_combinations)


