# ============================================================================
#   Section 2.8 : Vérifier le Type d'une Variable
#   Description : Utilisation de la fonction type() sur différents types
#   Fichier source : 02-variables-types-et-operateurs.md
# ============================================================================

age = 25
print(type(age))  # Affiche : <class 'int'>

taille = 1.75
print(type(taille))  # Affiche : <class 'float'>

nom = "Alice"
print(type(nom))  # Affiche : <class 'str'>

est_majeur = True
print(type(est_majeur))  # Affiche : <class 'bool'>

vide = None
print(type(vide))  # Affiche : <class 'NoneType'>
