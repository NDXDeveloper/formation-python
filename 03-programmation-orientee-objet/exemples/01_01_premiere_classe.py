# ============================================================================
#   Section 3.1 : Première classe simple
#   Description : Créer une classe, instancier un objet, constructeur __init__,
#                 self, attributs d'instance
#   Fichier source : 01-classes-et-objets.md
# ============================================================================

# --- Classe vide ---
class Chien:
    pass

mon_chien = Chien()
print(mon_chien)  # <__main__.Chien object at 0x...>

# --- Constructeur __init__ ---
class Chien:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

mon_chien = Chien("Rex", 5)
print(mon_chien.nom)  # Rex
print(mon_chien.age)  # 5

# --- Attributs d'instance ---
print()

class Chien:
    def __init__(self, nom, age, race):
        self.nom = nom
        self.age = age
        self.race = race

chien1 = Chien("Rex", 5, "Berger Allemand")
chien2 = Chien("Bella", 3, "Labrador")

print(chien1.nom)   # Rex
print(chien2.nom)   # Bella
print(chien1.race)  # Berger Allemand
print(chien2.race)  # Labrador
