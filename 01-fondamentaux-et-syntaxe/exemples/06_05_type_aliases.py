# ============================================================================
#   Section 6.7 : Type Aliases (Alias de types)
#   Description : Créer des alias pour des types complexes répétés
#   Fichier source : 06-type-hints-et-annotations.md
# ============================================================================

from typing import Any

# Créer des alias
Vector = list[float]
Matrix = list[list[float]]
JSON = dict[str, Any]

# Utiliser les alias
def additionner_vecteurs(v1: Vector, v2: Vector) -> Vector:
    return [a + b for a, b in zip(v1, v2)]

v1: Vector = [1.0, 2.0, 3.0]
v2: Vector = [4.0, 5.0, 6.0]
print(f"{v1} + {v2} = {additionner_vecteurs(v1, v2)}")  # [5.0, 7.0, 9.0]

def traiter_json(data: JSON) -> None:
    for cle, valeur in data.items():
        print(f"  {cle}: {valeur}")

print("JSON :")
traiter_json({"nom": "Alice", "age": 25, "actif": True})

# Alias pour des tuples complexes
Coordonnees = tuple[float, float, float]
Personne = tuple[str, int, str]  # (nom, age, ville)

def calculer_distance(p1: Coordonnees, p2: Coordonnees) -> float:
    """Calcule la distance entre deux points 3D."""
    return sum((a - b) ** 2 for a, b in zip(p1, p2)) ** 0.5

p1: Coordonnees = (0.0, 0.0, 0.0)
p2: Coordonnees = (1.0, 1.0, 1.0)
print(f"Distance {p1} -> {p2} = {calculer_distance(p1, p2):.4f}")  # 1.7321
