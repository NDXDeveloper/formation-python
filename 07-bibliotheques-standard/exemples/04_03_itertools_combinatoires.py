# ============================================================================
#   Section 7.4 : Les modules itertools et functools
#   Description : Itérateurs combinatoires - product, permutations,
#                 combinations, accumulate, tee, zip_longest
#   Fichier source : 04-itertools-et-functools.md
# ============================================================================

import itertools
import math
import operator

# --- product() ---
print("=== product() - Produit cartésien ===")

couleurs = ['rouge', 'bleu']
tailles = ['S', 'M', 'L']

produit = itertools.product(couleurs, tailles)
for item in produit:
    print(f"  {item}")

# Avec repeat
des = itertools.product(range(1, 7), repeat=2)
print(f"\nCombinaisons 2 dés : {len(list(des))}")

# Grille 3x3
coordonnees = list(itertools.product(range(3), range(3)))
print(f"Grille 3x3 : {coordonnees}")

# --- permutations() ---
print("\n=== permutations() ===")

elements = ['A', 'B', 'C']
perms = list(itertools.permutations(elements))
for p in perms:
    print(f"  {p}")

perms_2 = list(itertools.permutations(elements, 2))
print(f"\nPermutations de 2 parmi 3 : {perms_2}")

n, r = 3, 2
nb_perms = math.factorial(n) // math.factorial(n - r)
print(f"Nombre : {nb_perms}")

# --- combinations() ---
print("\n=== combinations() ===")

elements = ['A', 'B', 'C', 'D']
combos = list(itertools.combinations(elements, 2))
for c in combos:
    print(f"  {c}")

n, r = 4, 2
nb_combos = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
print(f"Nombre de combinaisons : {nb_combos}")

# --- combinations_with_replacement() ---
print("\n=== combinations_with_replacement() ===")

elements = ['A', 'B', 'C']
combos = list(itertools.combinations_with_replacement(elements, 2))
for c in combos:
    print(f"  {c}")

# --- Grilles de loto ---
print("\n=== Grilles de loto ===")

numeros = range(1, 50)
toutes_combinaisons = itertools.combinations(numeros, 5)
grilles = list(itertools.islice(toutes_combinaisons, 5))

for i, grille in enumerate(grilles, 1):
    print(f"  Grille {i}: {sorted(grille)}")

# --- accumulate() ---
print("\n=== accumulate() ===")

nombres = [1, 2, 3, 4, 5]
cumul = list(itertools.accumulate(nombres))
print(f"Somme cumulative : {cumul}")

produit_cumul = list(itertools.accumulate(nombres, operator.mul))
print(f"Produit cumulatif : {produit_cumul}")

nombres2 = [5, 1, 8, 3, 9, 2]
max_cumul = list(itertools.accumulate(nombres2, max))
print(f"Maximum cumulatif : {max_cumul}")

mots = ['Hello', ' ', 'World', '!']
concat = list(itertools.accumulate(mots, lambda a, b: a + b))
print(f"Concaténation : {concat}")

# --- tee() ---
print("\n=== tee() ===")

nombres = [1, 2, 3, 4, 5]
iter1, iter2, iter3 = itertools.tee(nombres, 3)
print(f"iter1 : {list(iter1)}")
print(f"iter2 : {list(iter2)}")
print(f"iter3 : {list(iter3)}")

# --- zip_longest() ---
print("\n=== zip_longest() ===")

liste1 = [1, 2, 3]
liste2 = ['a', 'b']

print(f"zip standard : {list(zip(liste1, liste2))}")
print(f"zip_longest  : {list(itertools.zip_longest(liste1, liste2, fillvalue='X'))}")

# Combiner des listes de longueurs différentes
noms = ['Alice', 'Bob', 'Charlie']
ages = [25, 30]
villes = ['Paris', 'Lyon', 'Marseille', 'Nice']

personnes = itertools.zip_longest(noms, ages, villes, fillvalue='N/A')
for nom, age, ville in personnes:
    print(f"  {nom} - {age} ans - {ville}")
