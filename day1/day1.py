
'''

Advent of Code 2020 - Day 1

'''

# 0-1 Knapsack Problem

nums = []
with open('day1.txt', 'r') as file:
    for line in file:
        nums.append(float(line))

# Part 1

def greed(v, target):
    for i in range(len(v)):
        for j in range(i + 1, len(v)):
            if v[i] + v[j] == target:
                return [int(v[i]), int(v[j])]
    return []

def mult(x):
    result = 1
    for num in x:
        result *= num
    return result

print('Advent of Code Day 1 Answer Part 1:', mult( greed(nums, 2020) ))

# Part 2

def subset_sum(numbers, target, partial=[], partial_sum=0):
    if partial_sum == target:
        yield partial
    if partial_sum >= target:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1:]
        yield from subset_sum(remaining, target, partial + [n], partial_sum + n)

possibles = list(subset_sum(nums, 2020))
for i in range(len(possibles)):
    for j in range(len(possibles[i])):
        possibles[i][j] = int(possibles[i][j])

p = [possible for possible in possibles if len(possible) == 3]

print('Advent of Code Day 1 Answer Part 2:', mult( p[0] ))
