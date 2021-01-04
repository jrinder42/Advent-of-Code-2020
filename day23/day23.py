
'''

Advent of Code 2020 - Day 23

'''

# Part 1

#cups = '389125467'
cups = '784235916'
cups = [int(num) for num in cups]
current_cup_index = 0
current_cup = cups[current_cup_index]

for _ in range(100):
    pickups = []
    pickups_index = []
    for i in range(1, 3 + 1):
        pickups_index.append((current_cup_index + i) % len(cups))
        pickups.append(cups[pickups_index[-1]])

    cups = [cup for cup in cups if cups.index(cup) not in pickups_index]

    sorted_cups = sorted(cups)
    sorted_cup_index = sorted_cups.index(current_cup)
    destination_cup = 0

    if sorted_cups[:sorted_cup_index]: # if there is a smaller number in the cup list
        destination_cup = sorted_cups[:sorted_cup_index][-1]
    else:
        destination_cup = max(sorted_cups[sorted_cup_index + 1:])

    destination_index = cups.index(destination_cup)

    for i in range(1, 3 + 1):
        cups.insert(destination_index + i, pickups[i - 1])

    current_cup_index = cups.index(current_cup) + 1
    if current_cup_index == len(cups):
        current_cup_index = 0
    current_cup = cups[current_cup_index]

one_index = cups.index(1)
label = ''
for i in range(1, len(cups)):
    label += str(cups[(one_index + i) % len(cups)])

print('Advent of Code Day 23 Answer Part 1:', label)

# Part 2

#cups = '389125467'
cups = '784235916'
cups = [int(num) for num in cups]
extra_cups = list(range(int(max(cups)) + 1, 1_000_000 + 1))
cups += extra_cups

# create dictionary as a linked list
cups_dict = {cups[-1]: cups[0]}
for i, cup in enumerate(cups[:-1]):
    cups_dict[cup] = cups[i + 1]
current_cup = cups[0]

for _ in range(10_000_000):
    pickups = []
    to_pickup = cups_dict[current_cup]
    for i in range(3):
        pickups.append(to_pickup)
        to_pickup = cups_dict[to_pickup]

    destination_cup = 0
    count = 1
    while destination_cup == 0:
        if current_cup - count == 0:
            destination_cup = max(set(cups_dict).symmetric_difference(pickups))
        elif current_cup - count > 0 and current_cup - count not in pickups:
            destination_cup = current_cup - count
        count += 1

    cups_dict[current_cup] = cups_dict[pickups[2]]
    cups_dict[pickups[2]] = cups_dict[destination_cup]
    cups_dict[destination_cup] = pickups[0]

    current_cup = cups_dict[current_cup]

to_cup = cups_dict[1]
label_multiply = to_cup * cups_dict[to_cup]

print('Advent of Code Day 23 Answer Part 2:', label_multiply)
