# ============================================================================
#   Section 2.4 : Concaténation et répétition
#   Description : Concaténation avec +, répétition avec *, concaténation
#                 implicite de littéraux
#   Fichier source : 04-chaines-et-regex.md
# ============================================================================

# Concaténation avec +
prenom = "Marie"
nom = "Dupont"
nom_complet = prenom + " " + nom
print(nom_complet)  # Marie Dupont

# Répétition avec *
ligne = "=" * 50
print(ligne)  # ==================================================

# Concaténation implicite (seulement pour les littéraux)
message = "Bonjour " "tout " "le monde"
print(message)  # Bonjour tout le monde
