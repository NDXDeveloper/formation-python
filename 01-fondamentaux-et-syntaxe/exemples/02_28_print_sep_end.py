# ============================================================================
#   Section 2.28 : Les paramètres de print() : sep et end
#   Description : sep (séparateur entre arguments) et end (fin de ligne) ;
#                 comportement par défaut (espace entre args + retour à la ligne)
#   Fichier source : 02-variables-types-et-operateurs.md
# ============================================================================

# Par défaut : arguments séparés par une espace, ligne finie par "\n"
print("a", "b", "c")                # a b c

# sep : changer le séparateur entre les arguments
print("a", "b", "c", sep="-")       # a-b-c
print("2024", "12", "25", sep="/")  # 2024/12/25

# end : changer ce qui termine la ligne (par défaut "\n")
print("Chargement", end="...")
print("terminé")                    # Chargement...terminé (sur une seule ligne)

# Combiner sep et end
print("x", "y", sep="", end="!\n")  # xy!
