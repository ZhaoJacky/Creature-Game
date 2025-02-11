from monsters import Monster
from monsters import Player
import kagglehub
import pandas as pd
import functions

# Imports the Creature Dataset.
path = kagglehub.dataset_download("jaczz19/test-dataset")
dpath = path + "/Creatures Dataset - Sheet1.csv"
data = pd.read_csv(dpath)

# Panda series that contains all the Monster data.
nameSeries = data["name"]
type1Series = data["type1"]
type2Series = data["type2"]
hpSeries = data["hp"]
attackSeries = data["attack"]
defenseSeries = data["defense"]
spAttackSeries = data["sp_attack"]
spDefenseSeries = data["sp_defense"]

# Introductory Message of the game.
print("\nWelcome to the wonderful world of powerful creatures!")
print("To begin your journey, please tell me your name.")

player_name = input("Enter Name: ")
player1 = Player(player_name)

# Code that handles choosing a starter monster.
print(f"\n{player1.get_name()} is it? Perfect! Now it's time to choose your starter!\n")
print("Please enter the number of the starter you choose.")
print("""1. Solfare
2. Glacierfish
3. Sombrafly\n""")

starter_num = input("Choose your starter: ")

while(starter_num != "1" and starter_num != "2" and starter_num != "3"):
    print("Please enter a valid starter number.")
    starter_num = input("Choose your starter: ")
if(starter_num == "1"):
    # Grabs the index where the monster is found. Used to access other data.
    index = data[nameSeries == "Solflare"].index[0]
    starter = Monster("Solfare", 
                      type1Series.iloc[index], 
                      type2Series.iloc[index], 
                      functions.calculateHP(hpSeries.iloc[index], 5),
                      functions.calculateHP(hpSeries.iloc[index], 5),
                      attackSeries.iloc[index],
                      defenseSeries.iloc[index],
                      spAttackSeries.iloc[index],
                      spDefenseSeries.iloc[index], 5,
                      functions.calculateEXP(5), 0, 
                      ["Blaze", "Slap", "Empty", "Empty"])
    player1.add_Monster(starter)
elif(starter_num == "2"):
    index = data[nameSeries == "Glacierfish"].index[0]
    starter = Monster("Glacierfish", 
                      type1Series.iloc[index], 
                      type2Series.iloc[index], 
                      functions.calculateHP(hpSeries.iloc[index], 5),
                      functions.calculateHP(hpSeries.iloc[index], 5),
                      attackSeries.iloc[index],
                      defenseSeries.iloc[index],
                      spAttackSeries.iloc[index],
                      spDefenseSeries.iloc[index], 5,
                      functions.calculateEXP(5), 0,
                      ["Sneeze", "Slap", "Empty", "Empty"])
    player1.add_Monster(starter)
else:
    index = data[nameSeries == "Sombrafly"].index[0]
    starter = Monster("Sombrafly", 
                      type1Series.iloc[index], 
                      type2Series.iloc[index], 
                      functions.calculateHP(hpSeries.iloc[index], 5),
                      functions.calculateHP(hpSeries.iloc[index], 5),
                      attackSeries.iloc[index],
                      defenseSeries.iloc[index],
                      spAttackSeries.iloc[index],
                      spDefenseSeries.iloc[index], 5,
                      functions.calculateEXP(5), 0,
                      ["Haunt", "Slap", "Empty", "Empty"])
    player1.add_Monster(starter)

print(f"{player1.get_Monster(0).get_name()} was sucessfully added to Party!")

# Query to ask the Player which action they want to take.
functions.printMainCommands()
command = input("Enter command number: ")

while(command != "QUIT"):
    if(command == "1"):
        print("\nCurrent Party:")
        functions.printParty(player1)
    else:
        print("That's not a command!")
    
    functions.printMainCommands()
    command = input("Enter command number: ")