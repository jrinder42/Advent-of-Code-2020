
'''

Advent of Code 2020 - Day 9

'''

xmas = []
with open('day9.txt', 'r') as file:
    for line in file:
        xmas.append( int( line.strip() ) )

# Part 1

preamble_length = 25

def subset_sum(numbers, target, partial=[], partial_sum=0):
    if partial_sum == target:
        yield partial
    if partial_sum >= target:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1:]
        yield from subset_sum(remaining, target, partial + [n], partial_sum + n)

weakness = 0
for num in range(len(xmas) - preamble_length):
    preamble = xmas[num:num + preamble_length]
    possibles = list(subset_sum(preamble, xmas[num + preamble_length]))
    valids = 0
    for possible in possibles:
        if len(possible) == 2:
            valids += 1
    if not valids:
        weakness = xmas[num + preamble_length]
        break

print('Advent of Code Day 9 Answer Part 1:', weakness)

# Part 2

continuous = []
start = 0
count = 0
continuous_encrypt = 0
while start < len(xmas):
    if sum(continuous) == weakness:
        continuous_encrypt = min(continuous) + max(continuous)
        break
    elif sum(continuous) > weakness: # reset
        start += 1
        count = 0
        continuous = []
    else:
        continuous.append(xmas[start + count])
        count += 1

print('Advent of Code Day 9 Answer Part 2:', continuous_encrypt)