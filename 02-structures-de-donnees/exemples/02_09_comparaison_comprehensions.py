# ============================================================================
#   Section 2.2 : Comparaison liste vs dictionnaire vs set
#   Description : Même problème résolu avec les trois types de compréhension
#   Fichier source : 02-comprehensions.md
# ============================================================================

nombres = [1, 2, 3, 4, 5]

# Compréhension de liste : créer une liste de carrés
carres_liste = [x**2 for x in nombres]
print(f"Liste : {carres_liste}")  # [1, 4, 9, 16, 25]

# Compréhension de dictionnaire : associer nombre → carré
carres_dict = {x: x**2 for x in nombres}
print(f"Dict  : {carres_dict}")  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Compréhension de set : ensemble de carrés (uniques)
nombres_avec_doublons = [1, 2, 2, 3, 3, 4, 5]
carres_set = {x**2 for x in nombres_avec_doublons}
print(f"Set   : {sorted(carres_set)}")  # [1, 4, 9, 16, 25]
