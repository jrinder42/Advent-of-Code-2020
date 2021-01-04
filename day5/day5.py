
'''

Advent of Code 2020 - Day 5

'''

import numpy as np

# Part 1

seat_ids = []
with open('day5.txt', 'r') as file:
    passport = {}
    for line in file:
        line = line.strip('\n')
        row_binary = 2**7
        col_binary = 2**3
        row_range = [0, row_binary - 1]
        col_range = [0, col_binary - 1]

        row = line[:7]
        col = line[7:]

        for r in row:
            row_binary /= 2
            if r == 'F':
                row_range = [row_range[0], row_range[1] - row_binary]
            else: # r == 'B'
                row_range = [row_range[0] + row_binary, row_range[1]]

        for c in col:
            col_binary /= 2
            if c == 'L':
                col_range = [col_range[0], col_range[1] - col_binary]
            else: # c == 'R'
                col_range = [col_range[0] + col_binary, col_range[1]]

        seat_ids.append(row_range[0] * 8 + col_range[0])

print('Advent of Code Day 5 Answer Part 1:', int(max(seat_ids)))

# Part 2

sorted_seat_ids = sorted(seat_ids)
sorted_seat_ids = list(map(int, sorted_seat_ids))

diff = np.diff(sorted_seat_ids)
idx = np.where(diff > 1)[0][0]

print('Advent of Code Day 5 Answer Part 2:', sorted_seat_ids[idx] + 1)



