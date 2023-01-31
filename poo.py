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
        self._vitesse_max = 250
        self._vitesse = 0
        self._est_demarree = False
        self._couleur = "rouge"
        self.bridage(vitesse_bridage)
        Voiture._nb_voiture = Voiture._nb_voiture + 1
        print("Création de la voiture n°" + str(Voiture._nb_voiture))

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
        if (not self._est_demarree):
            print("Démarrage de la voiture")
            print("Je peux rouler à " + str(self._vitesse_max))
            self._est_demarree = True
            
    def arreter(self):
        if (self._est_demarree and self._vitesse == 0):
            print("Arrêt de la voiture")
            self._est_demarree = False

    def klaxonner(self):
        print("Tut tut")

ta_voiture = Voiture(300)
ma_voiture = Voiture(225)

print(ta_voiture)
print(ma_voiture)

ta_voiture.bridage(180)

ta_voiture.demarrer()
ta_voiture.arreter()
ma_voiture.demarrer()
ma_voiture.arreter()