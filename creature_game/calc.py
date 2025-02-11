# Creator: ZhaoJacky
# Purpose: This file contains the functions to do the calculations in the
# game, such as EXP and health.


# Calculates the max HP of a monster.
def calculateHP(curr_hp, level):
    new_hp = ((4 * curr_hp * level) / 200) + 50
    return new_hp

# Calculates the EXP needed for the monster to level up.
def calculateEXP(level):
    exp = (3 * level * level * level) / 5
    return exp