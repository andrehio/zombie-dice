"""
Zombie Dice Game
Date: 26/may/2022
Version: 1.6
Author: André Hioki

Description: Development in python language of the game zombie dice.
"""
import random
import time
import operator
import collections

# Dice's face: B-Brain, F-Footprint, S-Shotgun
dice_type = collections.namedtuple("dice_type", ["green", "yellow", "red"])
dice_qty = dice_type(green=6, yellow=4, red=3)
dice_faces = dice_type(green="BFBSFB", yellow="SFBSFB", red="SFSBFS")

# ----number of players----
qty_players = 0
while qty_players < 2:
    try:
        qty_players = int(input("Enter number of players: "))
        if qty_players < 2:
            print("Error: it must have at least 2 players")
    except ValueError:
        print("Error! Please enter a number")
        qty_players = 0

# ----Name of players----
name_players = []
print("\nEnter the name of each player: ")
for counter1 in range(qty_players):
    name_players.append(input(f"Player {counter1 + 1}: "))

    # ----players' order----
print("\nPlayer order")
player_order = "0"
while int(player_order) == 0:
    player_order = input("Type '1' to keep the players order; or type '2' to shuffle the players order: ")
    try:
        if int(player_order) > 2:
            print("Error: Type 1 or 2")
            player_order = "0"
    except ValueError:
        print("Error! Please enter a number")
        player_order = "0"

if player_order == "2":
    random.shuffle(name_players)

# ----Dict Brains----
brain_players = {}
for counter1 in range(len(name_players)):
    brain_players[name_players[counter1]] = None

# ----dice in the shaker cup----
shaker_cup = []
for counter1 in range(dice_qty.green):
    shaker_cup.append("Green")

for counter1 in range(dice_qty.yellow):
    shaker_cup.append("Yellow")

for counter1 in range(dice_qty.red):
    shaker_cup.append("Red")

shaker_cup_original = list(shaker_cup)

# ----Turn of each player----
for counter1 in range(qty_players):
    brain = 0
    shotgun = 0
    round_option = 0
    lock = 0
    turn = 1
    dice_locked = []

    print(f"\n------{name_players[counter1]}'s turn------")
    while round_option < 2:
        print(f"\nTurn {turn}")
        print("Thrown dice")

        for counter2 in range(3):
            if round_option == 1 and len(dice_locked) > 0 and counter2 <= len(dice_locked):  # ----Check if there were footprint face in the last turn----
                chosen_dice = dice_locked[counter2]
                chosen_dice_random = -1
                if counter2 == len(dice_locked)-1:
                    dice_locked = []
            else:  # ----take a die----
                chosen_dice_random = random.randint(0, len(shaker_cup) - 1)
                chosen_dice = shaker_cup[chosen_dice_random]

            if chosen_dice == "Green":
                chosen_face = random.choice(dice_faces.green)
            elif chosen_dice == "Yellow":
                chosen_face = random.choice(dice_faces.yellow)
            else:
                chosen_face = random.choice(dice_faces.red)

            # ----roll the die----
            if chosen_face == "B":
                print(f"{counter2 + 1}) {chosen_dice} die: brain face")
                brain += 1
            elif chosen_face == "F":
                print(f"{counter2 + 1}) {chosen_dice} die: footprint face")
                dice_locked.append(chosen_dice)
            else:
                print(f"{counter2 + 1}) {chosen_dice} die: shotgun face")
                shotgun += 1
                lock += 1

            if chosen_dice_random != -1:
                shaker_cup.pop(chosen_dice_random)
            time.sleep(1)
            print(f"Shaker Cup: {shaker_cup}")  #teste

        # ----check victory/failure condition and option to continue the turn----
        if shotgun >= 3:
            round_option = 1
            brain = 1
            print(f"------Player {name_players[counter1]} lost!------")
        elif brain >= 13 and shotgun < 3:
            round_option = 3
            print(f"------Player {name_players[counter1]} won!------")
        else:
            round_option = 0
            while not (round_option == 1 or round_option == 2):
                try:
                    print(f"\nCurrent numbers: Brain: {brain} / Shotgun: {shotgun}")
                    print("Do you like to stay in your turn and roll new dice?")
                    round_option = int(input("Type '1' to YES; or type '2' to NO: "))
                except ValueError:
                    print("\nError! Please enter a number")

        turn += 1

    brain_players[name_players[counter1]] = brain
    if round_option == 3:
        break
    shaker_cup = shaker_cup_original.copy()

print("\n")
print("*" * 30)
print("**********Scoreboard**********")
print("*" * 30)

player_ranked = sorted(brain_players.items(), key=operator.itemgetter(1), reverse=True)
for counter1, v in enumerate(player_ranked):
    print(f"{counter1 + 1}º - {v[0]}: {v[1]}")