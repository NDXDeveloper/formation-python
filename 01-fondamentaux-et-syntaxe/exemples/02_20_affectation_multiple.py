# ============================================================================
#   Section 2.20 : Affectation multiple
#   Description : Affecter plusieurs variables d'un coup, affectation chaînée,
#                 échange de deux variables sans variable temporaire
#   Fichier source : 02-variables-types-et-operateurs.md
# ============================================================================

# --- Affecter plusieurs variables à la fois ---
x, y, z = 1, 2, 3
print(x)  # Affiche : 1
print(y)  # Affiche : 2
print(z)  # Affiche : 3

# --- Donner la même valeur à plusieurs variables (affectation chaînée) ---
a = b = c = 0
print(a, b, c)  # Affiche : 0 0 0

# --- Échanger le contenu de deux variables (sans variable temporaire) ---
x = 10
y = 20
x, y = y, x  # Python évalue d'abord la droite (y, x), puis affecte à gauche
print(x, y)  # Affiche : 20 10
