# ============================================================================
#   Section 2.2 : Compréhensions de listes - Avec condition (filtre)
#   Description : Filtrer avec if, nombres pairs, positifs, mots courts,
#                 comparaison boucle vs compréhension
#   Fichier source : 02-comprehensions.md
# ============================================================================

# Garder seulement les nombres pairs
nombres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
pairs = [x for x in nombres if x % 2 == 0]
print(pairs)  # [0, 2, 4, 6, 8]

# Garder seulement les nombres positifs
nombres = [-2, -1, 0, 1, 2, 3]
positifs = [x for x in nombres if x > 0]
print(positifs)  # [1, 2, 3]

# Filtrer les mots courts (moins de 5 lettres)
mots = ["chat", "éléphant", "oiseau", "souris"]
mots_courts = [mot for mot in mots if len(mot) < 5]
print(mots_courts)  # ['chat']

# Extraire les nombres pairs et les mettre au carré
nombres = range(10)
carres_pairs = [x ** 2 for x in nombres if x % 2 == 0]
print(carres_pairs)  # [0, 4, 16, 36, 64]

# --- Comparaison : boucle vs compréhension ---
mots = ["chat", "chien", "oiseau", "poisson"]

# Avec une boucle traditionnelle
longueurs = []
for mot in mots:
    if 'a' in mot:
        longueurs.append(len(mot))
print(longueurs)  # [4, 6]

# Avec une compréhension de liste
longueurs = [len(mot) for mot in mots if 'a' in mot]
print(longueurs)  # [4, 6]
