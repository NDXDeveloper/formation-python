# ============================================================================
#   Section 5.4 : yield from - Délégation de générateurs
#   Description : Combiner des générateurs, aplatir des listes imbriquées,
#                 parcourir un arbre
#   Fichier source : 04-generateurs.md
# ============================================================================

# --- Combiner des générateurs ---
print("=== Combiner des générateurs ===")

def generateur1():
    yield 1
    yield 2

def generateur2():
    yield 3
    yield 4

# Avec yield from (élégant)
def combine_auto():
    yield from generateur1()
    yield from generateur2()

print(list(combine_auto()))  # [1, 2, 3, 4]

# --- Aplatir des listes imbriquées ---
print("\n=== Aplatir des listes ===")

def aplatir(liste_imbriquee):
    """Aplatit une liste de listes."""
    for element in liste_imbriquee:
        if isinstance(element, list):
            yield from aplatir(element)  # Récursion
        else:
            yield element

donnees = [1, [2, 3, [4, 5]], 6, [7, [8, 9]]]
print(list(aplatir(donnees)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# --- Parcourir un arbre ---
print("\n=== Parcourir un arbre ===")

class Noeud:
    def __init__(self, valeur, enfants=None):
        self.valeur = valeur
        self.enfants = enfants or []

def parcourir_arbre(noeud):
    """Parcourt un arbre en profondeur."""
    yield noeud.valeur
    for enfant in noeud.enfants:
        yield from parcourir_arbre(enfant)

# Création d'un arbre
#       1
#      / \
#     2   3
#    / \
#   4   5

arbre = Noeud(1, [
    Noeud(2, [Noeud(4), Noeud(5)]),
    Noeud(3)
])

print(list(parcourir_arbre(arbre)))  # [1, 2, 4, 5, 3]
