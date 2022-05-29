"""
Zombie Dice Game
Date: 05/may/2022
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

# Shuffle dices inside the tube
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

print(faces)