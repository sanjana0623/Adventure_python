#!/usr/bin/env python
# coding: utf-8

# # Text based adventure application using python

# In[1]:


# Text-based adventure game

class Player:
    def __init__(self):
        self.inventory = []

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def check_inventory(self):
        if not self.inventory:
            print("Your inventory is empty.")
        else:
            print("Inventory:")
            for item in self.inventory:
                print("-", item)
        print()

def start_game():
    player = Player()
    print("Welcome to the Adventure Game!")
    print("You wake up in a mysterious forest...")
    print("You need to find your way out. Choose wisely!\n")
    forest(player)

def forest(player):
    print("You are in the forest.")
    print("What do you want to do?")
    print("1. Go left")
    print("2. Go right")
    print("3. Go straight")
    print("4. Check inventory")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("You encounter a river.")
        river(player)
    elif choice == "2":
        print("You find a hidden path.")
        hidden_path(player)
    elif choice == "3":
        print("You stumble upon a cave.")
        cave(player)
    elif choice == "4":
        player.check_inventory()
        forest(player)
    else:
        print("Invalid choice. Try again.")
        forest(player)

def river(player):
    print("The river is swift. What do you do?")
    print("1. Try to swim across")
    print("2. Look for a bridge")
    print("3. Check inventory")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("You attempt to swim across and get swept away by the current. Game over!")
    elif choice == "2":
        print("You find a sturdy bridge and cross it.")
        player.add_to_inventory("Map")
        final_path(player)
    elif choice == "3":
        player.check_inventory()
        river(player)
    else:
        print("Invalid choice. Try again.")
        river(player)

def hidden_path(player):
    print("You discover a path covered in foliage.")
    print("What will you do?")
    print("1. Follow the path")
    print("2. Turn back")
    print("3. Check inventory")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("You follow the path and reach a clearing.")
        player.add_to_inventory("Key")
        final_path(player)
    elif choice == "2":
        print("You decide to turn back.")
        forest(player)
    elif choice == "3":
        player.check_inventory()
        hidden_path(player)
    else:
        print("Invalid choice. Try again.")
        hidden_path(player)

def cave(player):
    print("The cave looks dark and ominous.")
    print("What's your move?")
    print("1. Enter the cave")
    print("2. Find another way")
    print("3. Check inventory")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("You enter the cave and encounter a bear. Game over!")
    elif choice == "2":
        print("You find a different route.")
        player.add_to_inventory("Lantern")
        final_path(player)
    elif choice == "3":
        player.check_inventory()
        cave(player)
    else:
        print("Invalid choice. Try again.")
        cave(player)

def final_path(player):
    print("You reach the final path.")
    print("You see sunlight ahead.")
    print("Congratulations! You made it out of the forest.")

    # Different endings based on inventory items
    if "Map" in player.inventory and "Key" in player.inventory:
        print("With the map and key, you unlock a hidden passage leading to a treasure chest. You win!")
    elif "Map" in player.inventory:
        print("You found the map. You survived, but there's more to explore...")
    else:
        print("You made it out, but there's a sense of something left behind...")
    play_again()

def play_again():
    print("\nDo you want to play again?")
    print("1. Yes")
    print("2. No")

    choice = input("Enter your choice: ")

    if choice == "1":
        start_game()
    elif choice == "2":
        print("Thank you for playing!")
    else:
        print("Invalid choice. Please enter 1 or 2.")
        play_again()

# Start the game
start_game()


# In[ ]:




