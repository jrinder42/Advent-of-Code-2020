
'''

Advent of Code 2020 - Day 20

'''

import numpy as np

# works for n x n matrices with n >= 3

# i was super lazy with the code, so there is a lot of copy and pasting

tiles = {}
with open('day20.txt', 'r') as file:
    tile = []
    name = 0
    for line in file:
        if line.strip() == '':
            tiles[name] = np.array(tile) # 10 x 10 matrix
            tile = []
            continue
        elif line.strip()[:4] == 'Tile':
            name = line.strip()[:-1].split(' ')[1]
            name = int(name)
        else:
            tile.append([char for char in line.strip()])

    tiles[name] = np.array(tile)
    tile = []

# Part 1

touching_tiles = {}
rot_matrices = {}
index_tiles = {}
tile_matrices = {} # only for middles
for key, value in tiles.items():
    matrix = value
    rot_matrices[key] = [matrix, np.flipud(matrix), np.fliplr(matrix),
                         np.rot90(matrix, 1), np.flipud(np.rot90(matrix, 1)), np.fliplr(np.rot90(matrix, 1)),
                         np.rot90(matrix, 2), np.flipud(np.rot90(matrix, 2)), np.fliplr(np.rot90(matrix, 2)),
                         np.rot90(matrix, 3), np.flipud(np.rot90(matrix, 3)), np.fliplr(np.rot90(matrix, 3))]

count_dict = {}
for outer_key, outer_value in tiles.items():
    matrix = outer_value
    nrows, ncols = matrix.shape

    inner_template = np.zeros((3, 3))
    inner_index_template = np.zeros((3, 3))
    count_unique = []
    for inner_key, inner_value in tiles.items():
        if inner_key == outer_key: # if this is the current tile
            continue

        inner_matrix = inner_value
        potentials = rot_matrices[inner_key]
        inner_index_template[1, 1] = 0
        for i, potential in enumerate(potentials): # iterate over all other rotations
            if np.all(matrix[:, ncols - 1] == potential[:, 0]):
                inner_template[1, 1] = outer_key
                inner_template[1, 2] = inner_key
                inner_index_template[1, 2] = i
                count_unique.append(inner_key)
            elif np.all(matrix[:, 0] == potential[:, ncols - 1]):
                inner_template[1, 1] = outer_key
                inner_template[1, 0] = inner_key
                inner_index_template[1, 0] = i
                count_unique.append(inner_key)
            elif np.all(matrix[nrows - 1, :] == potential[0, :]):
                inner_template[1, 1] = outer_key
                inner_template[2, 1] = inner_key
                inner_index_template[2, 1] = i
                count_unique.append(inner_key)
            elif np.all(matrix[0, :] == potential[nrows - 1, :]):
                inner_template[1, 1] = outer_key
                inner_template[0, 1] = inner_key
                inner_index_template[0, 1] = i
                count_unique.append(inner_key)

    touching_tiles[outer_key] = inner_template
    index_tiles[outer_key] = inner_index_template

    count_dict[outer_key] = len(list(set(count_unique)))

    if count_dict[outer_key] == 4:
        tile_matrix = np.empty([30, 30], dtype=str)

        tile_matrix[:10, 10:20] = rot_matrices[touching_tiles[outer_key][0, 1]][int(index_tiles[outer_key][0, 1])]  # up middle
        tile_matrix[10:20, :10] = rot_matrices[touching_tiles[outer_key][1, 0]][int(index_tiles[outer_key][1, 0])]  # left middle
        tile_matrix[10:20, 10:20] = rot_matrices[touching_tiles[outer_key][1, 1]][int(index_tiles[outer_key][1, 1])]  # middle
        tile_matrix[10:20, 20:] = rot_matrices[touching_tiles[outer_key][1, 2]][int(index_tiles[outer_key][1, 2])]  # right middle
        tile_matrix[20:, 10:20] = rot_matrices[touching_tiles[outer_key][2, 1]][int(index_tiles[outer_key][2, 1])]  # down middle
        tile_matrix[tile_matrix == ''] = ' '

        tile_matrices[outer_key] = tile_matrix

corners = []
edges = []
middles = []
for key, value in count_dict.items():
    if value == 2:
        corners.append(key)
    if value == 3:
        edges.append(key)
    elif value == 4:
        middles.append(key)

corner_ids = 1
for corner in corners:
    corner_ids *= corner

print('Advent of Code Day 20 Answer Part 1 - without the full image:', corner_ids)

# Part 2

def surrounding(tile):
    n, s, e, w = 0, 0, 0, 0

    if any(num > 0 for num in tile[0, :]):
        n += 1
    if any(num > 0 for num in tile[2, :]):
        s += 1
    if any(num > 0 for num in tile[:, 2]):
        e += 1
    if any(num > 0 for num in tile[:, 0]):
        w += 1
    return (n, s, e, w)

