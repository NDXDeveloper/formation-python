# ============================================================================
#   Section 2.1 : Les Tuples - Unpacking (déballage)
#   Description : Unpacking simple, partiel avec *, échange de variables
#   Fichier source : 01-listes-tuples-dicts-sets.md
# ============================================================================

# Unpacking simple
coordonnees = (10, 20)
x, y = coordonnees
print(x)  # 10
print(y)  # 20

# Unpacking avec plusieurs valeurs
personne = ("Alice", 25, "Paris", "Ingénieure")
nom, age, ville, profession = personne
print(nom)  # Alice

# Unpacking partiel avec *
nombres = (1, 2, 3, 4, 5)
premier, *milieu, dernier = nombres
print(premier)  # 1
print(milieu)   # [2, 3, 4]
print(dernier)  # 5

# Échanger des variables facilement
a = 5
b = 10
a, b = b, a
print(a, b)  # 10 5
