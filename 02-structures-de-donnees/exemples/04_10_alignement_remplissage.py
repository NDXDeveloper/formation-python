# ============================================================================
#   Section 2.4 : Alignement et remplissage
#   Description : center, ljust, rjust, zfill
#   Fichier source : 04-chaines-et-regex.md
# ============================================================================

texte = "Python"

# Centrer
print(f"'{texte.center(20)}'")       # '       Python       '
print(f"'{texte.center(20, '*')}'")  # '*******Python*******'

# Aligner à gauche
print(f"'{texte.ljust(20)}'")        # 'Python              '
print(f"'{texte.ljust(20, '-')}'")   # 'Python--------------'

# Aligner à droite
print(f"'{texte.rjust(20)}'")        # '              Python'
print(f"'{texte.rjust(20, '.')}'")   # '..............Python'

# Remplir avec des zéros (utile pour les nombres)
nombre = "42"
print(nombre.zfill(5))        # 00042
print("-42".zfill(5))         # -0042
