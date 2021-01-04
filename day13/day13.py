
'''

Advent of Code 2020 - Day 13

'''

from functools import reduce

earliest_departure = 0
buses = []
odd_buses = []
with open('day13.txt', 'r') as file:
    for i, line in enumerate(file):
        if i == 0:
            earliest_departure = int(line.strip())
        else: # i == 1
            buses = line.strip().split(',')
            odd_buses = [int(bus) if bus != 'x' else 0 for bus in buses] # for part 2
            buses = [int(bus) for bus in buses if bus != 'x']

# Part 1

earliest_bus = 0
wait_time = earliest_departure # in minutes
for bus in buses:
    next_bus = earliest_departure // bus * bus + bus
    if next_bus - earliest_departure < wait_time:
        earliest_bus = bus
        wait_time = next_bus - earliest_departure

print('Advent of Code Day 13 Answer Part 1:', earliest_bus * wait_time)

# Part 2

def chinese_remainder(n, a):
    s = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        s += a_i * mul_inv(p, n_i) * p
    return s % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1

n = []
a = []
for i, bus in enumerate(odd_buses):
    if bus != 0:
        n.append(bus)
        a.append(bus - i)

print('Advent of Code Day 13 Answer Part 2:', chinese_remainder(n, a))


