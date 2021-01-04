
'''

Advent of Code 2020 - Day 7

'''

import numpy as np

bags = {}
num_bags = {}
with open('day7.txt', 'r') as file:
    for line in file:
        bag, contents = line.split('contain')
        bag = bag.strip()
        contents = contents.split('.')[0].split(',')
        contents = [content.strip() for content in contents]

        if bag not in bags:
            bags[bag] = []
            num_bags[bag] = {}
            for content in contents:
                content_bag = content.split(' ')
                key = ' '.join(content_bag[1:])
                if key[-1] != 's':
                    key += 's'
                bags[bag].append(key)

                if content[0].isnumeric():
                    num_bags[bag].update({key: int(content[0])})

bag_depth = {}

for key, value in num_bags.items():
    bag_depth[key] = sum(value.values())

# dijkstra's algorithm

# https://stackoverflow.com/questions/24471136/how-to-find-all-paths-between-two-graph-nodes
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_all_paths(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

count = 0
for key in num_bags:
    all_paths = find_all_paths(bags, key, 'shiny gold bags')
    if all_paths:
        count += 1

print('Advent of Code Day 7 Answer Part 1:', count - 1) # -1 to subtract single "shiny gold bags" item

# Part 2

path_sum = 0
path_list = []
for key in num_bags:
    all_paths = find_all_paths(bags, 'shiny gold bags', key)

    for path in all_paths:
        if len(path) > 1:
            bag_list = []
            for i in range(1, len(path)):
                bag = path[i]
                if i == len(path) - 1: # last element
                    bag_list.append( bag_depth[path[i - 1]] )
                else:
                    bag_list.append( num_bags[path[i - 1]][bag] )

            if bag_list not in path_list:
                path_list.append(bag_list)

for lst in path_list:
    path_sum += np.prod(lst)

# 9565 is too low, 341161 is too high
print('Advent of Code Day 7 Answer Part 2:', path_sum)