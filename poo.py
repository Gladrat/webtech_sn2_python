# classe : Voiture
# attributs
# attributs de classes : nb_roues, constructeur
# attributs d'objets : Vitesse max, couleur, nb portes
# méthodes : demarrer, accelerer, freiner, klaxonner

# objet

def ma_fonction(prenom):
    print(f"Bonjour {prenom}")
    return True


class Voiture:
    constructeur = "Renault SARL"
    nb_roues = 4

    nb_voiture = 0

    # vitesse_max = 250

    # constructeur
    def __init__(self, vitesse_bridage):
        # Debug
        # self.nb_voiture = self.nb_voiture + 1
        # print("Création de la voiture n°" + str(self.nb_voiture))
        self.vitesse_max = 250
        self.couleur = "rouge"
        if (vitesse_bridage <= self.vitesse_max):
            self.vitesse_max = vitesse_bridage

    def __str__(self):
        # f-string
        return f"Je suis une voiture de couleur {self.couleur} roulant à {self.vitesse_max}km/h"

    def demarrer(self):
        print("Démarrage de la voiture")
        print("Je peux rouler à " + str(self.vitesse_max))

    def klaxonner(self):
        print("Tut tut")


ta_voiture = Voiture(300)
ma_voiture = Voiture(225)

# ta_voiture.vitesse_max = 200

# ta_voiture.demarrer()
# ma_voiture.demarrer()

print(ta_voiture)
print(ma_voiture)
