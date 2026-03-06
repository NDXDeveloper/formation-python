# ============================================================================
#   Section 2.1 : Les Tuples - Accéder aux éléments et immuabilité
#   Description : Accès par index, slicing, erreur de modification
#   Fichier source : 01-listes-tuples-dicts-sets.md
# ============================================================================

# --- Accéder aux éléments ---
informations = ("Alice", 25, "Paris", "Ingénieure")

print(informations[0])    # 'Alice'
print(informations[-1])   # 'Ingénieure'
print(informations[1:3])  # (25, 'Paris')

# --- Immuabilité ---
coordonnees = (10, 20)

# Ceci provoquera une erreur
try:
    coordonnees[0] = 15
except TypeError as e:
    print(f"TypeError : {e}")
    # TypeError : 'tuple' object does not support item assignment
