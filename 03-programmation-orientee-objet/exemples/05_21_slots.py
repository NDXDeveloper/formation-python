# ============================================================================
#   Section 3.5 : Slots - Optimisation de la mémoire
#   Description : Classe sans slots vs avec __slots__, comparaison mémoire
#   Fichier source : 05-metaclasses-et-prog-avancee.md
# ============================================================================

import sys

# --- Sans slots ---
class PersonneNormale:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

p = PersonneNormale("Alice", 30)
p.ville = "Paris"  # OK, stocké dans __dict__
print(p.__dict__)  # {'nom': 'Alice', 'age': 30, 'ville': 'Paris'}

# --- Avec slots ---
print()

class PersonneAvecSlots:
    __slots__ = ['nom', 'age']

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

p2 = PersonneAvecSlots("Bob", 25)
print(p2.nom, p2.age)  # Bob 25

# On ne peut PAS ajouter d'autres attributs
try:
    p2.ville = "Lyon"  # AttributeError !
except AttributeError as e:
    print(f"Erreur : {e}")

# --- Comparaison mémoire ---
print()

class SansSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class AvecSlots:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

obj1 = SansSlots(1, 2)
obj2 = AvecSlots(1, 2)

print(f"Taille sans slots : {sys.getsizeof(obj1) + sys.getsizeof(obj1.__dict__)} bytes")
print(f"Taille avec slots : {sys.getsizeof(obj2)} bytes")
