# ============================================================================
#   Section 2.4 : Recherche et remplacement
#   Description : find, index, count, startswith, endswith, replace
#   Fichier source : 04-chaines-et-regex.md
# ============================================================================

texte = "Python est un langage Python"

# Trouver une sous-chaîne
print(texte.find('Python'))        # 0 (première occurrence)
print(texte.find('Java'))          # -1 (non trouvé)
print(texte.find('Python', 1))     # 22 (chercher après l'indice 1)

# Index (comme find, mais lève une erreur si non trouvé)
print(texte.index('Python'))       # 0
try:
    print(texte.index('Java'))
except ValueError as e:
    print(f"ValueError: {e}")

# Compter les occurrences
print(texte.count('Python'))       # 2
print(texte.count('est'))          # 1

# Vérifier le début et la fin
print(texte.startswith('Python'))  # True
print(texte.startswith('Java'))    # False
print(texte.endswith('Python'))    # True
print(texte.endswith('langage'))   # False

# Remplacer
nouveau = texte.replace('Python', 'Java')
print(nouveau)  # Java est un langage Java

# Remplacer avec limite de nombre de remplacements
nouveau = texte.replace('Python', 'Java', 1)
print(nouveau)  # Java est un langage Python (seule la première occurrence)
