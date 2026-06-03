# ============================================================================
#   Section 2.1 : Les Listes - Opérations courantes
#   Description : len, in, count, index, sort, sorted, reverse, tri par clé (key)
#   Fichier source : 01-listes-tuples-dicts-sets.md
# ============================================================================

nombres = [3, 1, 4, 1, 5, 9, 2, 6]

# Longueur de la liste
print(len(nombres))  # 8

# Vérifier si un élément est dans la liste
print(4 in nombres)   # True
print(10 in nombres)  # False

# Compter les occurrences d'un élément
print(nombres.count(1))  # 2

# Trouver l'index d'un élément
print(nombres.index(5))  # 4

# Trier la liste (modifie la liste originale)
nombres.sort()
print(nombres)  # [1, 1, 2, 3, 4, 5, 6, 9]

# Trier en ordre décroissant
nombres.sort(reverse=True)
print(nombres)  # [9, 6, 5, 4, 3, 2, 1, 1]

# Créer une copie triée sans modifier l'original
nombres_originaux = [3, 1, 4, 1, 5]
nombres_tries = sorted(nombres_originaux)
print(nombres_originaux)  # [3, 1, 4, 1, 5]
print(nombres_tries)      # [1, 1, 3, 4, 5]

# Inverser l'ordre de la liste
nombres.reverse()
print(nombres)  # [1, 1, 2, 3, 4, 5, 6, 9]

# --- Trier avec une clé (key) ---
print()
mots = ["python", "go", "javascript", "c"]
print(sorted(mots, key=len))         # ['c', 'go', 'python', 'javascript']

noms = ["alice", "Bob", "charlie", "David"]
print(sorted(noms, key=str.lower))   # ['alice', 'Bob', 'charlie', 'David']

personnes = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
print(sorted(personnes, key=lambda p: p[1]))                # [('Bob', 25), ('Alice', 30), ('Charlie', 35)]
print(sorted(personnes, key=lambda p: p[1], reverse=True))  # [('Charlie', 35), ('Alice', 30), ('Bob', 25)]
