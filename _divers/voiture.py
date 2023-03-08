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
    _couleur_liste = ["rouge", "vert", "bleu"]

    # constructeur
    def __init__(self, vitesse_bridage, couleur = "rouge"):
        self._vitesse_max = 250
        self._vitesse = 0
        self._est_demarree = False
        self._couleur = ""
        self.changer_couleur(couleur, Voiture._couleur_liste)
        self.bridage(vitesse_bridage)
        Voiture._nb_voiture = Voiture._nb_voiture + 1
        print("Création de la voiture n°" + str(Voiture._nb_voiture))

    def changer_couleur(self, couleur, liste_couleur):
        if (couleur in liste_couleur):
            self._couleur = couleur
        else:
            print(f"Couleur non autorisée :  {couleur}")

    def __str__(self):
        # f-string
        return f"Je suis une voiture de couleur {self._couleur} roulant à {self._vitesse_max}km/h"

    def get_vitesse_max(self):
        return self._vitesse_max

    def set_vitesse_max(self, vitesse_max):
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

    def afficher_vitesse(self):
        print(f"Vitesse actuelle : {self._vitesse}km/h")

    def rouler(self, vitesse_cible):
        if (not self._est_demarree):
            return False
        if (vitesse_cible > self._vitesse_max):
            vitesse_cible = self._vitesse_max
        for i in range(self._vitesse, vitesse_cible + 1):
            self._vitesse = i
            self.afficher_vitesse()

    def klaxonner(self):
        print("Tut tut")


ta_voiture = Voiture(300, "rouge")
ma_voiture = Voiture(225, "vert")

# print(ta_voiture)
# print(ma_voiture)

# ta_voiture.bridage(180)

# ta_voiture.demarrer()
# ta_voiture.arreter()

# ma_voiture.demarrer()

# # ma_voiture.rouler(50)
# # ma_voiture.rouler(300)

# ma_voiture.arreter()
