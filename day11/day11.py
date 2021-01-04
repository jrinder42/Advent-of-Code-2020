
'''

Advent of Code 2020 - Day 11

'''

import numpy as np
from collections import Counter
from copy import deepcopy

layout = []
with open('day11.txt', 'r') as file:
    for line in file:
        layout.append( [char for char in line.strip()] ) # . is floor, L is empty, # is occupied

layout = np.array(layout)
new_layout = np.empty([layout.shape[0] + 2, layout.shape[1] + 2], dtype=str)
offset = 1
new_layout[offset:layout.shape[0] + offset, offset:layout.shape[1] + offset] = layout
layout = new_layout

# Part 1

def round(matrix):
    new_layout = deepcopy(matrix)
    for i in range(offset, matrix.shape[0] - offset):
        for j in range(offset, matrix.shape[1] - offset):
            subset = matrix[i - 1:i + 2, j - 1:j + 2] # 3 x 3 matrix
            flat = subset.flatten()
            c = Counter(flat)
            if '#' not in c and matrix[i, j] == 'L': # no occupied seats around this empty seat
                new_layout[i, j] = '#' # now the empty seat is occupied
            elif '#' in c and c['#'] > 4 and matrix[i, j] == '#': # greater than 4 because this seat is occupied
                new_layout[i, j] = 'L' # now the occupied seat is empty

    return new_layout

match = False
seats = 0 # occuped seats
layout_1 = deepcopy(layout)
while not match:
    updated_layout = round(layout_1)
    if (updated_layout == layout_1).all():
        match = True
    layout_1 = updated_layout

print('Advent of Code Day 11 Answer Part 1:', Counter(layout_1.flatten())['#'])

# Part 2

def first_index(values, target):
    for i, value in enumerate(values):
        if value != target:
            return i
    return -1

def custom_subset(matrix, x, y):
    result = np.empty([3, 3], dtype=str)
    result[1, 1] = matrix[x, y]

    # horizontal
    lst = matrix[x, :]
    left = lst[:y]
    if '#' not in left and 'L' not in left:
        result[1, 0] = '.'
    else:
        result[1, 0] = left[ len(left) - 1 - first_index(left[::-1], '.') ]

    right = lst[y + 1:]
    if '#' not in right and 'L' not in right:
        result[1, 2] = '.'
    else:
        result[1, 2] = right[ first_index(right, '.') ]

    # vertical
    lst = matrix[:, y]
    up = lst[:x]
    if '#' not in up and 'L' not in up:
        result[0, 1] = '.'
    else:
        result[0, 1] = up[ len(up) - 1 - first_index(up[::-1], '.') ]

    down = lst[x + 1:]
    if '#' not in down and 'L' not in down:
        result[2, 1] = '.'
    else:
        result[2, 1] = down[ first_index(down, '.') ]

    # main diagonal
    o = y - x # offset
    lst = np.diagonal(matrix, offset=o)
    if o < 0:
        up_left = lst[:y]
    else:
        up_left = lst[:x] # fixed to be x instead of y

    if '#' not in up_left and 'L' not in up_left:
        result[0, 0] = '.'
    else:
        result[0, 0] = up_left[ len(up_left) - 1 - first_index(up_left[::-1], '.') ]

    if o < 0:
        down_right = lst[y + 1:]
    else:
        down_right = lst[x + 1:]

    if '#' not in down_right and 'L' not in down_right:
        result[2, 2] = '.'
    else:
        result[2, 2] = down_right[ first_index(down_right, '.') ]

    # off diagonal
    flipped_matrix = np.flipud(matrix)
    new_x = flipped_matrix.shape[0] - 1 - x
    o = y - new_x
    lst = np.diagonal(flipped_matrix, offset=o)

    if o < 0:
        down_left = lst[:y]
    else:
        down_left = lst[:new_x]

    if '#' not in down_left and 'L' not in down_left: 
        result[2, 0] = '.'
    else:
        result[2, 0] = down_left[ len(down_left) - 1 - first_index(down_left[::-1], '.') ]

    if o < 0:
        up_right = lst[y + 1:]
    else:
        up_right = lst[new_x + 1:]

    if '#' not in up_right and 'L' not in up_right:
        result[0, 2] = '.'
    else:
        result[0, 2] = up_right[ first_index(up_right, '.') ]

    return result

def round_2(matrix):
    new_layout = deepcopy(matrix)
    for i in range(offset, matrix.shape[0] - offset):
        for j in range(offset, matrix.shape[1] - offset):
            subset = custom_subset(matrix, i, j)
            flat = subset.flatten()
            c = Counter(flat)
            if '#' not in c and matrix[i, j] == 'L': # no occupied seats around this empty seat
                new_layout[i, j] = '#' # now the empty seat is occupied
            elif '#' in c and c['#'] > 5 and matrix[i, j] == '#': # greater than 5 because this seat is occupied
                new_layout[i, j] = 'L' # now the occupied seat is empty

    return new_layout

match = False
layout_2 = deepcopy(layout)
while not match:
    updated_layout = round_2(layout_2)
    if (updated_layout == layout_2).all():
        match = True
    layout_2 = updated_layout

print('Advent of Code Day 11 Answer Part 2:', Counter(layout_2.flatten())['#'])

