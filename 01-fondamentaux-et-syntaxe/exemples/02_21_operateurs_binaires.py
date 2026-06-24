# ============================================================================
#   Section 2.21 : Les Opérateurs Binaires (bit à bit)
#   Description : &, |, ^, ~, <<, >> sur les entiers ; bin() pour visualiser
#                 la représentation binaire (section optionnelle, avancée)
#   Fichier source : 02-variables-types-et-operateurs.md
# ============================================================================

# 12 s'écrit 0b1100 en binaire, 10 s'écrit 0b1010
print(12 & 10)   # Affiche : 8  (ET binaire : bits présents dans les deux)
print(12 | 10)   # Affiche : 14 (OU binaire : bits présents dans l'un ou l'autre)
print(12 ^ 10)   # Affiche : 6  (XOR : bits présents dans un seul des deux)
print(~5)        # Affiche : -6 (NON binaire : complément à deux, ~x == -(x+1))

# --- Décalages : multiplier / diviser par des puissances de 2 ---
print(1 << 4)    # Affiche : 16  (décalage à gauche : 1 * 2**4)
print(16 >> 2)   # Affiche : 4   (décalage à droite : 16 // 2**2)

# --- bin() montre la représentation binaire d'un entier ---
print(bin(12))   # Affiche : 0b1100
print(bin(10))   # Affiche : 0b1010
