# ============================================================================
#   Section 5.2 : La fonction reduce() - Bases et exemples pratiques
#   Description : Somme avec boucle vs reduce(), produit, maximum,
#                 concaténer, occurrences, aplatir, factorielle
#   Fichier source : 02-map-filter-reduce.md
# ============================================================================

from functools import reduce

# --- Exemple de base : somme de nombres ---
print("=== Somme de nombres ===")

# Approche classique avec une boucle
nombres = [1, 2, 3, 4, 5]
somme = 0

for nombre in nombres:
    somme = somme + nombre

print(somme)  # 15

# Avec reduce()
nombres = [1, 2, 3, 4, 5]

somme = reduce(lambda acc, x: acc + x, nombres)

print(somme)  # 15

# --- Produit de nombres ---
print("\n=== Produit ===")

nombres = [2, 3, 4, 5]

produit = reduce(lambda acc, x: acc * x, nombres)

print(f"Produit : {produit}")  # 2 * 3 * 4 * 5 = 120

# --- Trouver le maximum ---
print("\n=== Maximum ===")

nombres = [45, 12, 89, 34, 67, 23]

maximum = reduce(lambda acc, x: acc if acc > x else x, nombres)

print(f"Maximum : {maximum}")  # 89

# --- Concaténer des chaînes ---
print("\n=== Concaténer ===")

mots = ["Python", "est", "génial"]

phrase = reduce(lambda acc, mot: acc + " " + mot, mots)

print(phrase)  # Python est génial

# Avec une valeur initiale
mots = ["Python", "est", "génial"]

phrase = reduce(lambda acc, mot: acc + " " + mot, mots, "Langage:")

print(phrase)  # Langage: Python est génial

# --- Compter les occurrences ---
print("\n=== Occurrences ===")

fruits = ["pomme", "banane", "pomme", "orange", "banane", "pomme"]

compteur = reduce(
    lambda acc, fruit: {**acc, fruit: acc.get(fruit, 0) + 1},
    fruits,
    {}
)

print(compteur)  # {'pomme': 3, 'banane': 2, 'orange': 1}

# --- Aplatir une liste de listes ---
print("\n=== Aplatir ===")

listes = [[1, 2], [3, 4], [5, 6], [7, 8]]

liste_aplatie = reduce(lambda acc, liste: acc + liste, listes)

print(liste_aplatie)  # [1, 2, 3, 4, 5, 6, 7, 8]

# --- Calculer une factorielle ---
print("\n=== Factorielle ===")

def factorielle(n):
    """Calcule la factorielle de n."""
    if n == 0 or n == 1:
        return 1
    return reduce(lambda acc, x: acc * x, range(1, n + 1))

print(f"5! = {factorielle(5)}")  # 5! = 120
print(f"7! = {factorielle(7)}")  # 7! = 5040
