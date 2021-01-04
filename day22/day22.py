
'''

Advent of Code 2020 - Day 22

'''

from collections import deque
from copy import deepcopy
from itertools import islice

players = {}
with open('day22.txt', 'r') as file:
    cards = []
    for line in file:
        line = line.strip()
        if line == '' and 'Player 2' not in players and 'Player 1' in players:
            players['Player 1'] = deque(cards)
            cards = []
            continue

        if line == 'Player 1:':
            players['Player 1'] = []
        elif line == 'Player 2:':
            players['Player 2'] = []
        else:
            cards.append(int(line))

players['Player 2'] = deque(cards)

# Part 1 - card game war

win_p1 = False
win_p2 = False
winning_deck = []

while not win_p1 and not win_p2:
    card_p1 = players['Player 1'].popleft()
    card_p2 = players['Player 2'].popleft()

    if card_p1 > card_p2:
        players['Player 1'].append(card_p1)
        players['Player 1'].append(card_p2)
    else:
        players['Player 2'].append(card_p2)
        players['Player 2'].append(card_p1)

    if not players['Player 1']:
        winning_deck = list(players['Player 2'])
        win_p2 = True
    elif not players['Player 2']:
        winning_deck = list(players['Player 1'])
        win_p1 = True

weight = list(range(len(winning_deck), 0, -1))
score = sum(a * b for a, b in zip(weight, winning_deck))

print('Advent of Code Day 22 Answer Part 1:', score)

# Part 2

players = {}
with open('day22.txt', 'r') as file:
    cards = []
    for line in file:
        line = line.strip()
        if line == '' and 'Player 2' not in players and 'Player 1' in players:
            players['Player 1'] = deque(cards)
            cards = []
            continue

        if line == 'Player 1:':
            players['Player 1'] = []
        elif line == 'Player 2:':
            players['Player 2'] = []
        else:
            cards.append(int(line))

players['Player 2'] = deque(cards)

def game(cards_p1, cards_p2):
    cards_p1 = deepcopy(cards_p1)
    cards_p2 = deepcopy(cards_p2)

    before = tuple()

    win_p1 = False
    win_p2 = False
    winning_deck = []

    while cards_p1 and cards_p2:
        state = (tuple(cards_p1), tuple(cards_p2))
        if state in before:
            winning_deck = list(cards_p1)

            weight = list(range(len(winning_deck), 0, -1))
            score = sum(a * b for a, b in zip(weight, winning_deck))

            win_p1 = True

            return score, cards_p1, cards_p2, win_p1, win_p2

        before += (state, )

        card_p1 = cards_p1.popleft()
        card_p2 = cards_p2.popleft()

        if len(cards_p1) >= card_p1 and len(cards_p2) >= card_p2:
            new_cards_p1 = deque(islice(cards_p1, 0, card_p1))
            new_cards_p2 = deque(islice(cards_p2, 0, card_p2))

            _, _, _, win_p1, win_p2 = game(new_cards_p1, new_cards_p2)

            if win_p1:
                cards_p1.append(card_p1)
                cards_p1.append(card_p2)
            elif win_p2:
                cards_p2.append(card_p2)
                cards_p2.append(card_p1)
        else:
            if card_p1 > card_p2:
                cards_p1.append(card_p1)
                cards_p1.append(card_p2)

            elif card_p2 > card_p1: # assumes no ties
                cards_p2.append(card_p2)
                cards_p2.append(card_p1)

    if not cards_p1:
        winning_deck = list(cards_p2)
        win_p2 = True
    elif not cards_p2:
        winning_deck = list(cards_p1)
        win_p1 = True

    weight = list(range(len(winning_deck), 0, -1))
    score = sum(a * b for a, b in zip(weight, winning_deck))
    return score, cards_p1, cards_p2, win_p1, win_p2

# 20535 is too low, 32305 is too low
print('Advent of Code Day 22 Answer Part 2:', game(players['Player 1'], players['Player 2'])[0])

