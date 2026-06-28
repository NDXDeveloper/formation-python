# ============================================================================
#   Section 5.4 : La valeur par défaut de next()
#   Description : next(gen, défaut) évite StopIteration ; idiome du "premier
#                 élément correspondant" avec une expression génératrice
#   Fichier source : 04-generateurs.md
# ============================================================================

# --- next() avec valeur par défaut : pas de StopIteration ---
print("=== next(gen, défaut) ===")
gen = (x for x in [10, 20])
print(next(gen, None))   # 10
print(next(gen, None))   # 20
print(next(gen, None))   # None -- épuisé, mais aucune erreur

# --- Idiome : premier élément correspondant à une condition ---
print("\n=== Premier élément correspondant ===")
nombres = [1, 3, 5, 8, 9, 10]

# Premier nombre pair (ou None s'il n'y en a aucun)
premier_pair = next((x for x in nombres if x % 2 == 0), None)
print("Premier pair :", premier_pair)   # 8

# Aucun élément ne correspond -> on récupère la valeur par défaut
aucun = next((x for x in nombres if x > 100), None)
print("Aucun match  :", aucun)          # None

# La recherche est paresseuse : elle s'arrête dès le premier élément trouvé,
# contrairement à [x for x in nombres if ...][0] qui parcourt toute la liste.
