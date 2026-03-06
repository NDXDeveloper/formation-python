# ============================================================================
#   Section 2.4 : Indexation et slicing
#   Description : Accès par indice, slicing avec pas, immutabilité des chaînes
#   Fichier source : 04-chaines-et-regex.md
# ============================================================================

texte = "Python"

# Indexation
print(texte[0])   # P
print(texte[2])   # t
print(texte[-1])  # n (dernier caractère)
print(texte[-2])  # o (avant-dernier)

# Slicing
print(texte[0:3])   # Pyt (indices 0, 1, 2)
print(texte[:4])    # Pyth (du début à l'indice 3)
print(texte[2:])    # thon (de l'indice 2 à la fin)
print(texte[::2])   # Pto (un caractère sur deux)
print(texte[::-1])  # nohtyP (inverse la chaîne)

# Les chaînes sont IMMUABLES
try:
    texte[0] = 'J'
except TypeError as e:
    print(f"TypeError: {e}")
