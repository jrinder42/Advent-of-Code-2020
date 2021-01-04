
'''

Advent of Code 2020 - Day 3

'''

import numpy as np

problem = []
with open('day3.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        problem.append([char for char in line])

problem = np.array(problem)
grid = problem
original = problem

# Part 1

for i in range((problem.shape[0] * 3) // problem.shape[1]): # 969
    problem = np.hstack((problem, grid))

nrow = 0
row = 0
col = 0
ntrees = 0
while nrow < problem.shape[0] - 1:
    row += 1
    col += 3
    if problem[row, col] == '#':
        ntrees += 1
    nrow += 1

print('Advent of Code Day 3 Answer Part 1:', ntrees)

# Part 2
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]] # right, down
ntrees = []
for slope in slopes:
    matrix = original
    right, down = slope
    nrows, ncols = matrix.shape
    if right == 1 and down > 1:
        for i in range((matrix.shape[0] // down) // matrix.shape[1]):
            matrix = np.hstack((matrix, grid))

    else: # down is 1
        for i in range((matrix.shape[0] * right) // matrix.shape[1]):
            matrix = np.hstack((matrix, grid))

    row = 0
    col = 0
    ntrees_slope = 0
    while row < matrix.shape[0] - 1:
        row += down
        col += right
        if matrix[row, col] == '#':
            ntrees_slope += 1

    ntrees.append(ntrees_slope)

def mult(x):
    result = 1
    for num in x:
        result *= num
    return result

print('Advent of Code Day 3 Answer Part 2:', mult(ntrees))