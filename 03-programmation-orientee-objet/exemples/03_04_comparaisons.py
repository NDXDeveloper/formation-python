# ============================================================================
#   Section 3.3 : Méthodes de comparaison
#   Description : __eq__, __lt__, __le__, __gt__, __ge__, __ne__,
#                 tri avec sorted()
#   Fichier source : 03-methodes-speciales.md
# ============================================================================

class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def __eq__(self, autre):
        return self.age == autre.age

    def __lt__(self, autre):
        return self.age < autre.age

    def __le__(self, autre):
        return self.age <= autre.age

    def __gt__(self, autre):
        return self.age > autre.age

    def __ge__(self, autre):
        return self.age >= autre.age

    def __ne__(self, autre):
        return self.age != autre.age

    def __str__(self):
        return f"{self.nom} ({self.age} ans)"

alice = Personne("Alice", 30)
bob = Personne("Bob", 25)
charlie = Personne("Charlie", 30)

print(alice == charlie)  # True (même âge)
print(alice == bob)      # False
print(bob < alice)       # True (25 < 30)
print(alice >= charlie)  # True (30 >= 30)

# Trier une liste de personnes
personnes = [alice, bob, charlie]
personnes_triees = sorted(personnes)  # Trie par âge grâce à __lt__
for p in personnes_triees:
    print(p)
