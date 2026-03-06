# ============================================================================
#   Section 2.5 : Les Chaînes de Caractères (str)
#   Description : Création, guillemets, multi-lignes, concaténation, répétition,
#                 indexation, longueur, méthodes courantes
#   Fichier source : 02-variables-types-et-operateurs.md
# ============================================================================

# --- Création de chaînes ---
prenom = "Alice"
nom = 'Dupont'
phrase = "J'aime Python !"

print(prenom)  # Alice
print(nom)     # Dupont
print(phrase)  # J'aime Python !

# --- Guillemets simples vs doubles ---
message1 = "J'aime Python"       # Plus lisible
message2 = 'J\'aime Python'      # Nécessite d'échapper l'apostrophe
print(message1)  # J'aime Python
print(message2)  # J'aime Python

# --- Chaînes multi-lignes ---
poeme = """
Roses sont rouges,
Violettes sont bleues,
Python est génial,
Et vous l'aimerez aussi !
"""
print(poeme)

# --- Concaténation de chaînes ---
prenom = "Alice"
nom = "Dupont"
nom_complet = prenom + " " + nom
print(nom_complet)  # Affiche : Alice Dupont

# --- Répétition de chaînes ---
rire = "Ha" * 5
print(rire)  # Affiche : HaHaHaHaHa

ligne = "-" * 40
print(ligne)  # Affiche une ligne de 40 tirets

# --- Accéder aux caractères (indexation) ---
mot = "Python"
print(mot[0])   # Affiche : P (premier caractère)
print(mot[1])   # Affiche : y (deuxième caractère)
print(mot[-1])  # Affiche : n (dernier caractère)
print(mot[-2])  # Affiche : o (avant-dernier caractère)

# --- Longueur d'une chaîne ---
texte = "Bonjour"
longueur = len(texte)
print(longueur)  # Affiche : 7

# --- Méthodes courantes des chaînes ---
texte = "  Bonjour Python  "

# Convertir en majuscules / minuscules
print(texte.upper())      # Affiche :   BONJOUR PYTHON
print(texte.lower())      # Affiche :   bonjour python

# Supprimer les espaces aux extrémités
print(texte.strip())      # Affiche : Bonjour Python

# Remplacer du texte
print(texte.replace("Python", "monde"))  # Affiche :   Bonjour monde

# Vérifier le contenu
print(texte.startswith("  Bon"))  # Affiche : True
print(texte.endswith("thon  "))   # Affiche : True
print("Python" in texte)          # Affiche : True
