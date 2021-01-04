
'''

Advent of Code 2020 - Day 25

'''

# Diffie-Hellman key exchange

card_public_key = 0
door_public_key = 0
with open('day25.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if card_public_key == 0:
            card_public_key = int(line)
        else:
            door_public_key = int(line)

# Part 1

# transforming the subject number into a public key
def transform(subject_number, public_key):
    loop_size = 0
    value = 1
    while value != public_key:
        value *= subject_number
        _, value = divmod(value, 20201227)
        loop_size += 1

    return loop_size

# card's public key --> card's secret loop size
# door's public key --> door's secret loop size

card_loop_size = transform(7, card_public_key)
door_loop_size = transform(7, door_public_key)

def encrypt_transform(subject_number, loop_size):
    value = 1
    for _ in range(loop_size):
        value *= subject_number
        _, value = divmod(value, 20201227)

    return value

encryption_key = encrypt_transform(door_public_key, card_loop_size)

print('Advent of Code Day 25 Answer Part 1:', encryption_key)

# Part 2

print('Advent of Code Day 25 Answer Part 2:', 'we paid our deposit!')



