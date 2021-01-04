
'''

Advent of Code 2020 - Day 17

'''

from itertools import product

init_cubes = []
with open('day17.txt', 'r') as file:
    for line in file:
        line = line.strip()
        line = line.replace('#', '1')
        line = line.replace('.', '0')
        init_cubes.append( [int(char) for char in line] )

cubes = {}
for r in range(len(init_cubes)):
    for c in range(len(init_cubes[0])):
        cubes[(r, c, 0)] = init_cubes[r][c]

# Part 1 - 3 dimensions

def edge_cubes(cube):
    x, y, z = cube
    edges = []
    for adjacent_cube in product([-1, 0, 1], repeat=3):
        if adjacent_cube == (0, 0, 0):
            continue
        new_x = x + adjacent_cube[0]
        new_y = y + adjacent_cube[1]
        new_z = z + adjacent_cube[2]
        edges.append((new_x, new_y, new_z))
    return edges

def boot_process(cubes, cycles=1):
    for cycle in range(1, cycles + 1):
        new_cubes = set(adjacent_cube for cube in cubes for adjacent_cube in edge_cubes(cube))
        for cube in cubes:
            new_cubes.add(cube)

        for cube in new_cubes:
            if cube not in cubes:
                cubes[cube] = 0

        to_modify = set()

        for cube in new_cubes:
            active_cubes = 0
            for adjacent_cube in edge_cubes(cube):
                if adjacent_cube in cubes:
                    active_cubes += cubes[adjacent_cube]

            if cubes[cube] == 1 and active_cubes not in [2, 3]:
                to_modify.add((cube, 0))
            elif cubes[cube] == 0 and active_cubes == 3:
                to_modify.add((cube, 1))

        for modified_cube in to_modify:
            updated_cube = {modified_cube[0]: modified_cube[1]}
            cubes.update(updated_cube)

    return sum(cubes.values())

print('Advent of Code Day 17 Answer Part 1:', boot_process(cubes, cycles=6))

# Part 2 - 4 dimensions

cubes_4d = {}
for r in range(len(init_cubes)):
    for c in range(len(init_cubes[0])):
        cubes_4d[(r, c, 0, 0)] = init_cubes[r][c]

def edge_cubes_4d(cube):
    x, y, z, w = cube
    edges = []
    for adjacent_cube in product([-1, 0, 1], repeat=4):
        if adjacent_cube == (0, 0, 0, 0):
            continue
        new_x = x + adjacent_cube[0]
        new_y = y + adjacent_cube[1]
        new_z = z + adjacent_cube[2]
        new_w = w + adjacent_cube[3]
        edges.append((new_x, new_y, new_z, new_w))
    return edges

def boot_process_4d(cubes, cycles=1):
    for cycle in range(1, cycles + 1):
        new_cubes = set(adjacent_cube for cube in cubes for adjacent_cube in edge_cubes_4d(cube))
        for cube in cubes:
            new_cubes.add(cube)

        for cube in new_cubes:
            if cube not in cubes:
                cubes[cube] = 0

        to_modify = set()

        for cube in new_cubes:
            active_cubes = 0
            for adjacent_cube in edge_cubes_4d(cube):
                if adjacent_cube in cubes:
                    active_cubes += cubes[adjacent_cube]

            if cubes[cube] == 1 and active_cubes not in [2, 3]:
                to_modify.add((cube, 0))
            elif cubes[cube] == 0 and active_cubes == 3:
                to_modify.add((cube, 1))

        for modified_cube in to_modify:
            updated_cube = {modified_cube[0]: modified_cube[1]}
            cubes.update(updated_cube)

    return sum(cubes.values())

print('Advent of Code Day 17 Answer Part 2:', boot_process_4d(cubes_4d, cycles=6))


