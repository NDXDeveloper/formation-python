# ============================================================================
#   Section 3.5 : Dataclasses - Classe classique vs dataclass
#   Description : Comparaison entre classe classique verbeuse et @dataclass
#                 concise, avec __repr__ et __eq__ générés automatiquement
#   Fichier source : 05-metaclasses-et-prog-avancee.md
# ============================================================================

# Classe classique : beaucoup de code répétitif
class PointClassique:
    def __init__(self, x: float, y: float, label: str = ""):
        self.x = x
        self.y = y
        self.label = label

    def __repr__(self):
        return f"PointClassique(x={self.x}, y={self.y}, label='{self.label}')"

    def __eq__(self, other):
        if not isinstance(other, PointClassique):
            return NotImplemented
        return self.x == other.x and self.y == other.y and self.label == other.label


# Dataclass : même résultat en quelques lignes
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
    label: str = ""

p = Point(1.0, 2.0, "A")
print(p)        # Point(x=1.0, y=2.0, label='A')
print(p == Point(1.0, 2.0, "A"))  # True
