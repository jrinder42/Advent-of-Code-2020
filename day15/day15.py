
'''

Advent of Code 2020 - Day 15

'''

lookup = {0: [1],
          3: [2],
          1: [3],
          6: [4],
          7: [5],
          5: [6]}
turn = 7
prev = 5
while turn != 2020 + 1: # Part 1
    #while turn != 30_000_000 + 1: # Part 2
    if prev in lookup and len(lookup[prev]) == 1:
        prev = 0
        if prev in lookup:
            lookup[prev].append(turn)
        else:
            lookup[prev] = [turn]
    elif prev in lookup: # not unique
        prev = lookup[prev][-1] - lookup[prev][-2] # most recent - second most recent
        if prev in lookup:
            lookup[prev].append(turn)
        else:
            lookup[prev] = [turn]
    turn += 1

print('Advent of Code Day 15 Answer Part 1 / 2:', prev) # depends on while loop condition

