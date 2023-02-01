from dice import Dice, RiggedDice

class Caracter:
    _type = "Caracter"

    def __init__(self, name, health, max_health, damage, defense):
        self._name = name
        self._health = health
        self._max_health = max_health
        self._damage = damage
        self._defense = defense


if __name__ == "__main__":
    a_new_dice = Dice()
    print(a_new_dice)