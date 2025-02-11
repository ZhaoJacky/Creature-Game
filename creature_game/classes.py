# Creator: ZhaoJacky
# Purpose: This file contains all the class definitions for the monster
# game.

# Class for a Monster.
class Monster:
    # Constructor for the Monster class.
    def __init__(self, name, type1, type2, max_hp, hp,
                 attack, defense, sp_attack, sp_defense, level, max_exp,
                 exp):
        # Stats
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.max_hp = max_hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.level = level
        self.max_exp = max_exp
        self.exp = exp

        # Moveset
        self.moveset = []

    # Gets data from the monster.
    def get_name(self):
        return self.name
    
    def get_type1(self):
        return self.type1
    
    def get_type2(self):
        return self.type2
    
    def get_maxHP(self):
        return self.max_hp

    def get_HP(self):
        return self.hp
    
    def get_attack(self):
        return self.attack
    
    def get_defense(self):
        return self.defense

    def get_spAttack(self):
        return self.sp_attack
    
    def get_spDefense(self):
        return self.sp_defense

    def get_level(self):
        return self.level
    
    def get_maxEXP(self):
        return self.max_exp
    
    def get_exp(self):
        return self.exp


# Class for the player.
class Player:
    # Constructor for the Player class.
    def __init__(self, name):
        self.name = name
        self.monsters = []

    # Adds a monster to the player party.
    def add_Monster(self, monster):
        if isinstance(monster, Monster):
            self.monsters.append(monster)
        else:
            raise TypeError("Cannot add non-Monster.")
    
    # Grabs the player name.
    def get_name(self):
        return self.name
    
    # Grabs the Monster object at the specified index.
    def get_Monster(self, index):
        return self.monsters[index]
    
    def get_partySize(self):
        return len(self.monsters)
    
