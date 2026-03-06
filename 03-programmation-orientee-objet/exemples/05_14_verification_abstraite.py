# ============================================================================
#   Section 3.5 : Vérification de l'implémentation abstraite
#   Description : Animal abstrait avec faire_bruit et se_deplacer,
#                 propriété abstraite Vehicule/Voiture
#   Fichier source : 05-metaclasses-et-prog-avancee.md
# ============================================================================

from abc import ABC, abstractmethod

# --- Vérifier l'implémentation ---
class Animal(ABC):
    @abstractmethod
    def faire_bruit(self):
        pass

    @abstractmethod
    def se_deplacer(self):
        pass

# Ceci fonctionne (toutes les méthodes implémentées)
class Chien(Animal):
    def faire_bruit(self):
        return "Wouf"

    def se_deplacer(self):
        return "Je cours"

rex = Chien()
print(rex.faire_bruit())      # Wouf
print(rex.se_deplacer())      # Je cours

# Ceci échoue (se_deplacer manquant)
try:
    ChienIncomplet = type('ChienIncomplet', (Animal,), {
        'faire_bruit': lambda self: "Wouf"
    })
    chien = ChienIncomplet()
except TypeError as e:
    print(f"Erreur : {e}")

# --- Propriétés abstraites ---
print()

class Vehicule(ABC):
    @property
    @abstractmethod
    def vitesse_max(self):
        """Propriété abstraite"""
        pass

class Voiture(Vehicule):
    def __init__(self):
        self._vitesse_max = 200

    @property
    def vitesse_max(self):
        return self._vitesse_max

voiture = Voiture()
print(f"Vitesse max : {voiture.vitesse_max} km/h")  # 200 km/h
