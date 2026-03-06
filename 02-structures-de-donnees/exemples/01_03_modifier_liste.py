# ============================================================================
#   Section 2.1 : Les Listes - Modifier une liste
#   Description : Modifier, ajouter (append, insert, extend) des éléments
#   Fichier source : 01-listes-tuples-dicts-sets.md
# ============================================================================

fruits = ["pomme", "banane", "orange"]

# Modifier un élément
fruits[1] = "mangue"
print(fruits)  # ['pomme', 'mangue', 'orange']

# Ajouter un élément à la fin
fruits.append("fraise")
print(fruits)  # ['pomme', 'mangue', 'orange', 'fraise']

# Insérer un élément à une position spécifique
fruits.insert(1, "kiwi")
print(fruits)  # ['pomme', 'kiwi', 'mangue', 'orange', 'fraise']

# Étendre la liste avec une autre liste
fruits.extend(["cerise", "raisin"])
print(fruits)  # ['pomme', 'kiwi', 'mangue', 'orange', 'fraise', 'cerise', 'raisin']
