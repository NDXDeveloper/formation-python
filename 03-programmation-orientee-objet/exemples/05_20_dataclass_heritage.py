# ============================================================================
#   Section 3.5 : Héritage de dataclasses
#   Description : Dataclass Animal héritée par Chien ; piège de l'ordre des
#                 champs et solution kw_only=True (Python 3.10+)
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

# --- ⚠️ Piège : un champ SANS défaut ne peut pas suivre un champ AVEC défaut ---
print()
try:
    @dataclass
    class Base:
        nom: str
        actif: bool = True     # champ AVEC défaut

    @dataclass
    class Derivee(Base):
        priorite: int          # champ SANS défaut après un champ AVEC défaut
except TypeError as e:
    print(f"TypeError : {e}")

# --- ✅ Solution (Python 3.10+) : kw_only=True supprime la contrainte d'ordre ---
@dataclass(kw_only=True)
class BaseKw:
    nom: str
    actif: bool = True

@dataclass(kw_only=True)
class DeriveeKw(BaseKw):
    priorite: int              # OK : tous les champs sont passés par mot-clé

tache = DeriveeKw(nom="tâche", priorite=5)
print(tache)  # DeriveeKw(nom='tâche', actif=True, priorite=5)
