# Créer une classe dé
    # On peut l'instancier en choisissant le nombre de face du dè
    # Penser à l'affichage humain de la classe print()
    # créer une méthode roll() qui jette un dè aléatoire
    
import random
    
class Dice:
    _type = "normal dice"
    
    def __init__(self, faces):
        self._faces = faces
    
    def __str__(self):
        return f"I'm {self._faces} faces {type(self)._type}"
        
    def roll(self):
        return random.randint(1, self._faces)
    
class RiggedDice(Dice):
    _type = "rigged dice"
    
    def roll(self, rigged = False):
        # argument un booléen "rigged" / par défaut False
            # True : jet de dès truqué
            # False : jet de dès normal
        return self._faces

a_dice = Dice(6)
print(a_dice)

a_rigged_dice = RiggedDice(20)
print(a_rigged_dice)
print(a_rigged_dice.roll())