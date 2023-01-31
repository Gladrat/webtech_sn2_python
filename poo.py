# classe : Voiture
# attributs
# attributs de classes : nb_roues, constructeur
# attributs d'objets : Vitesse max, couleur, nb portes
# méthodes : demarrer, accelerer, freiner, klaxonner

# objet

class Voiture:
    _constructeur = "Renault SARL"
    _nb_roues = 4
    _nb_voiture = 0

    # constructeur
    def __init__(self, vitesse_bridage):
        Voiture._nb_voiture = Voiture._nb_voiture + 1
        print("Création de la voiture n°" + str(Voiture._nb_voiture))
        self._vitesse_max = 250
        self._couleur = "rouge"
        self.bridage(vitesse_bridage)

    def __str__(self):
        # f-string
        return f"Je suis une voiture de couleur {self._couleur} roulant à {self._vitesse_max}km/h"

    def get_vitesse_max(self):
        return self._vitesse_max

    def set_vitesse_max(self, vitesse_max):
        # self._vitesse_max = vitesse_max
        self.bridage(vitesse_max)

    def bridage(self, vitesse_bridage):
        if (vitesse_bridage <= self._vitesse_max):
            self._vitesse_max = vitesse_bridage

    def demarrer(self):
        print("Démarrage de la voiture")
        print("Je peux rouler à " + str(self._vitesse_max))

    def klaxonner(self):
        print("Tut tut")

    # arreter()

ta_voiture = Voiture(300)
ma_voiture = Voiture(225)

print(ta_voiture)
print(ma_voiture)

ta_voiture.bridage(180)

# Interdit : accès direct aux attributs !
# print(ta_voiture._vitesse_max)
# ta_voiture._vitesse_max = 500

# On utilise les accesseurs & mutateurs
print(ta_voiture.get_vitesse_max())
ta_voiture.set_vitesse_max(500)

# ta_voiture.demarrer()
# ma_voiture.demarrer()