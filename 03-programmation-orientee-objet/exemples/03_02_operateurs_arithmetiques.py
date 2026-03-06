# ============================================================================
#   Section 3.3 : Opérateurs arithmétiques
#   Description : __add__, __sub__, __mul__, __truediv__ avec Vecteur et Nombre
#   Fichier source : 03-methodes-speciales.md
# ============================================================================

# --- __add__ : opérateur + ---
class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, autre):
        return Vecteur(self.x + autre.x, self.y + autre.y)

    def __str__(self):
        return f"Vecteur({self.x}, {self.y})"

v1 = Vecteur(2, 3)
v2 = Vecteur(1, 4)
v3 = v1 + v2  # Appelle v1.__add__(v2)

print(v3)  # Vecteur(3, 7)

# --- Tous les opérateurs ---
print()

class Nombre:
    def __init__(self, valeur):
        self.valeur = valeur

    def __add__(self, autre):
        return Nombre(self.valeur + autre.valeur)

    def __sub__(self, autre):
        return Nombre(self.valeur - autre.valeur)

    def __mul__(self, autre):
        return Nombre(self.valeur * autre.valeur)

    def __truediv__(self, autre):
        if autre.valeur == 0:
            raise ValueError("Division par zéro impossible")
        return Nombre(self.valeur / autre.valeur)

    def __str__(self):
        return str(self.valeur)

a = Nombre(10)
b = Nombre(3)

print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.3333333333333335
