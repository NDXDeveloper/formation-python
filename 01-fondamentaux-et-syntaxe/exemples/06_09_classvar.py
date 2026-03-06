# ============================================================================
#   Section 6.12 : Type hints pour les attributs de classe
#   Description : ClassVar pour attributs de classe partagés,
#                 distinction attributs de classe vs attributs d'instance
#   Fichier source : 06-type-hints-et-annotations.md
# ============================================================================

from typing import ClassVar

class Compteur:
    # Attribut de classe (partagé par toutes les instances)
    total: ClassVar[int] = 0

    # Attribut d'instance
    valeur: int

    def __init__(self, valeur: int) -> None:
        self.valeur = valeur
        Compteur.total += 1

    def incrementer(self) -> None:
        self.valeur += 1

c1 = Compteur(10)
c2 = Compteur(20)
print(f"Compteur.total = {Compteur.total}")  # 2
print(f"c1.valeur = {c1.valeur}")  # 10
print(f"c2.valeur = {c2.valeur}")  # 20

c1.incrementer()
print(f"c1.valeur après incrément = {c1.valeur}")  # 11
