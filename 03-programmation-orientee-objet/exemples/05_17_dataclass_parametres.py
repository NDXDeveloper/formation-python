# ============================================================================
#   Section 3.5 : Paramètres du décorateur @dataclass
#   Description : frozen=True (immutable), order=True (comparaison automatique)
#   Fichier source : 05-metaclasses-et-prog-avancee.md
# ============================================================================

from dataclasses import dataclass

# Classe immuable (comme un tuple nommé, mais plus puissant)
@dataclass(frozen=True)
class Coordonnees:
    latitude: float
    longitude: float

coord = Coordonnees(48.8566, 2.3522)

try:
    coord.latitude = 0  # FrozenInstanceError
except Exception as e:
    print(f"Erreur : {e}")

# Classe ordonnée (génère __lt__, __le__, __gt__, __ge__)
@dataclass(order=True)
class Version:
    majeure: int
    mineure: int
    patch: int = 0

versions = [Version(2, 0), Version(1, 9, 1), Version(1, 9)]
print(sorted(versions))  # [Version(1, 9, 0), Version(1, 9, 1), Version(2, 0, 0)]
