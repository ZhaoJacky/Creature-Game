# Creator: ZhaoJacky
# Purpose: This file contains the main code for the creature capturing game.

from classes import Monster
from classes import Player
import commands
import create

# Introductory Message of the game.
print("\nWelcome to the wonderful world of Monstertopia!")
print("To begin your journey, please tell me your name.")

player_name = input("Enter Name: ")
player1 = Player(player_name)

print(f"\n{player1.get_name()} is it? Perfect! Now it's time to choose your starter!\n")
print("Please enter the number of the starter you choose.")
print("""1. Solfare
2. Glacierfish
3. Sombrafly\n""")

starter_num = input("Choose your starter: ")

# Takes in the number entered by User and adds correct Starter to Party.
while(starter_num != "1" and starter_num != "2" and starter_num != "3"):
    print("Please enter a valid starter number.")
    starter_num = input("Choose your starter: ")
if(starter_num == "1"):
    starter = create.create_Monster("Solflare", 5, 0)
    player1.add_Monster(starter)
elif(starter_num == "2"):
    starter = create.create_Monster("Glacierfish", 5, 0)
    player1.add_Monster(starter)
else:
    starter = create.create_Monster("Sombrafly", 5, 0)
    player1.add_Monster(starter)

print(f"{player1.get_Monster(0).get_name()} was sucessfully added to Party!")

# Query to ask the Player which action they want to take.
commands.printMainCommands()
command = input("Enter command number: ")

while(command != "QUIT"):
    if(command == "1"):
        print("\nCurrent Party:")
        commands.printParty(player1)
        commands.printAccessCommands()
        commands.accessCommandQuery(player1)
    else:
        print("That's not a command!")
    
    commands.printMainCommands()
    command = input("Enter command number: ")
