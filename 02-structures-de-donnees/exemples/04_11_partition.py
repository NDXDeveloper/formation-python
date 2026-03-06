# ============================================================================
#   Section 2.4 : Partition
#   Description : partition (diviser en 3 parties), rpartition
#   Fichier source : 04-chaines-et-regex.md
# ============================================================================

# Diviser en 3 parties : avant, séparateur, après
email = "utilisateur@example.com"
avant, sep, apres = email.partition('@')
print(avant)  # utilisateur
print(sep)    # @
print(apres)  # example.com

# rpartition - partir de la droite
chemin = "dossier/sous-dossier/fichier.txt"
dossiers, sep, fichier = chemin.rpartition('/')
print(dossiers)  # dossier/sous-dossier
print(fichier)   # fichier.txt
