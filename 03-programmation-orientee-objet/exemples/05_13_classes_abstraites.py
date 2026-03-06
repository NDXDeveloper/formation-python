# ============================================================================
#   Section 3.5 : Classes abstraites et ABC
#   Description : Forme abstraite avec Rectangle et Cercle, méthode concrète
#                 afficher() héritée
#   Fichier source : 05-metaclasses-et-prog-avancee.md
# ============================================================================

from abc import ABC, abstractmethod

class Forme(ABC):
    """Classe abstraite pour les formes géométriques"""

    @abstractmethod
    def calculer_surface(self):
        """Méthode abstraite : doit être implémentée par les classes filles"""
        pass

    @abstractmethod
    def calculer_perimetre(self):
        """Méthode abstraite"""
        pass

    def afficher(self):
        """Méthode concrète : peut être utilisée telle quelle"""
        print(f"Forme : {self.__class__.__name__}")
        print(f"Surface : {self.calculer_surface()}")
        print(f"Périmètre : {self.calculer_perimetre()}")

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def calculer_surface(self):
        return self.largeur * self.hauteur

    def calculer_perimetre(self):
        return 2 * (self.largeur + self.hauteur)

class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def calculer_surface(self):
        return 3.14159 * self.rayon ** 2

    def calculer_perimetre(self):
        return 2 * 3.14159 * self.rayon

# Utilisation
rect = Rectangle(5, 3)
rect.afficher()

print()

cercle = Cercle(4)
cercle.afficher()

# Ceci échouerait :
try:
    forme = Forme()  # TypeError: Can't instantiate abstract class
except TypeError as e:
    print(f"\nErreur : {e}")
