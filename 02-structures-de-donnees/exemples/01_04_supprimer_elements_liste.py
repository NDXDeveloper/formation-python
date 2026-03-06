# ============================================================================
#   Section 2.1 : Les Listes - Supprimer des éléments
#   Description : remove(), pop(), del, clear() pour supprimer des éléments
#   Fichier source : 01-listes-tuples-dicts-sets.md
# ============================================================================

fruits = ["pomme", "banane", "orange", "fraise", "kiwi"]

# Supprimer par valeur
fruits.remove("banane")
print(fruits)  # ['pomme', 'orange', 'fraise', 'kiwi']

# Supprimer par index et récupérer la valeur
fruit_supprime = fruits.pop(2)
print(fruit_supprime)  # 'fraise'
print(fruits)          # ['pomme', 'orange', 'kiwi']

# Supprimer le dernier élément
dernier = fruits.pop()
print(dernier)  # 'kiwi'

# Supprimer un élément par index sans récupérer la valeur
del fruits[0]
print(fruits)  # ['orange']

# Vider complètement la liste
fruits.clear()
print(fruits)  # []
