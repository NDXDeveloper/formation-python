# ============================================================================
#   Section 2.25 : isinstance() - tester le type d'une variable
#   Description : isinstance(x, type) vs type() ; test multi-types ; héritage
#   Fichier source : 02-variables-types-et-operateurs.md
# ============================================================================

age = 25
print(isinstance(age, int))     # True
print(isinstance(age, str))     # False

nom = "Alice"
print(isinstance(nom, str))     # True

# Tester plusieurs types à la fois (avec un tuple)
valeur = 3.14
print(isinstance(valeur, (int, float)))  # True

# isinstance tient compte de l'héritage : en Python, un bool EST un int
print(isinstance(True, int))    # True  (bool hérite de int)
print(type(True) == int)        # False (type() ne voit pas l'héritage)
