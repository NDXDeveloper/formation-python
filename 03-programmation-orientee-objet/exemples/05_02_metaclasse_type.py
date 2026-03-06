# ============================================================================
#   Section 3.5 : La métaclasse par défaut : type
#   Description : Créer une classe avec la syntaxe classique et avec type()
#   Fichier source : 05-metaclasses-et-prog-avancee.md
# ============================================================================

# 1. Syntaxe classique
class Personne:
    def __init__(self, nom):
        self.nom = nom

# 2. En utilisant type() directement
def init_personne(self, nom):
    self.nom = nom

Personne2 = type('Personne', (), {'__init__': init_personne})

# Les deux créent la même classe !
p1 = Personne("Alice")
print(p1.nom)  # Alice

p2 = Personne2("Bob")
print(p2.nom)  # Bob
