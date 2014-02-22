# -*- coding: utf-8 -*-
__author__ = 'eeneku'

import itertools

ROCK = 0
PAPER = 1
SCISSORS = 2
SPOCK = 3
LIZARD = 4

unit_rules = [[0, -1, 1, -1, 1],
              [1, 0, -1, 1, -1],
              [-1, 1, 0, -1, 1],
              [1, -1, 1, 0, -1],
              [-1, 1, -1, 1, 0]]

player = [ROCK, PAPER, SCISSORS]
enemy = [ROCK, PAPER, SCISSORS, PAPER, SCISSORS, SCISSORS]

# Press A for AWESOME!
result = itertools.permutations(player, len(player))
usable = []

for e in result:
    usable.append(e)

print(usable)