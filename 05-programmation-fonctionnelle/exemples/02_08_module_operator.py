# ============================================================================
#   Section 5.2 : Le module operator
#   Description : operator.add/mul (alternative aux lambdas), itemgetter et
#                 attrgetter, math.prod (produit natif, Python 3.8+)
#   Fichier source : 02-map-filter-reduce.md
# ============================================================================

import operator
import math
from functools import reduce
from operator import itemgetter, attrgetter
from collections import namedtuple

# --- operator.add / operator.mul au lieu de lambda ---
print("=== operator avec reduce ===")
print(reduce(operator.add, [1, 2, 3, 4, 5]))   # 15
print(reduce(operator.mul, [2, 3, 4, 5]))       # 120

# --- itemgetter : clé de tri et extraction de "colonne" ---
print("\n=== itemgetter ===")
personnes = [
    {"nom": "Alice", "age": 30},
    {"nom": "Bob", "age": 25},
    {"nom": "Charlie", "age": 35},
]
par_age = sorted(personnes, key=itemgetter("age"))
print([p["nom"] for p in par_age])               # ['Bob', 'Alice', 'Charlie']
print(list(map(itemgetter("age"), personnes)))   # [30, 25, 35]

# --- attrgetter : pour les attributs d'objets ---
print("\n=== attrgetter ===")
Personne = namedtuple("Personne", ["nom", "age"])
gens = [Personne("Alice", 30), Personne("Bob", 25)]
print([p.nom for p in sorted(gens, key=attrgetter("age"))])   # ['Bob', 'Alice']

# --- math.prod : produit natif (Python 3.8+) ---
print("\n=== math.prod ===")
print(math.prod([2, 3, 4, 5]))   # 120
print(math.prod([]))             # 1 (élément neutre du produit)
