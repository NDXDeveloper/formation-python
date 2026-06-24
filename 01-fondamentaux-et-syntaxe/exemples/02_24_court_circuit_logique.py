# ============================================================================
#   Section 2.24 : Court-circuit de and / or (valeurs de retour)
#   Description : and/or renvoient l'une des valeurs ; idiome de la valeur par défaut
#   Fichier source : 02-variables-types-et-operateurs.md
# ============================================================================

# and / or renvoient l'une des deux VALEURS, pas forcément un booléen
print(5 and 3)        # 3  (1er vrai -> and renvoie le 2e)
print(0 and 3)        # 0  (1er faux -> and s'arrete dessus)
print(0 or "défaut")  # défaut  (or renvoie la 1re valeur « vraie »)
print("Alice" or "Anonyme")  # Alice

# Idiome courant : la valeur par défaut
nom = ""                       # une chaîne vide est « fausse »
affichage = nom or "Anonyme"   # si nom est vide/faux, on prend "Anonyme"
print(affichage)               # Anonyme
