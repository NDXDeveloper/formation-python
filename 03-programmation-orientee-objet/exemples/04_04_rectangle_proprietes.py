# ============================================================================
#   Section 3.4 : Rectangle avec propriétés
#   Description : Validation largeur/hauteur, surface et périmètre calculés
#   Fichier source : 04-proprietes-et-decorateurs.md
# ============================================================================

class Rectangle:
    def __init__(self, largeur, hauteur):
        self._largeur = largeur
        self._hauteur = hauteur

    @property
    def largeur(self):
        return self._largeur

    @largeur.setter
    def largeur(self, valeur):
        if valeur <= 0:
            raise ValueError("La largeur doit être positive")
        self._largeur = valeur

    @property
    def hauteur(self):
        return self._hauteur

    @hauteur.setter
    def hauteur(self, valeur):
        if valeur <= 0:
            raise ValueError("La hauteur doit être positive")
        self._hauteur = valeur

    @property
    def surface(self):
        return self._largeur * self._hauteur

    @property
    def perimetre(self):
        return 2 * (self._largeur + self._hauteur)

    def __str__(self):
        return f"Rectangle({self._largeur}x{self._hauteur})"

# Utilisation
rect = Rectangle(5, 3)
print(rect)                    # Rectangle(5x3)
print(f"Surface : {rect.surface}")      # Surface : 15
print(f"Périmètre : {rect.perimetre}")  # Périmètre : 16

# Modifier les dimensions
rect.largeur = 10
rect.hauteur = 4
print(rect)                    # Rectangle(10x4)
print(f"Surface : {rect.surface}")      # Surface : 40 (recalculée)

try:
    rect.largeur = -5  # ValueError !
except ValueError as e:
    print(f"Erreur : {e}")