def rotate_tile(tile, target):
    matrix = touching_tiles[tile]
    potentials = [matrix, np.flipud(matrix), np.fliplr(matrix),
                  np.rot90(matrix, 1), np.flipud(np.rot90(matrix, 1)), np.fliplr(np.rot90(matrix, 1)),
                  np.rot90(matrix, 2), np.flipud(np.rot90(matrix, 2)), np.fliplr(np.rot90(matrix, 2)),
                  np.rot90(matrix, 3), np.flipud(np.rot90(matrix, 3)), np.fliplr(np.rot90(matrix, 3))]
    for potential in potentials:
        if surrounding(potential) == target:
            return potential
    return np.array([])

def find_corner(edge_tile):
    for key, value in touching_tiles.items():
        if key in corners and key == edge_tile:
            return [key, value]
    return []

def find_edge(corner_tile):
    for key, value in touching_tiles.items():
        if key in edges and key == corner_tile:
            return [key, value]
    return []

current_tile = corners[0]
current_matrix = touching_tiles[current_tile]

size = np.sqrt(len(tiles))
size = int(np.floor(size))
image = np.zeros((size, size))

# insert first corner

rotated_tile = rotate_tile(corners[0], (0, 1, 1, 0)) # n, s, e, w

image[:2, :2] = rotated_tile[1:, 1:]

current_tile = corners[0]
corners.remove(corners[0])

# get edges of matrix

while corners or edges:
    if not corners and not edges:
        break

    # get edge for a given tile
    idx = np.where(image == current_tile)
    row, col = idx[0][0], idx[1][0]
    edge = find_edge(image[0, col + 1])

    if edge: # edge key not in image
        # if edge exists, insert edge
        rotated_tile = rotate_tile(edge[0], (0, 1, 1, 1))
        if rotated_tile[1, 0] != image[0, col]:
            rotated_tile[1, 0], rotated_tile[1, 2] = rotated_tile[1, 2], rotated_tile[1, 0]

        image[0, col + 1] = rotated_tile[1, 1]
        image[1, col + 1] = rotated_tile[2, 1]
        image[0, col + 2] = rotated_tile[1, 2]
        current_tile = edge[0]
        edges.remove(edge[0])
    else:
        # if edge does not exist, insert corner
        image = np.rot90(image, 1) # rotate 90 degrees counter-clockwise
        # top left corner
        corner = find_corner(image[0, 0])
        rotated_tile = rotate_tile(corner[0], (0, 1, 1, 0)) # n, s, e, w
        if rotated_tile[2, 1] != image[1, 0]:
            # flip
            rotated_tile[2, 1], rotated_tile[1, 2] = rotated_tile[1, 2], rotated_tile[2, 1]

        image[0, 0] = rotated_tile[1, 1]
        image[0, 1] = rotated_tile[1, 2]
        current_tile = corner[0]
        corners.remove(corner[0])

# get middle section of final matrix

def rotate_middle_tile(tile, left, up):
    matrix = touching_tiles[tile]
    large_matrix = tile_matrices[tile]
    potentials = [matrix, np.flipud(matrix), np.fliplr(matrix),
                  np.rot90(matrix, 1), np.flipud(np.rot90(matrix, 1)), np.fliplr(np.rot90(matrix, 1)),
                  np.rot90(matrix, 2), np.flipud(np.rot90(matrix, 2)), np.fliplr(np.rot90(matrix, 2)),
                  np.rot90(matrix, 3), np.flipud(np.rot90(matrix, 3)), np.fliplr(np.rot90(matrix, 3))]
    large_potentials = [large_matrix, np.flipud(large_matrix), np.fliplr(large_matrix),
                        np.rot90(large_matrix, 1), np.flipud(np.rot90(large_matrix, 1)), np.fliplr(np.rot90(large_matrix, 1)),
                        np.rot90(large_matrix, 2), np.flipud(np.rot90(large_matrix, 2)), np.fliplr(np.rot90(large_matrix, 2)),
                        np.rot90(large_matrix, 3), np.flipud(np.rot90(large_matrix, 3)), np.fliplr(np.rot90(large_matrix, 3))]
    for i, potential in enumerate(potentials):
        if potential[1, 0] == left and potential[0, 1] == up:
            tile_matrices[tile] = large_potentials[i]  # rotate larger 30 x 30 matrix
            return potential
    return np.array([])

for row in range(1, size - 1):
    for col in range(1, size - 1):
        middle = touching_tiles[image[row, col]]
        rotated_tile = rotate_middle_tile(image[row, col], image[row, col - 1], image[row - 1, col])
        image[row, col + 1] = rotated_tile[1, 2]
        image[row + 1, col] = rotated_tile[2, 1]
        middles.remove(image[row, col])

