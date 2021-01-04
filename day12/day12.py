
'''

Advent of Code 2020 - Day 12

'''

import numpy as np

actions = []
with open('day12.txt', 'r') as file:
    for line in file:
        l = line.strip()
        action, value = l[0], int(l[1:])
        actions.append({'action': action, 'value': value})

# Part 1

heading = {'N': 90, 'E': 0, 'S': 270, 'W': 180}
reverse_heading = {90: 'N', 0: 'E', 270: 'S', 180: 'W'}

current_heading = heading['E']
vertical = 0
horizontal = 0

for action in actions:
    if action['action'] == 'N':
        vertical += action['value']
    elif action['action'] == 'E':
        horizontal += action['value']
    elif action['action'] == 'S':
        vertical -= action['value']
    elif action['action'] == 'W':
        horizontal -= action['value']
    elif action['action'] == 'L':
        move = action['value'] % 360
        current_heading += move
        current_heading = current_heading % 360
    elif action['action'] == 'R':
        move = -1 * action['value'] % 360
        current_heading += move
        current_heading = current_heading % 360
    elif action['action'] == 'F':
        if reverse_heading[current_heading] == 'N':
            vertical += action['value']
        elif reverse_heading[current_heading] == 'E':
            horizontal += action['value']
        elif reverse_heading[current_heading] == 'S':
            vertical -= action['value']
        elif reverse_heading[current_heading] == 'W':
            horizontal -= action['value']

print('Advent of Code Day 12 Answer Part 1:', abs(vertical) + abs(horizontal))

# Part 2

def rotate(point, origin, degrees):
    radians = np.deg2rad(degrees)
    x,y = point
    offset_x, offset_y = origin
    adjusted_x = (x - offset_x)
    adjusted_y = (y - offset_y)
    cos_rad = np.cos(radians)
    sin_rad = np.sin(radians)
    qx = offset_x + cos_rad * adjusted_x + sin_rad * adjusted_y
    qy = offset_y + -sin_rad * adjusted_x + cos_rad * adjusted_y
    return qx, qy

current_heading = heading['E'] # this is for the waypoint
vertical = 0
horizontal = 0
waypoint_vertical = 1
waypoint_horizontal = 10

for action in actions:
    if action['action'] == 'N':
        waypoint_vertical += action['value']
    elif action['action'] == 'E':
        waypoint_horizontal += action['value']
    elif action['action'] == 'S':
        waypoint_vertical -= action['value']
    elif action['action'] == 'W':
        waypoint_horizontal -= action['value']
    elif action['action'] == 'L':
        waypoint_horizontal, waypoint_vertical = rotate([waypoint_horizontal, waypoint_vertical],
                                                        [0, 0],
                                                        -action['value'])
        waypoint_horizontal, waypoint_vertical = list(map(round, [waypoint_horizontal, waypoint_vertical]))
        waypoint_horizontal, waypoint_vertical = list(map(int, [waypoint_horizontal, waypoint_vertical]))
    elif action['action'] == 'R':
        waypoint_horizontal, waypoint_vertical = rotate([waypoint_horizontal, waypoint_vertical],
                                                        [0, 0],
                                                        action['value'])
        waypoint_horizontal, waypoint_vertical = list(map(round, [waypoint_horizontal, waypoint_vertical]))
        waypoint_horizontal, waypoint_vertical = list(map(int, [waypoint_horizontal, waypoint_vertical]))
    elif action['action'] == 'F':
        vertical += action['value'] * waypoint_vertical
        horizontal += action['value'] * waypoint_horizontal


# 55014 is too high | 33732 is too low
print('Advent of Code Day 12 Answer Part 2:', abs(vertical) + abs(horizontal))
