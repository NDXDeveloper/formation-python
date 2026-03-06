# ============================================================================
#   Section 2.6 : Les Booléens (bool)
#   Description : Valeurs True/False, résultat de comparaisons, conversions
#   Fichier source : 02-variables-types-et-operateurs.md
# ============================================================================

# --- Booléens de base ---
est_majeur = True
est_connecte = False

print(est_majeur)    # True
print(est_connecte)  # False

# --- Booléens comme résultat de comparaisons ---
age = 20
est_majeur = age >= 18
print(est_majeur)  # Affiche : True

# --- Conversions en booléen ---
print(bool(1))       # Affiche : True
print(bool(0))       # Affiche : False
print(bool(""))      # Affiche : False
print(bool("texte")) # Affiche : True
print(bool(-5))      # Affiche : True
