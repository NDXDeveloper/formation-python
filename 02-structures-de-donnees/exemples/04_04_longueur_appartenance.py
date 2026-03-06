# ============================================================================
#   Section 2.4 : Longueur et appartenance
#   Description : len(), opérateurs in et not in sur les chaînes
#   Fichier source : 04-chaines-et-regex.md
# ============================================================================

texte = "Python est génial"

# Longueur
print(len(texte))  # 17

# Vérifier si un caractère ou sous-chaîne est présent
print('P' in texte)        # True
print('Java' in texte)     # False
print('Python' in texte)   # True
print('est' not in texte)  # False
