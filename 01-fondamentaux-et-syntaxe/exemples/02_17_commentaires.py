# ============================================================================
#   Section 2.17 : Commentaires dans le Code
#   Description : Commentaires ligne, multi-lignes, bonnes pratiques
#   Fichier source : 02-variables-types-et-operateurs.md
# ============================================================================

# --- Commentaires sur une ligne ---
# Ceci est un commentaire
age = 25  # Commentaire après du code
print(age)  # 25

# --- Commentaires multi-lignes ---
"""
Ceci est un commentaire
sur plusieurs lignes.
Python l'ignore complètement.
"""

nom = "Alice"
print(nom)  # Alice

# Ceci est également un commentaire
# sur plusieurs lignes
# avec des dièses

# --- Bonnes pratiques ---
# Bon : Expliquer le "pourquoi" et le "comment" complexe
# Conversion des miles en kilomètres (1 mile = 1.60934 km)
distance_miles = 10
distance_km = distance_miles * 1.60934
print(f"{distance_miles} miles = {distance_km} km")  # 10 miles = 16.0934 km

# Mauvais : Répéter ce que le code fait déjà de façon évidente
# Afficher le nom  (commentaire inutile)
print(nom)
