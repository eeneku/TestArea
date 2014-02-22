# -*- coding: utf-8 -*-
__author__ = 'eeneku'

ROCK = 0
PAPER = 1
SCISSORS = 2

battle_loop_one = [PAPER, SCISSORS, ROCK, PAPER]
battle_loop_two = [SCISSORS, ROCK, SCISSORS, ROCK]

# rock beats scissors, scissors beat paper, paper beats rock

turn = 0

print("Start\n")
print(battle_loop_one)
print(battle_loop_two)

while len(battle_loop_one) > 0 and len(battle_loop_two) > 0 and turn < 10:
    if battle_loop_one[0] == ROCK:
        if battle_loop_two[0] == SCISSORS:
            print("Turn " + str(turn) + ": ROCK > SCISSORS")
            battle_loop_two.pop(0)
            battle_loop_one.append(battle_loop_one.pop(0))

        elif battle_loop_two[0] == PAPER:
            print("Turn " + str(turn) + ": ROCK < PAPER")
            battle_loop_one.pop(0)
            battle_loop_two.append(battle_loop_two.pop(0))

        elif battle_loop_two[0] == ROCK:
            print("Turn " + str(turn) + ": ROCK | ROCK")
            battle_loop_one.append(battle_loop_one.pop(0))
            battle_loop_two.append(battle_loop_two.pop(0))

    elif battle_loop_one[0] == PAPER:
        if battle_loop_two[0] == ROCK:
            print("Turn " + str(turn) + ": PAPER > ROCK")
            battle_loop_two.pop(0)
            battle_loop_one.append(battle_loop_one.pop(0))

        elif battle_loop_two[0] == SCISSORS:
            print("Turn " + str(turn) + ": PAPER < SCISSORS")
            battle_loop_one.pop(0)
            battle_loop_two.append(battle_loop_two.pop(0))

        elif battle_loop_two[0] == PAPER:
            print("Turn " + str(turn) + ": PAPER | PAPER")
            battle_loop_one.append(battle_loop_one.pop(0))
            battle_loop_two.append(battle_loop_two.pop(0))

    elif battle_loop_one[0] == SCISSORS:
        if battle_loop_two[0] == PAPER:
            print("Turn " + str(turn) + ": SCISSORS > PAPER")
            battle_loop_two.pop(0)
            battle_loop_one.append(battle_loop_one.pop(0))

        elif battle_loop_two[0] == ROCK:
            print("Turn " + str(turn) + ": SCISSORS < ROCK")
            battle_loop_one.pop(0)
            battle_loop_two.append(battle_loop_two.pop(0))

        elif battle_loop_two[0] == SCISSORS:
            print("Turn " + str(turn) + ": SCISSORS | SCISSORS")
            battle_loop_one.append(battle_loop_one.pop(0))
            battle_loop_two.append(battle_loop_two.pop(0))

    print(battle_loop_one)
    print(battle_loop_two)
    turn += 1

print("\nEnd")