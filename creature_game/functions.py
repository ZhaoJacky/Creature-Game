from monsters import Monster
from monsters import Player

# Calculates the max HP of a monster.
def calculateHP(curr_hp, level):
    new_hp = ((4 * curr_hp * level) / 200) + 50
    return new_hp

# Calculates the EXP needed for the monster to level up.
def calculateEXP(level):
    exp = (3 * level * level * level) / 5
    return exp

# Prints the stats of the Monster.
def printStats(monster: Monster):
    print(f"""Name: {monster.get_name()}
Level: {monster.get_level()}
Type: {monster.get_type1()} + {monster.get_type2()}
HP: {monster.get_HP()} / {monster.get_maxHP()}
Attack: {monster.get_attack()}
Defense: {monster.get_defense()}
Special Attack: {monster.get_spAttack()}
Special Defense: {monster.get_spDefense()}
EXP: {monster.get_exp()} / {monster.get_maxEXP()}
""")
    
# Prints the monster names in the Player's current party.
def printParty(player: Player):
    for x in range(player.get_partySize()):
        print(f"{x + 1}. {player.get_Monster(x).get_name()}\n")

# Prints the main screen commands.
def printMainCommands():
    print("""
-------------------------------------------------------------------------------
Please choose what you would like to do:
    
    1. Access Party
      
Enter QUIT to exit the game.
-------------------------------------------------------------------------------
""")

# Prints the commands after the user chooses "Access Party"
def printAccessCommand():
    print("""
-------------------------------------------------------------------------------
Please choose what you want to do:

    1. View Stats
    2. View Moveset

Enter EXIT to return to Main Commands
-------------------------------------------------------------------------------
""")