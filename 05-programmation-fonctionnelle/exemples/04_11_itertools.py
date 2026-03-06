# ============================================================================
#   Section 5.4 : Le module itertools
#   Description : count(), cycle(), repeat(), chain(), islice(),
#                 takewhile(), dropwhile()
#   Fichier source : 04-generateurs.md
# ============================================================================

import itertools

# --- count() ---
print("=== count() ===")

compteur = itertools.count(10, 2)  # Commence à 10, incrémente de 2
for i in range(5):
    print(next(compteur), end=" ")  # 10 12 14 16 18
print()

# --- cycle() ---
print("\n=== cycle() ===")

couleurs = itertools.cycle(['R', 'G', 'B'])
for i in range(7):
    print(next(couleurs), end=" ")  # R G B R G B R
print()

# --- repeat() ---
print("\n=== repeat() ===")

for x in itertools.repeat("Python", 3):
    print(x, end=" ")  # Python Python Python
print()

# --- chain() ---
print("\n=== chain() ===")

liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
for x in itertools.chain(liste1, liste2):
    print(x, end=" ")  # 1 2 3 4 5 6
print()

# --- islice() ---
print("\n=== islice() ===")

nombres = range(100)
for x in itertools.islice(nombres, 5, 10):  # Éléments 5 à 9
    print(x, end=" ")  # 5 6 7 8 9
print()

# --- takewhile() ---
print("\n=== takewhile() ===")

nombres = [1, 4, 6, 4, 1]
for x in itertools.takewhile(lambda x: x < 5, nombres):
    print(x, end=" ")  # 1 4
print()

# --- dropwhile() ---
print("\n=== dropwhile() ===")

nombres = [1, 4, 6, 4, 1]
for x in itertools.dropwhile(lambda x: x < 5, nombres):
    print(x, end=" ")  # 6 4 1
print()
