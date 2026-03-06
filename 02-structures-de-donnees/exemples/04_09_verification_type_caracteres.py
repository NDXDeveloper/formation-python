# ============================================================================
#   Section 2.4 : Vérifications de type de caractères
#   Description : isalnum, isalpha, isdigit, isdecimal, isspace
#   Fichier source : 04-chaines-et-regex.md
# ============================================================================

# Vérifier si alphanumérique
print("Python3".isalnum())   # True
print("Python 3".isalnum())  # False (à cause de l'espace)

# Vérifier si alphabétique
print("Python".isalpha())    # True
print("Python3".isalpha())   # False

# Vérifier si numérique
print("12345".isdigit())     # True
print("123.45".isdigit())    # False

# Vérifier si décimal
print("12345".isdecimal())   # True
print("½".isdecimal())       # False

# Vérifier si espaces
print("   ".isspace())       # True
print("  a ".isspace())      # False
