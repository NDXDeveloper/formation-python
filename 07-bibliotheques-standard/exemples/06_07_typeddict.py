# ============================================================================
#   Section 7.6 : Le module typing - Annotations avancées
#   Description : TypedDict (dictionnaires structurés) - clés requises,
#                 total=False (clés facultatives), NotRequired (3.11+)
#   Fichier source : 06-typing-annotations-avancees.md
# ============================================================================

import sys
from typing import TypedDict

# ==========================================
# 1. TypedDict de base - clés et types fixes
# ==========================================
print("=== TypedDict de base ===")

class Film(TypedDict):
    titre: str
    annee: int
    note: float

# À l'exécution, c'est un dictionnaire ordinaire ; ce sont les outils
# (mypy, IDE) qui vérifient les clés présentes et le type de chaque valeur.
inception: Film = {"titre": "Inception", "annee": 2010, "note": 8.8}
matrix: Film = {"titre": "Matrix", "annee": 1999, "note": 8.7}

def resumer(film: Film) -> str:
    return f"{film['titre']} ({film['annee']}) - {film['note']}/10"

print(f"  {resumer(inception)}")
print(f"  {resumer(matrix)}")

# C'est bien un dict : les opérations habituelles fonctionnent
print(f"  Clés de 'inception' : {list(inception.keys())}")
print(f"  Type réel : {type(inception).__name__}")

# ==========================================
# 2. total=False - toutes les clés facultatives
# ==========================================
print("\n=== total=False (clés facultatives) ===")

class Preferences(TypedDict, total=False):
    couleur: str
    taille: int

p1: Preferences = {"couleur": "rouge"}
p2: Preferences = {"couleur": "bleu", "taille": 42}
p3: Preferences = {}

for i, p in enumerate((p1, p2, p3), start=1):
    print(f"  p{i} = {p}")

# ==========================================
# 3. NotRequired - granularité par clé (Python 3.11+)
# ==========================================
print("\n=== NotRequired (granularité par clé, 3.11+) ===")

if sys.version_info >= (3, 11):
    from typing import NotRequired

    class Utilisateur(TypedDict):
        nom: str                     # requis
        email: str                   # requis
        telephone: NotRequired[str]  # facultatif

    u1: Utilisateur = {"nom": "Alice", "email": "alice@example.com"}
    u2: Utilisateur = {"nom": "Bob", "email": "bob@example.com",
                       "telephone": "06 00 00 00 00"}
    print(f"  u1 = {u1}")
    print(f"  u2 = {u2}")
else:
    print("  NotRequired : nécessite Python 3.11+")
