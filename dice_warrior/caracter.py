from dice import Dice, RiggedDice

class Caracter:
    _type = "Caracter"

    def __init__(self, name, max_health, damage, defense, dice):
        self._name = name
        self._max_health = max_health
        self._health = max_health
        self._damage = damage
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
        # calculer les damages infligés à une cible
        # rajouter un jet de dès
        # afficher le calcul complet
        pass
    
    def defense(self, wounds):
        # soustrayant la defense
        # soustrayant le résultat d'un jet de dès
        pass

if __name__ == "__main__":
    a_new_dice = Dice()
    print(a_new_dice)
    
    a_caracter = Caracter("Tom", 20, 8, 3, a_new_dice)
    a_caracter._health = 6
    a_caracter.show_health()
    
    a_second_caracter = Caracter("Helen", 20, 8, 3, a_new_dice)