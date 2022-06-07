"""
Zombie Dice Game
Date: 06/06/2022
Version: 1.7
Author: André Hioki

Description: Development in python language of the game zombie dice.
"""
import random
import time
import operator
import collections


# ----number of players----
def fnumber_players():
    qty_player = 0
    while qty_player < 2:
        try:
            qty_player = int(input("Enter number of players: "))
            if qty_player < 2:
                print("Error: it must have at least 2 players")
        except ValueError:
            print("Error! Please enter a number")
            qty_player = 0
    return qty_player


# ----Name of players----
def fname_players():
    name_player = []
    print("\nEnter the name of each player: ")
    for i in range(qty_players):
        name_player.append(input(f"Player {i + 1}: "))
    return name_player


    # ----players' order----
def forder_players():
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


# ----Die's face----
def dice_face(dice):
    if dice == "Green":
        face = random.choice(dice_faces.green)
        color = "\033[32m"
    elif dice == "Yellow":
        face = random.choice(dice_faces.yellow)
        color = "\033[33m"
    else:
        face = random.choice(dice_faces.red)
        color = "\033[31m"
    color += dice + " die\033[m"
    return face, color


# ----dice in the shaker cup----
def organize_shake_cup():
    cup = []
    for i in range(dice_qty.green):
        cup.append("Green")
    for i in range(dice_qty.yellow):
        cup.append("Yellow")
    for i in range(dice_qty.red):
        cup.append("Red")
    return cup


def current_numbers(brains, footprints, shotguns):
    print(f"\nCurrent numbers: \033[30;42mBrain: {brains}\033[m | "
          f"\033[30;43mFootprint: {footprints}\033[m | "
          f"\033[30;41mShotgun: {shotguns}\033[m")


# ----Quantidade de dados----
# Dice's face: B-Brain, F-Footprint, S-Shotgun
dice_type = collections.namedtuple("dice_type", ["green", "yellow", "red"])
dice_qty = dice_type(green=6, yellow=4, red=3)
dice_faces = dice_type(green="BFBSFB", yellow="SFBSFB", red="SFSBFS")

qty_players = fnumber_players()
name_players = fname_players()
forder_players()

# ----Dict Brains----
brain_players = {}
for counter1 in range(len(name_players)):
    brain_players[name_players[counter1]] = 0

shaker_cup = organize_shake_cup()

# ----Turn of each player----
for counter1 in range(qty_players):
    brain = 0
    shotgun = 0
    round_option = 0
    turn = 1
    dice_locked = []

    print(f"\n\033[1;30;46m------{name_players[counter1]}'s turn------\033[m")
    while round_option < 2:
        print(f"\n\033[4;36mTurn {turn}\033[m")
        print("Thrown dice")

        for counter2 in range(3):
            # ----Check if there was footprint face in the last turn----
            if round_option == 1 and len(dice_locked) > 0 and counter2 < len(dice_locked):
                chosen_dice = dice_locked[counter2]
                index_dice_random = -1
                if counter2 == len(dice_locked) - 1:
                    dice_locked = []
            else:  # ----take a die----
                index_dice_random = random.randint(0, len(shaker_cup) - 1)
                chosen_dice = shaker_cup[index_dice_random]

            chosen_face, dice_color = dice_face(chosen_dice)

            # ----roll the die----
            if chosen_face == "B":
                print(f"{counter2 + 1}) {dice_color}: brain face")
                brain += 1
            elif chosen_face == "F":
                print(f"{counter2 + 1}) {dice_color}: footprint face")
                dice_locked.append(chosen_dice)
            else:
                print(f"{counter2 + 1}) {dice_color}: shotgun face")
                shotgun += 1

            if index_dice_random != -1:
                shaker_cup.pop(index_dice_random)
            time.sleep(1)
            print(f"Shaker Cup: {shaker_cup} | nº dados: {len(shaker_cup)}")  # teste

        # ----check victory/failure condition and option to continue the turn----
        if shotgun >= 3:
            round_option = 2
            brain = 1
            current_numbers(brain, len(dice_locked), shotgun)
            print(f"\n\033[30;41m------Player {name_players[counter1]} lost!------\033[m")
            time.sleep(2)
        elif brain >= 13 and shotgun < 3:
            round_option = 3
            print(f"\033[30;42m------Player {name_players[counter1]} won!------\033[m")
        else:
            round_option = 0
            while not (round_option == 1 or round_option == 2):
                try:
                    current_numbers(brain, len(dice_locked), shotgun)
                    print("Do you like to stay in your turn and roll new dice?")
                    round_option = int(input("Type '1' to YES; or type '2' to NO: "))
                except ValueError:
                    print("\nError! Please enter a number")

        turn += 1

    brain_players[name_players[counter1]] = brain
    if round_option == 3:
        break
    shaker_cup = organize_shake_cup()

print("\n")
print("\033[1m*\033[m" * 30)
print("\033[1m**********Scoreboard**********\033[m")
print("\033[1m*\033[m" * 30)

player_ranked = sorted(brain_players.items(), key=operator.itemgetter(1), reverse=True)
for counter1, v in enumerate(player_ranked):
    print(f"{counter1 + 1}º - {v[0]}: {v[1]}")