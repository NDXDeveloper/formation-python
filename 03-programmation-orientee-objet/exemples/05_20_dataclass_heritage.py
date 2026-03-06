# ============================================================================
#   Section 3.5 : Héritage de dataclasses
#   Description : Dataclass Animal héritée par Chien avec champs supplémentaires
#   Fichier source : 05-metaclasses-et-prog-avancee.md
# ============================================================================

from dataclasses import dataclass

@dataclass
class Animal:
    nom: str
    age: int

@dataclass
class Chien(Animal):
    race: str
    dresse: bool = False

rex = Chien("Rex", 5, "Berger Allemand", dresse=True)
print(rex)  # Chien(nom='Rex', age=5, race='Berger Allemand', dresse=True)
