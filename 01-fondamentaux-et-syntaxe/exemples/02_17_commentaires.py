# ============================================================================
#   Section 2.17 : Commentaires dans le Code
#   Description : Commentaires ligne, multi-lignes, bonnes pratiques
#   Fichier source : 02-variables-types-et-operateurs.md
# ============================================================================

# --- Commentaires sur une ligne ---
# Ceci est un commentaire
age = 25  # Commentaire après du code
print(age)  # 25

# --- "Commentaires" multi-lignes : ATTENTION, ce ne sont pas de vrais commentaires ! ---
# Une chaîne entre triple guillemets n'est PAS un commentaire : c'est une chaîne de
# caractères que Python crée puis ignore si on ne l'utilise pas. Son seul rôle spécial
# est d'être une docstring (1re instruction d'une fonction/classe/module, voir 1.4).
"""
Ceci ressemble à un commentaire,
mais c'est en réalité une chaîne de caractères.
Python n'en fait rien ici (elle est créée puis ignorée).
"""

nom = "Alice"
print(nom)  # Alice

# La vraie façon de "commenter" sur plusieurs lignes : préfixer CHAQUE ligne par #
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
