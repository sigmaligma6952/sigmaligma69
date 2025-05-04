import random
import time
import os
import math
class Character:
    def __init__ (self, health, maxhealth, attack):
        self.health = health
        self.maxhealth = maxhealth
        self.attack = attack
class Attacker:
    def __init__ (self, maxhealth, attack):
        self.health = maxhealth
        self.maxhealth = maxhealth
        self.attack = attack
        
char = Character(health=100, maxhealth=100, attack=10)
att1 = Attacker(maxhealth=random.randint(10, 150), attack=random.randint(5, 20))
turns = math.ceil(att1.maxhealth / 20 + att1.attack)
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("every time u play, u have (math.ceil(health of an attacker / 20 + damage of an attacker)) turns to win!!! (chosse attack or defend wisely)")
    print("ur health =", char.health)
    print("ur damage =", char.attack)
    print("Attacker Health =", att1.health)
    print("Attacker Damage =", att1.attack)
    print("turns left:", turns)
    if att1.health > 0 and char.health > 0 and turns > 0:
        dora = input("defend or attack? (type d or a) ")
        turns -= 1
        if dora == "a":
            att1.health -= char.attack
            char.health -= att1.attack
        elif dora == "d":
            att1.health -= char.attack / 2
            char.health -= char.attack / 4
        else:
            print("ok we automatically chose attack")
            att1.health -= char.attack
            char.health -= att1.attack
    elif att1.health <= 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        yorn = input("u won!! want to play again? (type y or n) ")
        if yorn == "y":
            char = Character(health=100, maxhealth=100, attack=10)
            att1 = Attacker(maxhealth=random.randint(10, 150), attack=random.randint(1, 20))
            turns = math.ceil(att1.maxhealth / 20 + att1.attack)
        elif yorn == "n":
            break
        else:
            print("ok we automatically chose to play")
            char = Character(health=100, maxhealth=100, attack=10)
            att1 = Attacker(maxhealth=random.randint(10, 150), attack=random.randint(1, 20))
            turns = math.ceil(att1.maxhealth / 20 + att1.attack)
    elif char.health <= 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        yorn = input("u lost.. (0 hp) want to play again? (type y or n) ")
        if yorn == "y":
            char = Character(health=100, maxhealth=100, attack=10)
            att1 = Attacker(maxhealth=random.randint(10, 150), attack=random.randint(1, 20))
            turns = math.ceil(att1.maxhealth / 20 + att1.attack)
        elif yorn == "n":
            break
        else:
            print("ok we automatically chose to play")
            char = Character(health=100, maxhealth=100, attack=10)
            att1 = Attacker(maxhealth=random.randint(10, 150), attack=random.randint(1, 20))
            turns = math.ceil(att1.maxhealth / 20 + att1.attack)
    elif turns <= 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        yorn = input("u lost.. (0 turns) want to play again? (type y or n) ")
        if yorn == "y":
            char = Character(health=100, maxhealth=100, attack=10)
            att1 = Attacker(maxhealth=random.randint(10, 150), attack=random.randint(1, 20))
            turns = math.ceil(att1.maxhealth / 20 + att1.attack)
        elif yorn == "n":
            break
        else:
            print("ok we automatically chose to play")
            char = Character(health=100, maxhealth=100, attack=10)
            att1 = Attacker(maxhealth=random.randint(10, 150), attack=random.randint(1, 20))
            turns = math.ceil(att1.maxhealth / 20 + att1.attack)
        