from __future__ import annotations
from dice import Dice, RiggedDice


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
    
    def is_alive(self):
        return (self._health > 0)
    
    def show_health(self):
        missing_health = self._max_health - self._health
        health_bar = f"{self._name}'s health bar : [{'●' *self._health}{'○'*missing_health}] {self._health}/{self._max_health}hp"
        print(health_bar)
    
    def compute_damages(self, result):
        damages = 0
        damages = self._attack + result
        return damages
    
    def attack(self, target: Caracter):
        if (self.is_alive()):    
            result = self._dice.roll()
            damages = self.compute_damages(result)
            print(f"{type(self)._type} {self._name} attack {target.get_name()} with {damages} (attack: {self._attack} + roll: {result})")
            target.defend(damages)
    
    def defend(self, wounds):
        damages = wounds
        result = self._dice.roll()
        wounds = wounds - self._defense - result
        print(f"{type(self)._type} {self._name} take {wounds} (damages: {damages} - defense: {self._defense} - roll: {result})")
        self._health = self._health - wounds
        if (self._health < 0):
            self._health = 0
        self.show_health()

class Warrior(Caracter):
    _type = "Warrior"
    
    def compute_damages(self, result):
        print("Coup de hache ! (+3)")
        return super().compute_damages(result) + 3

    
class Mage(Caracter):
    _type = "Mage"
    
    # Armure magique absorbe 3 de dégats supplémentaires
    # + message d'affichage

if __name__ == "__main__":
    a_new_dice = Dice()
    print(a_new_dice)
    
    player_1 = Warrior("Tom", 20, 8, 3, a_new_dice)
    player_2 = Mage("Helen", 20, 8, 3, a_new_dice)
    
    while (player_1.is_alive() and player_2.is_alive()):
        player_1.attack(player_2)
        player_2.attack(player_1)