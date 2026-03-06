# ============================================================================
#   Section 2.1 : Les Sets - Opérations mathématiques et comparaisons
#   Description : Union, intersection, différence, différence symétrique,
#                 sous-ensemble, sur-ensemble, sets disjoints
#   Fichier source : 01-listes-tuples-dicts-sets.md
# ============================================================================

# --- Opérations mathématiques d'ensembles ---
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union (tous les éléments des deux sets)
union = set1 | set2
print(f"Union : {sorted(union)}")  # [1, 2, 3, 4, 5, 6, 7, 8]

# Intersection (éléments présents dans les deux sets)
intersection = set1 & set2
print(f"Intersection : {sorted(intersection)}")  # [4, 5]

# Différence (éléments dans set1 mais pas dans set2)
difference = set1 - set2
print(f"Différence : {sorted(difference)}")  # [1, 2, 3]

# Différence symétrique (dans l'un ou l'autre, mais pas les deux)
diff_sym = set1 ^ set2
print(f"Diff. symétrique : {sorted(diff_sym)}")  # [1, 2, 3, 6, 7, 8]

# --- Comparaisons de sets ---
print()
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
set3 = {1, 2, 3}

# Égalité
print(f"set1 == set3 : {set1 == set3}")  # True

# Sous-ensemble (subset)
print(f"set1 <= set2 : {set1 <= set2}")          # True
print(f"set1.issubset(set2) : {set1.issubset(set2)}")  # True

# Sous-ensemble strict
print(f"set1 < set2 : {set1 < set2}")  # True

# Sur-ensemble (superset)
print(f"set2 >= set1 : {set2 >= set1}")  # True
print(f"set2.issuperset(set1) : {set2.issuperset(set1)}")  # True

# Sets disjoints (aucun élément en commun)
set_a = {1, 2, 3}
set_b = {4, 5, 6}
print(f"set_a.isdisjoint(set_b) : {set_a.isdisjoint(set_b)}")  # True
