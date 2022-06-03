"""
Zombie Dice Game
Date: 16/may/2022
Version: 1.4
Author: André Hioki

Description: Development in python language of the game zombie dice.
"""
import random
import time
import operator

# Dice's face: B-Brain, F-Footprint, S-Shotgun
dices = {
    "green_qty": 6, "green_faces": "BFBSFB",
    "yellow_qty": 4, "yellow_faces": "SFBSFB",
    "red_qty": 3, "red_faces": "SFSBFS"
    }
dice_qty = dices["green_qty"] + dices["yellow_qty"] + dices["red_qty"]

# ----number of players----
qty_players = "0"
while int(qty_players) < 2:
    qty_players = input("Enter number of players: ")
    try:
        if int(qty_players) < 2:
            print("Error: it must have at least 2 players")
    except ValueError:
        print("Error! Please enter a number")
        qty_players = "0"

qty_players_int = int(qty_players)

# ----Name of players----
name_players = []
print("Enter the name of each player: ")
for counter1 in range(qty_players_int):
    name_players.append(input(f"Player {counter1 + 1}: "))

    # ----players' order----
print("Player order")
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
for counter1 in range(dices["green_qty"]):
    shaker_cup.append("Green")

for counter1 in range(dices["yellow_qty"]):
    shaker_cup.append("Yellow")

for counter1 in range(dices["red_qty"]):
    shaker_cup.append("Red")

# ----Turn of each player----
for counter1 in range(qty_players_int):
    brain = 0
    shotgun = 0
    round_option = 2
    lock = 0
    dice_locked = []
    turn = 1

    print(f"\n------{name_players[counter1]}'s turn------")
    while round_option == 2:
        print(f"\nTurn {turn}")
        print("Thrown dice")
        for counter2 in range(3):
            condition = 0
            while condition == 0:
                chosen_dice_random = random.randint(0, dice_qty - 1)
                if lock != 0:
                    for counter3 in range(lock):
                        if chosen_dice_random != dice_locked[counter3]:
                            condition = 1
                else:
                    condition = 1

            # ----take a die----
            chosen_dice = shaker_cup[chosen_dice_random]

            if chosen_dice == "Green":
                chosen_face = random.choice(dices["green_faces"])
            elif chosen_dice == "Yellow":
                chosen_face = random.choice(dices["yellow_faces"])
            else:
                chosen_face = random.choice(dices["red_faces"])

            # ----roll the die----
            if chosen_face == "B":
                print(f"{counter2 + 1}) {chosen_dice} die: brain face")
                brain += 1
            elif chosen_face == "F":
                print(f"{counter2 + 1}) {chosen_dice} die: footprint face")
            else:
                print(f"{counter2 + 1}) {chosen_dice} die: shotgun face")
                shotgun += 1
                lock += 1
                dice_locked.append(chosen_dice_random)
            time.sleep(1)

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
                    round_option = int(input("Type '1' to NO; or type '2' to YES: "))
                except ValueError:
                    print("\nError! Please enter a number")

        turn += 1

    brain_players[name_players[counter1]] = brain
    if round_option == 3:
        break

print("\n")
print("*" * 30)
print("**********Scoreboard**********")
print("*" * 30)

player_ranked = sorted(brain_players.items(), key=operator.itemgetter(1), reverse=True)
for counter1, v in enumerate(player_ranked):
    print(f"{counter1+1}º - {v[0]}: {v[1]}")