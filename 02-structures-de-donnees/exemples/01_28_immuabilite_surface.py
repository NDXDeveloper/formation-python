# ============================================================================
#   Section 2.1 : Immuabilité « de surface » des tuples
#   Description : un tuple fige ses références, pas le contenu des objets
#                 mutables qu'il pointe ; conséquence sur la hachabilité
#   Fichier source : 01-listes-tuples-dicts-sets.md
# ============================================================================

# --- Un tuple contenant une liste : la liste reste modifiable ---
donnees = (1, [2, 3])

# Remplacer l'élément est interdit (la référence est figée) :
try:
    donnees[1] = [9]
except TypeError as e:
    print("Réassignation interdite :", e)
    # 'tuple' object does not support item assignment

# Mais modifier la liste pointée fonctionne, car elle est mutable :
donnees[1].append(4)
print(donnees)                          # (1, [2, 3, 4]) -- le contenu a changé !

# --- Conséquence : la hachabilité ---
# Un tuple n'est hachable que si TOUS ses éléments le sont aussi.
print(hash((1, 2, 3)) is not None)      # True : que des éléments immuables

# Dès qu'il contient une liste, il n'est plus hachable :
try:
    hash((1, [2, 3]))
except TypeError as e:
    print("Non hachable :", e)          # unhashable type: 'list'

# Donc impossible comme clé de dict ou élément d'un set :
try:
    _ = {(1, [2, 3])}
except TypeError as e:
    print("Impossible dans un set :", e)  # unhashable type: 'list'
