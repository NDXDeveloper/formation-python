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

# --- ⚠️ Piège : définir __eq__ rend les instances NON hashables ---
print()
try:
    ensemble = {alice, bob}   # impossible : Personne n'a plus de __hash__
except TypeError as e:
    print(f"TypeError : {e}")

# --- ✅ Pour rester hashable, définir __hash__ sur les MÊMES attributs que __eq__ ---
class PersonneHashable:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def __eq__(self, autre):
        return self.age == autre.age

    def __hash__(self):
        return hash(self.age)   # cohérent avec __eq__ (qui compare l'âge)

p1 = PersonneHashable("Alice", 30)
p2 = PersonneHashable("Bob", 25)
print(len({p1, p2}))   # 2 — utilisable dans un set
