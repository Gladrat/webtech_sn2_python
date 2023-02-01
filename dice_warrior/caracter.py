from dice import Dice, RiggedDice

class Caracter:
    _type = "Caracter"

    def __init__(self, name, max_health, attack, defense, dice):
        self._name = name
        self._max_health = max_health
        self._health = max_health
        self._attack = attack
        self._defense = defense
        self._dice = dice

    def __str__(self):
        return f"I'm a {type(self)._type} named {self._name}"
    
    def is_alive(self):
        return (self._health > 0)
    
    def show_health(self):
        missing_health = self._max_health - self._health
        health_bar = f"{self._name}'s health bar : [{'●' *self._health}{'○'*missing_health}]"
        print(health_bar)
    
    def attack(self):
        result = self._dice.roll()
        damages = self._attack + result
        print(f"{type(self)._type} {self._name} attack with {damages} (attack: {self._attack} + roll: {result})")
    
    def defend(self, wounds):
        damages = wounds
        result = self._dice.roll()
        wounds = wounds - self._defense - result
        print(f"{type(self)._type} {self._name} take {wounds} (damages: {damages} - defense: {self._defense} - roll: {result})")

if __name__ == "__main__":
    a_new_dice = Dice()
    print(a_new_dice)
    
    caracter_1 = Caracter("Tom", 20, 8, 3, a_new_dice)
    caracter_2 = Caracter("Helen", 20, 8, 3, a_new_dice)
    
    caracter_1.attack()
    caracter_1.defend(10)