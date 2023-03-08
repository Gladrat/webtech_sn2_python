import json
from caracter import Farmer, Warrior, Mage, Thief
from dice import Dice
import random


def game():
    warrior = Warrior("Tom", 24, 1, 8, Dice(6))
    mage = Mage("Helen", 24, 8, 1, Dice(6))
    thief = Thief("Doug", 20, 6, 5, Dice(6))
    farmer = Farmer("Bernardo", 24, 6, 6, Dice(6))

    cars = [warrior, mage, thief, farmer]

    stats = {
        warrior.get_name(): 0,
        mage.get_name(): 0,
        thief.get_name(): 0,
        farmer.get_name(): 0,
    }

    car1 = random.choice(cars)
    index = cars.index(car1)
    cars.pop(index)
    
    car2 = random.choice(cars)
    index = cars.index(car2)
    cars.pop(index)

    for i in range(0, 100):
        car1.regenerate()
        car2.regenerate()
        while (car1.is_alive() and car2.is_alive()):
            car1.attack(car2)
            car2.attack(car1)
        if (car1.is_alive()):
            stats[car1.get_name()] += 1
        else:
            stats[car2.get_name()] += 1

    print(json.dumps(stats, indent=4))


if __name__ == "__main__":
    game()
