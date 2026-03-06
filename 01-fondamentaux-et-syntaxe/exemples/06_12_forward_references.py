# ============================================================================
#   Section 6.18 : Forward references et compatibilité
#   Description : Annotations en string pour forward references,
#                 from __future__ import annotations, commentaires de type
#   Fichier source : 06-type-hints-et-annotations.md
# ============================================================================

from __future__ import annotations

# --- Forward reference avec __future__ annotations ---
class Noeud:
    def __init__(self, valeur: int, suivant: Noeud | None = None):
        self.valeur = valeur
        self.suivant = suivant

    def __repr__(self) -> str:
        if self.suivant is None:
            return f"Noeud({self.valeur})"
        return f"Noeud({self.valeur}) -> {self.suivant}"

# Créer une liste chaînée : 1 -> 2 -> 3
n3 = Noeud(3)
n2 = Noeud(2, n3)
n1 = Noeud(1, n2)
print(f"Liste chaînée : {n1}")

# --- Annotations en commentaires (ancien style Python 3.5) ---
def additionner_ancien(a, b):
    # type: (int, int) -> int
    return a + b

x = 5  # type: int
print(f"additionner_ancien(3, 4) = {additionner_ancien(3, 4)}")
