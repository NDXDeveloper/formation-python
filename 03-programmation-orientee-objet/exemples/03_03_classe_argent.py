# ============================================================================
#   Section 3.3 : Classe Argent
#   Description : Exemple pratique avec addition, soustraction, multiplication
#                 et vérification de devise
#   Fichier source : 03-methodes-speciales.md
# ============================================================================

class Argent:
    def __init__(self, montant, devise="EUR"):
        self.montant = montant
        self.devise = devise

    def __add__(self, autre):
        if self.devise != autre.devise:
            raise ValueError("Impossible d'additionner des devises différentes")
        return Argent(self.montant + autre.montant, self.devise)

    def __sub__(self, autre):
        if self.devise != autre.devise:
            raise ValueError("Impossible de soustraire des devises différentes")
        return Argent(self.montant - autre.montant, self.devise)

    def __mul__(self, facteur):
        return Argent(self.montant * facteur, self.devise)

    def __str__(self):
        return f"{self.montant:.2f} {self.devise}"

    def __repr__(self):
        return f"Argent({self.montant}, '{self.devise}')"

prix1 = Argent(50.00)
prix2 = Argent(30.50)

total = prix1 + prix2
print(total)  # 80.50 EUR

reduction = total - Argent(10)
print(reduction)  # 70.50 EUR

double = prix1 * 2
print(double)  # 100.00 EUR
