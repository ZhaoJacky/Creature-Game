# Creator: ZhaoJacky
# Purpose: This file contains the functions that control the commands of the
# player.

from classes import Monster
from classes import Player

# Prints the main screen commands.
def printMainCommands():
    print("""
-------------------------------------------------------------------------------
Please choose what you would like to do:
    
    1. Access Party
      
Enter QUIT to exit the game.
-------------------------------------------------------------------------------
""")
    
# Prints the monster names in the Player's current party.
def printParty(player: Player):
    for x in range(player.get_partySize()):
        print(f"{x + 1}. {player.get_Monster(x).get_name()}\n")





# Below Contains the Access Party Commands.



# Prints the commands after the user chooses "Access Party"
def printAccessCommands():
    print("""
-------------------------------------------------------------------------------
Please choose what you want to do:

    1. View Stats
          
Enter EXIT to return to Main Commands
-------------------------------------------------------------------------------
""")

# Asks the User for the access command they wish to perform.
def accessCommandQuery(player: Player):
    command = input("Enter command number: ")
    while(command != "EXIT"):
        if(command == "1"):
            printStats(player)

        printAccessCommands()
        command = input("Enter command number: ")


# Wrapper function for printing the stats of a Monster.
def printStats(player: Player):
    try:
        monster_num = int(input("Please enter Monster Number: "))
    except ValueError:
        print("Not a valid number.")
    
    if(monster_num <= player.get_partySize()):
        monster = player.get_Monster(monster_num - 1)
        stats(monster)
    else:
        print("You have no monster in that slot!")


# Prints the stats of a Monster.
def stats(monster: Monster):
    print(f"""\nName: {monster.get_name()}
Level: {monster.get_level()}
Type: {monster.get_type1()} + {monster.get_type2()}
HP: {monster.get_HP()} / {monster.get_maxHP()}
Attack: {monster.get_attack()}
Defense: {monster.get_defense()}
Special Attack: {monster.get_spAttack()}
Special Defense: {monster.get_spDefense()}
EXP: {monster.get_exp()} / {monster.get_maxEXP()}
""")