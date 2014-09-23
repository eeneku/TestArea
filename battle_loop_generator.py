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

player_units = [ROCK, PAPER, LIZARD, SPOCK, LIZARD]
enemy_units = [4, 2, 0, 1, 4, 3, 1, 2]

# Press A for AWESOME!
player_permutations = itertools.permutations(player_units, len(player_units))
enemy_permutations = itertools.permutations(enemy_units, len(enemy_units))

player_combos = []
enemy_combos = []

for e in player_permutations:
    player_combos.append(e)

for e in enemy_permutations:
    enemy_combos.append(e)

player_wins = {}


for en in enemy_combos:
    for pl in player_combos:
        player = list(pl)
        enemy = list(en)
        while len(enemy) > 0 and len(player) > 0:
            if unit_rules[player[0]][enemy[0]] == 1:
                enemy.pop(0)
                player.append(player.pop(0))
            elif unit_rules[player[0]][enemy[0]] == 0:
                enemy.pop(0)
                player.pop(0)
            elif unit_rules[player[0]][enemy[0]] == -1:
                player.pop(0)
                enemy.append(enemy.pop(0))

        if len(player) > 1:
            player_wins.setdefault(en, set()).add(pl)

print (player_wins)