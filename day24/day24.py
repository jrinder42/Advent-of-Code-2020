
'''

Advent of Code 2020 - Day 24

'''

tiles = []
with open('day24.txt', 'r') as file:
    for line in file:
        line = line.strip()

        line = line.replace('n', ' n ')
        line = line.replace('e', ' e ')
        line = line.replace('w', ' w ')
        line = line.replace('s', ' s ')

        tiles.append([char.strip() for char in line.split(' ') if char != ''])

# Part 1

tiles_dict = {}
for tile in tiles:
    # start at the center
    x = 0
    y = 0

    prev_direction = ''
    for direction in tile:
        if direction == 'n':
            y += 1
        elif direction == 'e':
            x += 1
            if prev_direction in ['n', 's']:
                x -= 0.5
        elif direction == 's':
            y -= 1
        elif direction == 'w':
            x -= 1
            if prev_direction in ['n', 's']:
                x += 0.5

        prev_direction = direction

    if (x, y) not in tiles_dict:
        tiles_dict[(x, y)] = 1
    else:
        tiles_dict[(x, y)] = 1 if tiles_dict[(x, y)] == 0 else 0

print('Advent of Code Day 24 Answer Part 1:', sum(tiles_dict.values()))

# Part 2

def surrounding_tile(tile):
    x, y = tile
    return [(x - 1, y), (x + 1, y), (x - 0.5, y + 1), (x - 0.5, y - 1), (x + 0.5, y + 1), (x + 0.5, y - 1)]

def living_art(tile_floor, days=1):
    for day in range(1, days + 1):
        new_tiles = set(adjacent_tile for tile in tiles_dict for adjacent_tile in surrounding_tile(tile))
        for tile in tiles_dict:
            new_tiles.add(tile)

        for tile in new_tiles:
            if tile not in tile_floor:
                tile_floor[tile] = 0

        to_modify = set()
        for tile in new_tiles:
            tile_count = 0
            for adjacent_tile in surrounding_tile(tile):
                if adjacent_tile in new_tiles:
                    tile_count += tile_floor[adjacent_tile]

            if tile_floor[tile] == 1 and (tile_count == 0 or tile_count > 2):
                to_modify.add((tile, 0))
            elif tile_floor[tile] == 0 and tile_count == 2:
                to_modify.add((tile, 1))

        # sets cannot hold dictionaries, so have to convert from a tuple
        for modified_tile in to_modify:
            updated_tile = {modified_tile[0]: modified_tile[1]}
            tile_floor.update(updated_tile)

    return sum(tile_floor.values())

print('Advent of Code Day 24 Answer Part 2:', living_art(tiles_dict, days=100))