corners = [image[0, 0], image[0, image.shape[1] - 1],
           image[image.shape[0] - 1, 0], image[image.shape[0] - 1, image.shape[1] - 1]]

corner_ids = 1
for corner in corners:
    corner_ids *= corner

print('Advent of Code Day 20 Answer Part 1 - with the full image:', int(corner_ids))

# corner fix

# top left
nrows, ncols = tiles[image[0, 0]].shape
for potential in rot_matrices[image[0, 0]]:
    side1 = np.all(potential[:, ncols - 1] == tile_matrices[image[1, 1]][:10, 10])
    side2 = np.all(potential[nrows - 1, :] == tile_matrices[image[1, 1]][10, :10])
    if side1 and side2:
        tile_matrices[image[1, 1]][:10, :10] = potential

# top right
for potential in rot_matrices[image[0, size - 1]]:
    side1 = np.all(potential[:, 0] == tile_matrices[image[1, size - 2]][:10, 20 - 1])
    side2 = np.all(potential[nrows - 1, :] == tile_matrices[image[1, size - 2]][10, 20:])
    if side1 and side2:
        tile_matrices[image[1, size - 2]][:10, 20:] = potential

# bottom left
for potential in rot_matrices[image[size - 1, 0]]:
    side1 = np.all(potential[:, ncols - 1] == tile_matrices[image[size - 2, 1]][20:, 10])
    side2 = np.all(potential[0, :] == tile_matrices[image[size - 2, 1]][20 - 1, :10])
    if side1 and side2:
        tile_matrices[image[size - 2, 1]][20:, :10] = potential

# bottom right
for potential in rot_matrices[image[size - 1, size - 1]]:
    side1 = np.all(potential[:, 0] == tile_matrices[image[size - 2, size - 2]][20:, 20 - 1])
    side2 = np.all(potential[0, :] == tile_matrices[image[size - 2, size - 2]][20 - 1, 20:])
    if side1 and side2:
        tile_matrices[image[size - 2, size - 2]][20:, 20:] = potential


# remove borders for part 2
for key, value in tile_matrices.items():
    matrix = np.delete(value, [0, 10 - 1, 10, 20 - 1, 20, 30 - 1], axis=1) # columns
    matrix = np.delete(matrix, [0, 10 - 1, 10, 20 - 1, 20, 30 - 1], axis=0) # rows
    tile_matrices[key] = matrix

# final

final_row_image = []
for row in range(1, image.shape[0] - 1):
    col_image = []
    for col in range(1, image.shape[1] - 1):
        if col == 1:
            col_image.append( tile_matrices[image[row, col]][:, :16] )
        elif col == image.shape[1] - 2:
            col_image.append( tile_matrices[image[row, col]][:, 8:] )
        else:
            col_image.append( tile_matrices[image[row, col]][:, 8:16] )
    if row == 1:
        final_row_image.append( np.hstack(col_image)[:16, :] )
    elif row == image.shape[0] - 2:
        final_row_image.append( np.hstack(col_image)[8:, :] )
    else:
        final_row_image.append( np.hstack(col_image)[8:16, :] )

final_image = np.vstack(final_row_image)

monster = '''
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
'''

monster = [[char for char in row] for row in monster.split('\n')]
monster = [lst for lst in monster if lst]
monster = np.array(monster)
target_count = 0 # number of #
for r in range(monster.shape[0]):
    for c in range(monster.shape[1]):
        if monster[r, c] == '#':
            target_count += 1

potentials = [final_image, np.flipud(final_image), np.fliplr(final_image),
              np.rot90(final_image, 1), np.flipud(np.rot90(final_image, 1)), np.fliplr(np.rot90(final_image, 1)),
              np.rot90(final_image, 2), np.flipud(np.rot90(final_image, 2)), np.fliplr(np.rot90(final_image, 2)),
              np.rot90(final_image, 3), np.flipud(np.rot90(final_image, 3)), np.fliplr(np.rot90(final_image, 3))]

monster_count = 0
water_roughness = 0
for potential in potentials:
    monster_count = 0
    for row in range(potential.shape[0] - monster.shape[0]):
        for col in range(potential.shape[1] - monster.shape[1]):
            square_count = 0
            square_indexes = []
            potential_monster = potential[row:row + monster.shape[0], col:col + monster.shape[1]]
            for r in range(potential_monster.shape[0]):
                for c in range(potential_monster.shape[1]):
                    if potential_monster[r, c] == '#' and monster[r, c] == '#':
                        square_count += 1

            if square_count == target_count:
                monster_count += 1

    if monster_count > 0:
        water_roughness = 0
        for r in range(potential.shape[0]):
            for c in range(potential.shape[1]):
                if potential[r, c] == '#':
                    water_roughness += 1
        water_roughness -= monster_count * 15 # 15 is the number of # in the monster
        break

print('Advent of Code Day 20 Answer Part 2:', water_roughness)



