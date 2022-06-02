"""
Zombie Dice Game
Date: 09/may/2022
Author: André Hioki

Description: Development in python language of the game zombie dice.
"""
import random

# Dice's face: B-Brain, F-Footprint, S-Shotgun
dices = {
    "green_qty": 6, "green_faces": "BFBSFB",
    "yellow_qty": 4, "yellow_faces": "SFBSFB",
    "red_qty": 3, "red_faces": "SFSBFS"
    }

# ----number of players----
qty_players = "0"
while int(qty_players) < 2:
    qty_players = input("Enter number of players:")
    try:
        if int(qty_players) < 2:
            print("Error: it must have at least 2 players")
    except ValueError:
        print("Error! Please enter a number")
        qty_players = "0"

qty_players_int = int(qty_players)

# ----Name of players----
name_players = []
print("Enter the name of each player:")
for counter1 in range(qty_players_int):
    name_players.append(input("Player " + str(counter1 + 1) + ": "))

# ----dice in the shaker cup----
shaker_cup = ""
for i in range(dices["green_qty"]):
    shaker_cup += "G"

for i in range(dices["yellow_qty"]):
    shaker_cup += "Y"

for i in range(dices["red_qty"]):
    shaker_cup += "R"

qty_players = input("Enter number of players:")
if int(qty_players) < 2:
    print("Error: it must have at least 2 players")
    qty_players = input("Enter number of players:")

# Shuffle dices inside the shaker cup
dice_sequence = random.choice(shaker_cup)

faces = ""
brain = 0
footprint = 0
shotgun = 0

if dice_sequence == "G":
    faces += random.choice(dices["green_faces"])
    brain += 1
elif dice_sequence == "Y":
    faces += random.choice(dices["yellow_faces"])
    footprint += 1
else:
    faces += random.choice(dices["red_faces"])
    shotgun += 1

# ----Turn of each player----
dice_qty = dices["green_qty"] + dices["yellow_qty"] + dices["red_qty"]
for counter1 in range(qty_players_int):
    brain = 0
    shotgun = 0
    round_option = 2
    lock = 0
    dice_locked = []
    turn = 1

    # ----Take a die----
    chosen_dice = random.choice(shaker_cup)

    print("\nPlayer " + name_players[counter1] + "'s turn")

    # ********insert round_option

    if chosen_dice == "G":
        chosen_face = random.choice(dices["green_faces"])
    elif chosen_dice == "Y":
        chosen_face = random.choice(dices["yellow_faces"])
    else:
        chosen_face = random.choice(dices["red_faces"])

    print("Chosen dices")
    if chosen_face == "B":
        print(chosen_dice + " dice: brain")
        brain += 1
    elif chosen_face == "F":
        print(chosen_dice + " dice: footprint")
    else:
        print(chosen_dice + " dice: shotgun")
        shotgun += 1
        lock += 1
