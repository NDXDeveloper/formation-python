# ============================================================================
#   Section 3.3 : Classe Fraction
#   Description : Simplification automatique, opérations arithmétiques,
#                 comparaisons, conversion float/int
#   Fichier source : 03-methodes-speciales.md
# ============================================================================

from math import gcd

class Fraction:
    """Représente une fraction avec simplification automatique."""

    def __init__(self, numerateur, denominateur):
        if denominateur == 0:
            raise ValueError("Le dénominateur ne peut pas être zéro")

        # Simplifier la fraction
        pgcd = gcd(abs(numerateur), abs(denominateur))
        self.numerateur = numerateur // pgcd
        self.denominateur = denominateur // pgcd

        # Garder le signe au numérateur
        if self.denominateur < 0:
            self.numerateur = -self.numerateur
            self.denominateur = -self.denominateur

    def __str__(self):
        if self.denominateur == 1:
            return str(self.numerateur)
        return f"{self.numerateur}/{self.denominateur}"

    def __repr__(self):
        return f"Fraction({self.numerateur}, {self.denominateur})"

    def __add__(self, autre):
        num = self.numerateur * autre.denominateur + autre.numerateur * self.denominateur
        den = self.denominateur * autre.denominateur
        return Fraction(num, den)

    def __sub__(self, autre):
        num = self.numerateur * autre.denominateur - autre.numerateur * self.denominateur
        den = self.denominateur * autre.denominateur
        return Fraction(num, den)

    def __mul__(self, autre):
        num = self.numerateur * autre.numerateur
        den = self.denominateur * autre.denominateur
        return Fraction(num, den)

    def __truediv__(self, autre):
        if autre.numerateur == 0:
            raise ValueError("Division par zéro")
        num = self.numerateur * autre.denominateur
        den = self.denominateur * autre.numerateur
        return Fraction(num, den)

    def __eq__(self, autre):
        return (self.numerateur == autre.numerateur and
                self.denominateur == autre.denominateur)

    def __lt__(self, autre):
        return (self.numerateur * autre.denominateur <
                autre.numerateur * self.denominateur)

    def __le__(self, autre):
        return self < autre or self == autre

    def __float__(self):
        return self.numerateur / self.denominateur

    def __int__(self):
        return self.numerateur // self.denominateur

# Utilisation
f1 = Fraction(1, 2)
f2 = Fraction(1, 3)

print(f"f1 = {f1}")                    # 1/2
print(f"f2 = {f2}")                    # 1/3

somme = f1 + f2
print(f"f1 + f2 = {somme}")            # 5/6

difference = f1 - f2
print(f"f1 - f2 = {difference}")       # 1/6

produit = f1 * f2
print(f"f1 * f2 = {produit}")          # 1/6

quotient = f1 / f2
print(f"f1 / f2 = {quotient}")         # 3/2

print(f"f1 < f2 : {f1 < f2}")          # False
print(f"f1 > f2 : {f1 > f2}")          # True

print(f"Valeur décimale de f1 : {float(f1)}")  # 0.5
print(f"Partie entière de f1 : {int(f1)}")     # 0

# Simplification automatique
f3 = Fraction(4, 8)
print(f"4/8 simplifié = {f3}")         # 1/2
