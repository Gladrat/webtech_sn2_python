# Exercice 24 : Tuning

A partir du code vu en cours :

## Phase 1

**Attributs**

- Créer un attribut ``vitesse`` (initialisé à ``0``)
  - C'est la vitesse courante du véhicule
- Créer un attribut ``est_demarree`` (initialisé à `False`)

**Méthodes**

- Créer les méthodes `demarrer()` et `arreter()`
- Une voiture démarre uniquement si elle n'est pas déjà démarrée
- Une voiture s'arrête si elle est démarrée et que sa vitesse est à 0

## Phase 2

- Créer la méthode `rouler(vitesse)` qui prend en paramètre une ``vitesse`` cible
- Une voiture ne peut rouler que si elle est démarrée
- ``rouler(vitesse)`` incrémente la vitesse de la voiture depuis sa ``vitesse actuelle`` jusqu'à la ``vitesse cible``, sans jamais dépasser la ``vitesse maximale``

## Phase 3

- Permettre de choisir la couleur de la voiture à sa construction