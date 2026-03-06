# ============================================================================
#   Section 2.14 : Les Opérateurs d'Identité
#   Description : is, is not - tester si deux variables référencent le même objet
#   Fichier source : 02-variables-types-et-operateurs.md
# ============================================================================

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)   # Affiche : True (même valeur)
print(a is b)   # Affiche : False (objets différents en mémoire)
print(a is c)   # Affiche : True (c pointe vers le même objet que a)

# Cas particulier avec None
valeur = None
print(valeur is None)      # Affiche : True (recommandé)
print(valeur == None)      # Affiche : True (fonctionne mais moins idiomatique)
