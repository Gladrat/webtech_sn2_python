from __future__ import annotations
from dice import Dice, RiggedDice
from rich import print

class Caracter:
    _type = "Caracter"

    def __init__(self, name, max_health, attack, defense, dice):
        self._name = name
        self._max_health = max_health
        self._health = max_health
        self._attack = attack
        self._defense = defense
        self._dice: Dice = dice

    def __str__(self):
        return f"I'm a {type(self)._type} named {self._name}"
    
    def get_name(self):
        return self._name
    
    def get_defense(self):
        return self._defense
    
    def is_alive(self):
        return (self._health > 0)
    
    def show_health(self):
        missing_health = self._max_health - self._health
        health_bar = f"{self._name}'s health bar : [{'●' *self._health}{'○'*missing_health}] {self._health}/{self._max_health}hp"
        print(health_bar)
    
    def compute_damages(self, result, target):
        damages = 0
        damages = self._attack + result
        return damages
    
    def attack(self, target: Caracter):
        if (self.is_alive()):
            result = self._dice.roll()
            damages = self.compute_damages(result, target)
            print(f"{type(self)._type} [b][red]{self._name}[/red][/b] attack {target.get_name()} with {damages} (attack: {self._attack} + roll: {result})")
            target.defend(damages, self)
    
    def compute_defense(self, wounds, result, attacker):
        wounds = wounds - self._defense - result
        return wounds
    
    def defend(self, wounds, attacker: Caracter):
        damages = wounds
        result = self._dice.roll()
        wounds = self.compute_defense(wounds, result, attacker)
        print(f"{type(self)._type} [b][blue]{self._name}[/blue][/b] take {wounds} from {attacker.get_name()} (damages: {damages} - defense: {self._defense} - roll: {result})")
        self._health = self._health - wounds
        if (self._health < 0):
            self._health = 0
        self.show_health()

class Warrior(Caracter):
    _type = "Warrior"
    
    def compute_damages(self, result, target):
        print("Coup de hache ! (+3)")
        return super().compute_damages(result, target) + 3

class Mage(Caracter):
    _type = "Mage"
    
    def compute_defense(self, wounds, result, attacker):
        print("Armure magique ! (-3)")
        return super().compute_defense(wounds, result, attacker) - 3

class Thief(Caracter):
    _type = "Thief"
    
    def compute_damages(self, result, target: Caracter):
        print(f"Coup vicieux ! +{target.get_defense()}")
        return super().compute_damages(result, target) + target.get_defense()

class Farmer(Caracter):
    _type = "Farmer"

if __name__ == "__main__":
    
    warrior = Warrior("Tom", 24, 1, 8, Dice(6))
    mage = Mage("Helen", 24, 8, 1, Dice(6))
    thief = Thief("Doug", 20, 6, 5, Dice(6))
    farmer = Farmer("Bernardo", 24, 6, 6, Dice(6))    
    
    # while (player_1.is_alive() and player_2.is_alive()):
    #     player_1.attack(player_2)
    #     player_2.attack(player_1)