# ============================================================================
#   Section 3.3 : Classe Vecteur complète
#   Description : Exemple combinant __str__, __repr__, __add__, __sub__,
#                 __mul__, __neg__, __eq__, __abs__, __bool__, __getitem__
#   Fichier source : 03-methodes-speciales.md
# ============================================================================

import math

class Vecteur:
    """Représente un vecteur 2D avec des opérations mathématiques."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Vecteur({self.x}, {self.y})"

    def __add__(self, autre):
        return Vecteur(self.x + autre.x, self.y + autre.y)

    def __sub__(self, autre):
        return Vecteur(self.x - autre.x, self.y - autre.y)

    def __mul__(self, scalaire):
        return Vecteur(self.x * scalaire, self.y * scalaire)

    def __truediv__(self, scalaire):
        if scalaire == 0:
            raise ValueError("Division par zéro")
        return Vecteur(self.x / scalaire, self.y / scalaire)

    def __neg__(self):
        return Vecteur(-self.x, -self.y)

    def __eq__(self, autre):
        return self.x == autre.x and self.y == autre.y

    def __ne__(self, autre):
        return not self.__eq__(autre)

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Index invalide (0 ou 1 uniquement)")

    def __setitem__(self, index, valeur):
        if index == 0:
            self.x = valeur
        elif index == 1:
            self.y = valeur
        else:
            raise IndexError("Index invalide (0 ou 1 uniquement)")

# Utilisation complète
v1 = Vecteur(3, 4)
v2 = Vecteur(1, 2)

print(f"v1 = {v1}")              # (3, 4)
print(f"v2 = {v2}")              # (1, 2)

# Opérations
v3 = v1 + v2
print(f"v1 + v2 = {v3}")        # (4, 6)

v4 = v1 - v2
print(f"v1 - v2 = {v4}")        # (2, 2)

v5 = v1 * 2
print(f"v1 * 2 = {v5}")         # (6, 8)

v6 = -v1
print(f"-v1 = {v6}")            # (-3, -4)

# Comparaison
print(f"v1 == v2 : {v1 == v2}") # False
print(f"v1 != v2 : {v1 != v2}") # True

# Longueur
print(f"|v1| = {abs(v1)}")      # 5.0

# Booléen
v_nul = Vecteur(0, 0)
print(f"v1 est vrai : {bool(v1)}")      # True
print(f"v_nul est vrai : {bool(v_nul)}") # False

# Indexation
print(f"v1[0] = {v1[0]}")       # 3
print(f"v1[1] = {v1[1]}")       # 4
v1[0] = 10
print(f"v1 après modification = {v1}")  # (10, 4)
