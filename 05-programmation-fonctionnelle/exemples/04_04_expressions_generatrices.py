# ============================================================================
#   Section 5.4 : Expressions génératrices
#   Description : Syntaxe compacte, comparaison avec compréhensions,
#                 filtrage, somme efficace, chaîner des générateurs
#   Fichier source : 04-generateurs.md
# ============================================================================

# --- Comparaison liste vs expression génératrice ---
print("=== Comparaison ===")

# Compréhension de liste
carres_liste = [x ** 2 for x in range(5)]
print(carres_liste)  # [0, 1, 4, 9, 16]
print(type(carres_liste))  # <class 'list'>

# Expression génératrice
carres_gen = (x ** 2 for x in range(5))
print(carres_gen)  # <generator object <genexpr> at 0x...>
print(type(carres_gen))  # <class 'generator'>

# Convertir en liste
print(list(carres_gen))  # [0, 1, 4, 9, 16]

# --- Filtrage et transformation ---
print("\n=== Filtrage et transformation ===")

nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pairs_doubles_gen = (x * 2 for x in nombres if x % 2 == 0)

print(list(pairs_doubles_gen))  # [4, 8, 12, 16, 20]

# --- Somme efficace ---
print("\n=== Somme efficace ===")

# Plus efficace : utilise un générateur (pas de liste intermédiaire)
somme = sum(x ** 2 for x in range(1000000))

print(f"Somme des carrés : {somme}")

# --- Chaîner des générateurs ---
print("\n=== Chaîner ===")

nombres = range(20)

# Filtrer les pairs
pairs = (x for x in nombres if x % 2 == 0)

# Mettre au carré
carres = (x ** 2 for x in pairs)

# Filtrer ceux supérieurs à 50
grands = (x for x in carres if x > 50)

print(list(grands))  # [64, 100, 144, 196, 256, 324]
