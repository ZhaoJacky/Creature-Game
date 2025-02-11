# Creator: ZhaoJacky
# Purpose: This file contains the data for the monsters and the functions
# that create monster objects.

import kagglehub
import pandas as pd
import calc

from classes import Monster
from classes import Player

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

# Function that creates a monster by initializing a Monster object.
def create_Monster(name, level, exp):
    index = data[nameSeries == name].index[0]
    monster = Monster(name, type1Series.iloc[index], 
                    type2Series.iloc[index], 
                    calc.calculateHP(hpSeries.iloc[index], level),
                    calc.calculateHP(hpSeries.iloc[index], level),
                    attackSeries.iloc[index],
                    defenseSeries.iloc[index],
                    spAttackSeries.iloc[index],
                    spDefenseSeries.iloc[index], level,
                    calc.calculateEXP(level), exp)
    return monster