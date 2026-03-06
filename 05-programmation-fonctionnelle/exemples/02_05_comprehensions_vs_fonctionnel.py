# ============================================================================
#   Section 5.2 : Comparaison avec les compréhensions de listes
#   Description : map() vs compréhension, filter() vs compréhension,
#                 map()+filter() vs compréhension
#   Fichier source : 02-map-filter-reduce.md
# ============================================================================

# --- map() vs compréhension de liste ---
print("=== map() vs compréhension ===")

nombres = [1, 2, 3, 4, 5]

# Avec map()
doubles_map = list(map(lambda x: x * 2, nombres))

# Avec compréhension de liste
doubles_comp = [x * 2 for x in nombres]

print(doubles_map)  # [2, 4, 6, 8, 10]
print(doubles_comp)  # [2, 4, 6, 8, 10]

# --- filter() vs compréhension de liste ---
print("\n=== filter() vs compréhension ===")

nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Avec filter()
pairs_filter = list(filter(lambda x: x % 2 == 0, nombres))

# Avec compréhension de liste
pairs_comp = [x for x in nombres if x % 2 == 0]

print(pairs_filter)  # [2, 4, 6, 8, 10]
print(pairs_comp)    # [2, 4, 6, 8, 10]

# --- map() + filter() vs compréhension de liste ---
print("\n=== map()+filter() vs compréhension ===")

nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Avec map() et filter()
resultat_func = list(map(
    lambda x: x ** 2,
    filter(lambda x: x % 2 == 0, nombres)
))

# Avec compréhension de liste
resultat_comp = [x ** 2 for x in nombres if x % 2 == 0]

print(resultat_func)  # [4, 16, 36, 64, 100]
print(resultat_comp)  # [4, 16, 36, 64, 100]
