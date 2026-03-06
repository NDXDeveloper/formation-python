# ============================================================================
#   Section 2.13 : Les Opérateurs d'Appartenance
#   Description : in, not in - tester la présence dans une séquence
#   Fichier source : 02-variables-types-et-operateurs.md
# ============================================================================

texte = "Python est génial"

print("Python" in texte)     # Affiche : True
print("Java" in texte)       # Affiche : False
print("Java" not in texte)   # Affiche : True

# Vérifier si une chaîne contient une lettre
mot = "Bonjour"
print("o" in mot)  # Affiche : True
print("z" in mot)  # Affiche : False
