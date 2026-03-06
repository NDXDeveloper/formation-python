# ============================================================================
#   Section 2.1 : Les Sets - Ajouter et supprimer des éléments
#   Description : add(), update(), remove(), discard(), pop(), clear()
#   Fichier source : 01-listes-tuples-dicts-sets.md
# ============================================================================

fruits = {"pomme", "banane"}

# Ajouter un élément
fruits.add("orange")
print(sorted(fruits))  # ['banane', 'orange', 'pomme']

# Ajouter plusieurs éléments
fruits.update(["fraise", "kiwi"])
print(sorted(fruits))  # ['banane', 'fraise', 'kiwi', 'orange', 'pomme']

# Supprimer un élément (lève une erreur si l'élément n'existe pas)
fruits.remove("banane")
print(sorted(fruits))  # ['fraise', 'kiwi', 'orange', 'pomme']

# Supprimer un élément (ne lève pas d'erreur si absent)
fruits.discard("mangue")  # Pas d'erreur
print(sorted(fruits))  # Inchangé

# Supprimer et retourner un élément arbitraire
fruit = fruits.pop()
print(f"Retiré : {fruit}")
print(f"Restants : {sorted(fruits)}")

# Vider le set
fruits.clear()
print(fruits)  # set()

# --- Opérations sur les sets ---
nombres = {1, 2, 3, 4, 5}

# Nombre d'éléments
print(f"\nlen = {len(nombres)}")  # 5

# Vérifier si un élément est dans le set
print(f"3 in nombres : {3 in nombres}")   # True
print(f"10 in nombres : {10 in nombres}")  # False
