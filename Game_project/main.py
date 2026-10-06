import pandas as pd
import numpy as np
import classes as cls
import defs
import time

print("Loading data...")
time.sleep(1)
print("Data loaded successfully.")
print("Welcome to the game!")
time.sleep(2)


while True:
    try:
        game = input("Do you want to start a new game? (write 'new', or 'q' to quit): ")

        if game.lower() == "new":
            health, inventory = defs.start_new_game()
            time.sleep(0.5)
            print("New game started.")
            break
        elif game.lower() == "q":
            print("Quitting the game.")
            exit()
        else:
            raise ValueError("Invalid input for game start.")
    except Exception as e:
            print(f"An error occurred: {e}")
name = input("What is your name? ")
print(f"Your health: {health}")
defs.check_health(health)
defs.check_inventory(inventory)
time.sleep(0.5)
print("You can add items to your inventory as you progress in the game.")
time.sleep(0.5)
print("Good luck on your adventure!")
time.sleep(2)
room = cls.place("Dark Room", "You have awaked in a dark room. You can see barely see anything. There is small line of light beneath, it might be the door. What do you want to do?" ["walk around", "walk to the door"])
decision1 = input()
while decision1 not in room.actions:
    print("Invalid action. Please choose a valid option.")
    if decision1 == "walk around":
        time.sleep(0.5)
        print("You walk around the room and find something small and shiny on the floor.")
        inventory.append("small key")
        print("You have added 'small key' to your inventory.")
    elif decision1 == "walk to the door":
        print("You walk to the door and see that it is locked. You can try to unlock it with a key or break it down.")
        action = input("What do you want to do? (unlock/break): ")
        if action == "unlock":
            if "small key" in inventory:
                print("You use the small key to unlock the door.")
                inventory.remove("small key")
                print("The door is now unlocked. You can proceed to the next room.")
            else:
                print("You don't have a key to unlock the door.")
        elif action == "break":
            print("You try to break down the door, but it's too strong. You need a tool or a key to open it.")
            cls.damage.taken("banging the door", "You hurt your shoulder while trying to break the door.", 1)
            defs.check_health(health)
            continue

